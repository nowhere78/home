#Requires -Version 5.1
<#
.SYNOPSIS
    Hermes 데스크톱 앱 설치 실패("INSTALL DIDN'T FINISH") 원인 진단 스크립트.

.DESCRIPTION
    bootstrap-installer.log 에서 실제 실패 원인 줄만 뽑아내고,
    Node/npm/디스크/프로세스/네트워크 환경을 함께 점검해 유력 원인과 조치를 출력한다.
    아무것도 삭제하거나 수정하지 않는 읽기 전용 스크립트다.

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .\scripts\hermes-install-diagnose.ps1
#>
[CmdletBinding()]
param(
    [string]$LogPath      = (Join-Path $env:LOCALAPPDATA 'hermes\logs\bootstrap-installer.log'),
    [int]   $TailLines    = 80,
    [int]   $ContextLines = 150,
    [string]$ReportPath = (Join-Path ([Environment]::GetFolderPath('Desktop')) 'hermes-install-report.txt')
)

$ErrorActionPreference = 'Continue'
$script:Report = New-Object System.Collections.Generic.List[string]

function Say {
    param([string]$Text = '', [string]$Color = 'Gray')
    Write-Host $Text -ForegroundColor $Color
    $script:Report.Add($Text)
}

function Section { param([string]$Title) Say ''; Say ("=== $Title " + ('=' * [Math]::Max(0, 60 - $Title.Length))) 'Cyan' }

Say "Hermes 설치 진단 - $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" 'White'

# ---------------------------------------------------------------- 1. 로그 파싱
Section '1. 설치 로그'

if (-not (Test-Path -LiteralPath $LogPath)) {
    Say "로그 파일을 찾을 수 없음: $LogPath" 'Red'
    Say '설치 창의 "Open log folder" 버튼으로 실제 경로를 확인한 뒤 -LogPath 로 지정하세요.' 'Yellow'
    $lines = @()
} else {
    $logFile = Get-Item -LiteralPath $LogPath
    Say ("경로   : " + $logFile.FullName)
    Say ("크기   : {0:N0} bytes" -f $logFile.Length)
    Say ("수정일 : " + $logFile.LastWriteTime)
    $lines = Get-Content -LiteralPath $LogPath -ErrorAction SilentlyContinue
    Say ("줄 수  : {0:N0}" -f $lines.Count)
}

# 우선순위가 높은(= 위쪽에 있는) 규칙일수록 유력 원인으로 본다.
$rules = @(
    # 2026-08-07 실제 확인된 원인. npm 11.11.0 이 Hermes 의 허용 범위
    # {"npm":"<11.10.0 || >=11.17.0"} 한가운데(금지 구간)에 걸려서 실패했다.
    @{ Name    = 'Node/npm 버전 불일치 (EBADENGINE) - 실제 확인된 원인'
       Pattern = 'EBADENGINE|Unsupported engine|notsup|Not compatible with your version of node/npm'
       Fix     = @('Node 나 npm 버전이 Hermes 요구 범위를 벗어났습니다. 파일 잠김이나 재설치와 무관하며, 버전만 맞추면 됩니다.',
                   '아래 "engine 요구/실제 버전"을 보고 어느 쪽이 어긋났는지 확인하세요.',
                   'npm 이 문제면:  npm install -g npm@latest   (그래도 범위 밖이면  npm install -g "npm@<11.10.0")',
                   'Node 가 문제면: 요구 범위에 맞는 LTS 를 설치하세요(예: winget install OpenJS.NodeJS.LTS).',
                   '버전을 맞춘 뒤 Hermes 창의 [Retry install] 을 누르면 됩니다.') },

    @{ Name    = '네이티브 모듈 빌드 실패 (node-gyp / Visual Studio / Python 없음)'
       Pattern = 'gyp ERR!|node-gyp|MSB\d{4}|Visual Studio|msvs|python.*not found|Could not find any Visual Studio'
       Fix     = @('Visual Studio Build Tools(C++ 빌드 도구)와 Python 3.x 설치가 필요합니다.',
                   '  winget install Microsoft.VisualStudio.2022.BuildTools --override "--quiet --add Microsoft.VisualStudio.Workload.VCTools --includeRecommended"',
                   '  winget install Python.Python.3.12',
                   '설치 후 PowerShell을 새로 열고 재설치하세요.') },

    @{ Name    = '파일 잠김 / 삭제 실패 (EPERM, EBUSY, ENOTEMPTY)'
       Pattern = 'EPERM|EBUSY|ENOTEMPTY|operation not permitted|resource busy or locked|being used by another process'
       Fix     = @('이전 Hermes(또는 그 node 프로세스)가 살아 있어서 파일을 못 지우는 상태입니다. 가장 흔한 "기존 설치 때문에 나는" 오류입니다.',
                   'Hermes 창을 모두 닫고 hermes-clean-reinstall.ps1 -Force 를 실행하세요.',
                   '백신(실시간 검사)이 node_modules 를 잡는 경우도 있으니 설치 폴더를 예외로 등록해 보세요.') },

    @{ Name    = 'npm 캐시 손상 (EINTEGRITY, checksum 불일치)'
       Pattern = 'EINTEGRITY|sha512-.*integrity checksum failed|Integrity check failed'
       Fix     = @('npm 캐시가 깨졌습니다.  npm cache clean --force  후 재설치하세요.') },

    @{ Name    = '의존성 충돌 (ERESOLVE)'
       Pattern = 'ERESOLVE|could not resolve dependency|peer dep'
       Fix     = @('peer dependency 충돌입니다. 설치 폴더에서 다음을 시도하세요.',
                   '  npm install --legacy-peer-deps',
                   '반복되면 Hermes 배포판 자체 문제일 수 있으니 최신 인스톨러를 다시 받으세요.') },

    @{ Name    = '패키지/버전 없음 (E404, ETARGET)'
       Pattern = 'E404|ETARGET|notarget|No matching version found|404 Not Found - GET'
       Fix     = @('요청한 패키지 버전이 레지스트리에 없습니다.',
                   'npm config get registry 결과가 https://registry.npmjs.org/ 인지 확인하고,',
                   '사내 미러/프록시가 설정돼 있으면 해제 후 재시도하세요.') },

    @{ Name    = '네트워크 / 프록시 / 방화벽'
       Pattern = 'ECONNRESET|ETIMEDOUT|ENOTFOUND|EAI_AGAIN|ECONNREFUSED|socket hang up|network.*request to.*failed|self signed certificate|UNABLE_TO_VERIFY|CERT_'
       Fix     = @('레지스트리 접속이 막혔습니다. VPN/사내 프록시/백신 SSL 검사를 끄고 재시도하세요.',
                   '  npm config delete proxy ; npm config delete https-proxy',
                   '  npm config set registry https://registry.npmjs.org/') },

    @{ Name    = '경로 길이 초과 (MAX_PATH)'
       Pattern = 'ENAMETOOLONG|path too long|The specified path, file name, or both are too long'
       Fix     = @('Windows 260자 경로 제한입니다. 관리자 PowerShell에서 긴 경로를 켜세요.',
                   '  New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name LongPathsEnabled -Value 1 -PropertyType DWORD -Force',
                   '이후 재부팅하고 재설치하세요.') },

    @{ Name    = '디스크 공간 부족 (ENOSPC)'
       Pattern = 'ENOSPC|no space left|not enough space|디스크 공간'
       Fix     = @('C: 드라이브 공간을 확보한 뒤 재설치하세요(최소 2~3GB 권장).') },

    @{ Name    = '권한 부족 (EACCES)'
       Pattern = 'EACCES|access is denied|액세스가 거부'
       Fix     = @('설치 프로그램을 "관리자 권한으로 실행"으로 다시 실행해 보세요.') },

    @{ Name    = '파일 없음 (ENOENT) / 워크스페이스 손상'
       Pattern = 'ENOENT|no such file or directory|Cannot find module'
       Fix     = @('설치 파일이 제대로 풀리지 않았거나 node_modules 가 깨졌습니다.',
                   'hermes-clean-reinstall.ps1 -Mode Hard -Force 로 완전 정리 후 재설치하세요.') }
)

$hits = @()
if ($lines.Count -gt 0) {
    foreach ($rule in $rules) {
        $matched = $lines | Select-String -Pattern $rule.Pattern -AllMatches
        if ($matched) {
            $hits += [pscustomobject]@{ Rule = $rule; Count = $matched.Count; Samples = ($matched | Select-Object -First 3) }
        }
    }
}

Section '2. 로그에서 발견된 오류 신호'
if ($hits.Count -eq 0) {
    Say '알려진 오류 패턴이 잡히지 않았습니다. 아래 4번의 로그 꼬리를 확인하세요.' 'Yellow'
} else {
    foreach ($h in $hits) {
        Say ("[{0}회] {1}" -f $h.Count, $h.Rule.Name) 'Yellow'
        foreach ($s in $h.Samples) {
            $t = $s.Line.Trim()
            if ($t.Length -gt 200) { $t = $t.Substring(0, 200) + ' ...' }
            Say ("    L{0}: {1}" -f $s.LineNumber, $t)
        }
    }
}

# engine 오류는 요구/실제 버전이 로그에 그대로 찍히므로 따로 뽑아서 보여준다.
if ($lines.Count -gt 0) {
    $engineLines = $lines | Select-String -Pattern 'notsup (Required|Actual)' | Select-Object -Last 4
    if ($engineLines) {
        Say ''
        Say 'engine 요구/실제 버전:' 'Green'
        $engineLines | ForEach-Object { Say ('    ' + ($_.Line -replace '^.*npm error ', '').Trim()) }
        Say '    → 요구 범위를 벗어난 쪽(node 또는 npm)만 맞추면 해결됩니다.' 'Green'
    }
}

# --------------------------------------------- 2-1. "see lines above" 지점 잘라내기
# 화면에 뜨는 "desktop workspace npm install failed (exit 1) -- see lines above for cause"
# 는 결과 통보일 뿐이고, 진짜 원인은 그 줄 "바로 위"에 찍혀 있다. 그 구간만 뽑아낸다.
Section '2-1. 실패 선언 직전 구간 (진짜 원인 위치)'

$failMarker = 'npm install failed \(exit \d+\)|see lines above for cause|INSTALL DIDN''T FINISH|install did ?n.t finish'
$failHit = $null
if ($lines.Count -gt 0) {
    $failHit = $lines | Select-String -Pattern $failMarker | Select-Object -Last 1
}

if (-not $failHit) {
    Say '실패 선언 줄을 찾지 못했습니다. 아래 4번(로그 꼬리)을 대신 보세요.' 'Yellow'
} else {
    $idx   = $failHit.LineNumber - 1              # 0-based
    $start = [Math]::Max(0, $idx - $ContextLines)
    Say ("실패 선언 위치: L{0}  →  L{1}~L{2} 구간을 출력합니다." -f $failHit.LineNumber, ($start + 1), ($idx + 1)) 'Yellow'
    Say ''

    # 이 구간 안에서 오류로 보이는 줄은 화면에서 노랗게 강조
    for ($i = $start; $i -le $idx; $i++) {
        $t = $lines[$i]
        if ($null -eq $t) { continue }
        if ($t.Length -gt 300) { $t = $t.Substring(0, 300) + ' ...' }
        $line = "L{0,-6} {1}" -f ($i + 1), $t
        if ($t -match 'ERR!|error|Error:|failed|EPERM|EBUSY|EACCES|ENOENT|ERESOLVE|EINTEGRITY|E404|ETARGET|ECONN|ETIMEDOUT|gyp ERR!|ENOSPC') {
            Say $line 'Yellow'
        } else {
            Say $line
        }
    }
}

# ------------------------------------------------------------ 3. 환경 점검
Section '3. 환경 점검'

function Try-Cmd { param([string]$Exe, [string]$ArgLine)
    try { (& $Exe $ArgLine.Split(' ') 2>&1 | Select-Object -First 1) } catch { '(없음)' }
}

Say ("Node       : " + (Try-Cmd 'node' '-v'))
Say ("npm        : " + (Try-Cmd 'npm' '-v'))
Say ("registry   : " + (Try-Cmd 'npm' 'config get registry'))
$proxy = Try-Cmd 'npm' 'config get proxy'
$hproxy = Try-Cmd 'npm' 'config get https-proxy'
Say ("proxy      : $proxy / $hproxy")
if (("$proxy$hproxy" -notmatch 'null') -and ("$proxy$hproxy".Trim())) {
    Say '  → 프록시가 설정돼 있습니다. 사내망이 아니면 해제하세요.' 'Yellow'
}

$drive = Get-PSDrive -Name ($env:LOCALAPPDATA.Substring(0,1)) -ErrorAction SilentlyContinue
if ($drive) { Say ("여유 공간   : {0:N1} GB" -f ($drive.Free / 1GB)) }

$lp = (Get-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem' -Name LongPathsEnabled -ErrorAction SilentlyContinue).LongPathsEnabled
Say ("긴 경로 허용: " + $(if ($lp -eq 1) { '켜짐' } else { '꺼짐 (경로 길이 오류가 있으면 켜야 함)' }))

# 실행 중인 Hermes 관련 프로세스
$roots = @(
    (Join-Path $env:LOCALAPPDATA 'hermes'),
    (Join-Path $env:APPDATA      'hermes'),
    (Join-Path $env:LOCALAPPDATA 'Programs\hermes'),
    (Join-Path $env:USERPROFILE  '.hermes')
) | Where-Object { Test-Path -LiteralPath $_ }

Say ''
Say '설치 폴더 후보:'
if ($roots.Count -eq 0) { Say '  (없음)' } else { $roots | ForEach-Object { Say "  $_" } }

$running = @()
foreach ($p in (Get-Process -ErrorAction SilentlyContinue)) {
    $path = $null
    try { $path = $p.Path } catch { }
    if ($p.ProcessName -match '^hermes' -or ($path -and ($roots | Where-Object { $path -like "$_*" }))) {
        $running += $p
    }
}
Say ''
if ($running.Count -gt 0) {
    Say '실행 중인 Hermes 관련 프로세스 (설치를 막는 주범일 수 있음):' 'Yellow'
    $running | ForEach-Object { Say ("  PID {0,-7} {1}" -f $_.Id, $_.ProcessName) }
} else {
    Say '실행 중인 Hermes 관련 프로세스: 없음'
}

# 잠금 파일 / node_modules
$locks = @()
$mods  = @()
foreach ($r in $roots) {
    $locks += Get-ChildItem -LiteralPath $r -Recurse -Force -Filter '*.lock' -ErrorAction SilentlyContinue
    $mods  += Get-ChildItem -LiteralPath $r -Recurse -Force -Directory -Filter 'node_modules' -ErrorAction SilentlyContinue |
              Where-Object { $_.FullName -notmatch 'node_modules.+node_modules' }
}
Say ''
Say ("잠금 파일    : {0}개" -f $locks.Count)
$locks | Select-Object -First 10 | ForEach-Object { Say ("  " + $_.FullName) }
Say ("node_modules : {0}개" -f $mods.Count)
$mods  | Select-Object -First 10 | ForEach-Object { Say ("  " + $_.FullName) }

# ------------------------------------------------------------ 4. 로그 꼬리
Section "4. 로그 마지막 $TailLines 줄"
if ($lines.Count -gt 0) {
    $lines | Select-Object -Last $TailLines | ForEach-Object {
        $t = $_
        if ($t.Length -gt 300) { $t = $t.Substring(0, 300) + ' ...' }
        Say $t
    }
}

# ------------------------------------------------------------ 5. 결론
Section '5. 유력 원인과 조치'
if ($hits.Count -gt 0) {
    $top = $hits[0]
    Say ("유력 원인: " + $top.Rule.Name) 'Green'
    $top.Rule.Fix | ForEach-Object { Say ("  - " + $_) }
    if ($hits.Count -gt 1) {
        Say ''
        Say '그 외 함께 발견된 신호:'
        $hits | Select-Object -Skip 1 | ForEach-Object { Say ("  - " + $_.Rule.Name) }
    }
} elseif ($running.Count -gt 0) {
    Say '로그에서 명확한 패턴은 못 찾았지만, Hermes 프로세스가 실행 중입니다. 먼저 종료 후 재설치하세요.' 'Yellow'
} else {
    Say '자동 판별 실패. 위 4번 로그 꼬리를 그대로 복사해 문의하세요.' 'Yellow'
}

Say ''
Say '다음 단계:' 'White'
Say '  1) .\scripts\hermes-clean-reinstall.ps1              (삭제 목록 미리보기)'
Say '  2) .\scripts\hermes-clean-reinstall.ps1 -Force       (실제 정리)'
Say '  3) Hermes 인스톨러 재실행 또는 창의 [Retry install] 클릭'

try {
    $script:Report | Set-Content -LiteralPath $ReportPath -Encoding UTF8
    Write-Host ''
    Write-Host "리포트 저장: $ReportPath" -ForegroundColor Green
    Write-Host '이 파일을 그대로 붙여넣어 주면 원인을 더 정확히 짚을 수 있습니다.' -ForegroundColor Green
} catch {
    Write-Host "리포트 저장 실패: $_" -ForegroundColor Red
}
