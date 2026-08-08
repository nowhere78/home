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

## ⭐ 2026-08-07 실제로 확인된 원인 — npm 버전 (EBADENGINE)

이 PC에서 실제로 잡힌 원인은 **npm 버전 하나**였다. 파일 잠김도, 기존 설치 잔여물도 아니었다.

로그 `stage=desktop` 구간:

```
npm error code EBADENGINE
npm error engine Unsupported engine
npm error notsup Not compatible with your version of node/npm: hermes-agent@1.0.0
npm error notsup Required: {"node":">=22.22.0","npm":"<11.10.0 || >=11.17.0"}
npm error notsup Actual:   {"node":"v24.14.1","npm":"11.11.0"}
```

- Node v24.14.1 → 요구(≥22.22.0) **만족**
- npm 11.11.0 → 요구(`<11.10.0 || >=11.17.0`)의 **금지 구간(11.10.0 ~ 11.16.x) 한가운데**. 여기가 원인.

Hermes가 문제 있는 npm 버전대를 의도적으로 배제한 것으로 보인다.
`npm warn Unknown project config "min-release-age-exclude"` 경고도 npm이 기대 버전보다 낮다는 같은 신호다.

**해결 — 버전을 반드시 명시할 것**

```powershell
npm install -g npm@11.19.0
npm -v            # 11.19.0 확인 후 [Retry install]
```

다른 PC(집 컴퓨터 등)에서 같은 화면이 뜨면 Node 버전이 달라 처방이 갈릴 수 있으므로,
버전을 읽어 알아서 판정·수정하는 스크립트를 쓰는 편이 안전하다:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\hermes-fix-npm.ps1
```

node/npm 을 읽어 (a) npm 만 문제면 11.19.0 설치, (b) Node 가 낮으면 Node 부터 올리라고 안내,
(c) 둘 다 정상이면 EBADENGINE 이 원인이 아니라고 알려준다. `-WhatIfOnly` 로 판정만 볼 수도 있다.

⚠️ **`npm install -g npm@latest` 는 이 PC에서 실패한다.** 실제로 시도했을 때:

```
npm error code EBADENGINE
npm error engine Not compatible with your version of node/npm: npm@12.0.2
npm error notsup Required: {"node":"^22.22.2 || ^24.15.0 || >=26.0.0"}
npm error notsup Actual:   {"node":"v24.14.1","npm":"11.11.0"}
```

`npm@latest` = **12.0.2** 인데 이건 Node **24.15.0 이상**을 요구한다. 설치된 Node가 24.14.1 이라
0.0.1 차이로 탈락한다. 그래서 `latest` 대신 **버전을 직접 지정**해야 한다.

2026-08-07 레지스트리 확인 결과:

| 후보 | Node 요구 | 설치 가능? | Hermes 요구(`<11.10.0 \|\| >=11.17.0`) |
|---|---|---|---|
| npm 12.0.2 (`@latest`) | `^22.22.2 \|\| ^24.15.0 \|\| >=26.0.0` | ❌ Node 24.14.1 탈락 | — |
| **npm 11.19.0** | `^20.17.0 \|\| >=22.9.0` | ✅ | ✅ (≥11.17.0) |
| npm 11.9.0 | `^20.17.0 \|\| >=22.9.0` | ✅ | ✅ (<11.10.0) |

11.19.0 이 현재 Node로 설치 가능한 최신이면서 Hermes 조건도 만족하므로 이걸 쓴다.
(11.x 중 11.10.0~11.16.0 구간만 Hermes 가 배제한다. 11.19.0 이 11.x 최고 버전.)

Node 자체를 24.15.0 이상 / 26.x 로 올리면 `npm@latest` 도 쓸 수 있지만, 그럴 필요는 없다.

> 버전 확인 명령:
> `curl -s https://registry.npmjs.org/npm` 로 `versions` / `dist-tags` 와 각 버전의 `engines` 를 직접 조회할 수 있다.

### 같은 원인으로 앞 단계도 실패해 있었다

```
[!] Browser tools npm install failed -- exit code 1
[!] TUI npm install failed -- exit code 1
```

이 둘도 `EBADENGINE`이라 npm을 고치면 함께 해결된다. Retry 후에도 남으면 수동으로:

```powershell
cd "C:\Users\smile\AppData\Local\hermes\hermes-agent"; npm install
cd "C:\Users\smile\AppData\Local\hermes\hermes-agent\ui-tui"; npm install
```

### 이때 하지 않아도 되는 것

Python 쪽(venv 재생성, 의존성 250개, 음성/웨이크워드 24개)과 git 저장소 갱신은 모두 정상 완료였다.
`EBADENGINE`이 원인일 때는 `node_modules` 삭제나 정리 재설치가 **아무 효과가 없다.** 버전만 맞추면 된다.

> 참고: Hermes 설치 단계 순서는
> `repository → venv → dependencies → node-deps → desktop` 이고,
> 로그에서 `stage transition ... state=Failed` 줄을 찾으면 어느 단계에서 죽었는지 바로 보인다.

---

## 0. 이 문장 자체는 원인이 아니다

```
desktop workspace npm install failed (exit 1) -- see lines above for cause
```

문장 끝의 **`see lines above for cause`** 가 핵심이다. 이건 인스톨러가 npm의 종료 코드(1)만
받아 적은 "결과 통보"일 뿐이고, **진짜 원인은 로그에서 이 줄보다 위쪽에 찍혀 있다.**
그래서 이 줄만 보고는 무엇을 고쳐야 할지 알 수 없고, 그 위 구간을 잘라내야 한다.

```powershell
# 실패 선언 줄 위쪽 150줄만 뽑기
$log = "$env:LOCALAPPDATA\hermes\logs\bootstrap-installer.log"
$all = Get-Content $log
$i   = ($all | Select-String 'npm install failed' | Select-Object -Last 1).LineNumber
$all[[Math]::Max(0, $i - 150) .. ($i - 1)]
```

진단 스크립트의 **`2-1. 실패 선언 직전 구간`** 섹션이 이 작업을 자동으로 해주고,
그 구간 안의 오류 줄을 노란색으로 강조해 준다. 구간 길이는 `-ContextLines 300` 처럼 조절한다.
결국 봐야 할 것은 그 구간 안의 `npm ERR!` 첫 덩어리다.

---

## 1. 가장 빠른 길 (스크립트 2개)

로컬 PC(`E:\안티그라비티 자료\brain`)에서 PowerShell을 열고:

```powershell
# (0) npm 버전 문제 자동 수정 - 지금까지 확인된 원인은 전부 이것이었다
powershell -ExecutionPolicy Bypass -File .\scripts\hermes-fix-npm.ps1

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
| `EBADENGINE`, `Unsupported engine`, `notsup` | **Node/npm 버전이 요구 범위 밖** (이 PC의 실제 원인) | 위 ⭐ 항목 참고. `npm install -g npm@latest` |

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
