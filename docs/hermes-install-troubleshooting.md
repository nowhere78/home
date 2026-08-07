# Hermes 데스크톱 앱 설치 실패 대응 ("INSTALL DIDN'T FINISH")

증상 화면:

```
INSTALL DIDN'T FINISH
desktop workspace npm install failed (exit 1) -- see lines above for cause
Log: C:\Users\smile\AppData\Local\hermes\logs\bootstrap-installer.log
```

이 메시지는 **Hermes 인스톨러가 데스크톱 워크스페이스의 `npm install`을 돌리다 실패했다**는 뜻이다.
Hermes 자체가 깨진 게 아니라 npm 단계가 죽은 것이므로, 진짜 원인은 로그(`bootstrap-installer.log`) 안에 있다.
`exit 1`은 결과일 뿐 원인이 아니니 로그를 보지 않고 재설치만 반복하면 같은 자리에서 또 멈춘다.

---

## 1. 가장 빠른 길 (스크립트 2개)

로컬 PC(`E:\안티그라비티 자료\brain`)에서 PowerShell을 열고:

```powershell
# (1) 원인 진단 - 아무것도 지우지 않는 읽기 전용
powershell -ExecutionPolicy Bypass -File .\scripts\hermes-install-diagnose.ps1

# (2) 무엇을 지울지 미리보기
powershell -ExecutionPolicy Bypass -File .\scripts\hermes-clean-reinstall.ps1

# (3) 실제 정리 (프로세스 종료 + 잠금 파일 + node_modules + npm 캐시)
powershell -ExecutionPolicy Bypass -File .\scripts\hermes-clean-reinstall.ps1 -Force
```

(3) 후에 Hermes 창의 **[Retry install]** 을 누르거나 인스톨러를 다시 실행한다.

그래도 안 되면 완전 초기화:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\hermes-clean-reinstall.ps1 -Mode Hard -Force
```

`-Mode Hard`는 설치 폴더를 밀기 전에 설정·데이터 파일(`*.json`, `*.env`, `*.db` 등)을
바탕화면 `hermes-backup-<날짜>` 폴더로 먼저 복사하고, `logs` 폴더는 남긴다.

> `-Force` 없이 실행하면 항상 미리보기(드라이런)다. 삭제 목록을 먼저 눈으로 확인하고 붙이자.

---

## 2. "기존에 깔려 있어서" 나는 오류인 경우

실제로 가장 흔한 패턴이다. 로그에 `EPERM` / `EBUSY` / `ENOTEMPTY` /
`operation not permitted` 가 보이면 이 경우다.

- 이전 Hermes(또는 그 자식 node 프로세스)가 살아 있어서 인스톨러가 `node_modules`를 못 지운다.
- 스크린샷의 `AppData\Local\hermes\logs\__agent.lock` 도 이전 에이전트가 아직 물고 있다는 신호다.
- 백신 실시간 검사가 `node_modules` 파일을 잡고 있어도 같은 오류가 난다.

**조치**

1. Hermes 창을 전부 닫는다(작업 표시줄 아이콘까지).
2. 작업 관리자에서 `hermes*` 프로세스가 남아 있으면 끝낸다.
3. `hermes-clean-reinstall.ps1 -Force` 실행.
4. 그래도 삭제 실패하면 **재부팅 후** 다시 실행(부팅 직후엔 파일 잠금이 없다).
5. 백신에 Hermes 설치 폴더를 예외로 등록한다.

> 스크립트는 **Hermes 설치 폴더에서 실행된 프로세스만** 종료한다.
> 다른 에이전트(알파에이전트, 옵시디언 등)의 node 프로세스는 건드리지 않는다.

---

## 3. 로그에서 원인 직접 찾기

수동으로 볼 때는 아래처럼 오류 줄만 뽑는 게 빠르다. 334KB를 다 읽을 필요가 없다.

```powershell
$log = "$env:LOCALAPPDATA\hermes\logs\bootstrap-installer.log"

# npm 에러 줄만
Select-String -Path $log -Pattern 'npm ERR!' | Select-Object -Last 40

# 대표 에러 코드
Select-String -Path $log -Pattern 'EPERM|EBUSY|EACCES|ENOENT|ERESOLVE|EINTEGRITY|E404|ETARGET|ECONNRESET|ETIMEDOUT|gyp ERR!|ENOSPC'

# 마지막 80줄 (실패 직전 맥락)
Get-Content $log -Tail 80
```

### 오류 코드별 조치

| 로그에 보이는 것 | 원인 | 조치 |
|---|---|---|
| `EPERM`, `EBUSY`, `ENOTEMPTY` | 기존 프로세스/백신이 파일을 잠금 | 2번 항목 |
| `EINTEGRITY`, checksum failed | npm 캐시 손상 | `npm cache clean --force` 후 재설치 |
| `ERESOLVE`, peer dep | 의존성 충돌 | 설치 폴더에서 `npm install --legacy-peer-deps` |
| `E404`, `ETARGET` | 패키지/버전 없음, 미러 레지스트리 | `npm config set registry https://registry.npmjs.org/` |
| `ECONNRESET`, `ETIMEDOUT`, `ENOTFOUND`, `CERT_` | 네트워크·프록시·백신 SSL 검사 | VPN/프록시 해제 후 재시도, `npm config delete proxy` |
| `gyp ERR!`, `MSB####`, `Visual Studio`, `python` | 네이티브 모듈 빌드 도구 없음 | VS Build Tools(C++) + Python 3.x 설치 |
| `ENAMETOOLONG`, path too long | Windows 260자 경로 제한 | `LongPathsEnabled=1` 후 재부팅 |
| `ENOSPC` | 디스크 공간 부족 | C: 2~3GB 이상 확보 |
| `EACCES`, 액세스 거부 | 권한 부족 | 인스톨러를 관리자 권한으로 실행 |
| `Unsupported engine`, `EBADENGINE` | Node 버전 불일치 | Node LTS(20 또는 22)로 맞춤 |

### 네이티브 빌드 도구 설치 (gyp 오류일 때)

```powershell
winget install Microsoft.VisualStudio.2022.BuildTools --override "--quiet --add Microsoft.VisualStudio.Workload.VCTools --includeRecommended"
winget install Python.Python.3.12
```

설치 후 PowerShell을 새로 열고 재설치한다.

### 긴 경로 켜기 (관리자 PowerShell)

```powershell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" `
  -Name LongPathsEnabled -Value 1 -PropertyType DWORD -Force
```

재부팅해야 적용된다.

---

## 4. 완전 수동 재설치 절차

스크립트를 쓰지 않고 손으로 할 경우:

```powershell
# 1) Hermes 종료
Get-Process hermes* -ErrorAction SilentlyContinue | Stop-Process -Force

# 2) 잠금 파일 제거
Remove-Item "$env:LOCALAPPDATA\hermes\logs\__agent.lock" -Force -ErrorAction SilentlyContinue

# 3) node_modules / lock 파일 제거
Get-ChildItem "$env:LOCALAPPDATA\hermes" -Recurse -Directory -Filter node_modules |
    ForEach-Object { Remove-Item $_.FullName -Recurse -Force -ErrorAction SilentlyContinue }
Get-ChildItem "$env:LOCALAPPDATA\hermes" -Recurse -Filter package-lock.json |
    Remove-Item -Force -ErrorAction SilentlyContinue

# 4) npm 캐시 정리
npm cache clean --force

# 5) 인스톨러 재실행 (가능하면 관리자 권한)
```

그래도 실패하면 `%LOCALAPPDATA%\hermes` 폴더 전체를 백업 후 삭제하고 최신 인스톨러를 새로 받는다.

---

## 5. 참고

- 진단 스크립트는 결과를 바탕화면 `hermes-install-report.txt` 로 저장한다.
  원인이 애매하면 그 파일 내용을 그대로 붙여 넣어 문의하면 바로 짚을 수 있다.
- 클라우드/샌드박스 세션(Claude Code on the web)에서는 `C:` 드라이브가 마운트되지 않아
  로그를 직접 읽을 수 없다. 로그 분석은 반드시 **로컬 PC 세션**에서 하거나 리포트를 붙여넣어야 한다.
