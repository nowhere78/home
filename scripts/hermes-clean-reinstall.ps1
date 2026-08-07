#Requires -Version 5.1
<#
.SYNOPSIS
    기존 Hermes 설치 잔여물을 정리해 재설치가 되게 만드는 스크립트.

.DESCRIPTION
    Soft(기본) : Hermes 프로세스 종료 → 잠금 파일 제거 → node_modules / package-lock.json 삭제 → npm 캐시 정리
    Hard       : 위 + 설정/데이터를 바탕화면에 백업한 뒤 설치 폴더 자체를 제거(logs 는 남김)

    -Force 를 주지 않으면 아무것도 지우지 않고 "무엇을 지울지"만 보여준다(드라이런).

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .\scripts\hermes-clean-reinstall.ps1
    powershell -ExecutionPolicy Bypass -File .\scripts\hermes-clean-reinstall.ps1 -Force
    powershell -ExecutionPolicy Bypass -File .\scripts\hermes-clean-reinstall.ps1 -Mode Hard -Force
#>
[CmdletBinding()]
param(
    [ValidateSet('Soft','Hard')]
    [string]  $Mode = 'Soft',
    [string[]]$Roots,
    [switch]  $Force,
    [switch]  $SkipCacheClean
)

$ErrorActionPreference = 'Continue'
$dry = -not $Force

function Info { param($m) Write-Host $m -ForegroundColor Gray }
function Warn { param($m) Write-Host $m -ForegroundColor Yellow }
function Ok   { param($m) Write-Host $m -ForegroundColor Green }
function Head { param($m) Write-Host ''; Write-Host "== $m" -ForegroundColor Cyan }

# 긴 경로/깊은 node_modules 도 확실히 지우는 삭제 헬퍼(robocopy 미러 트릭)
function Remove-Tree {
    param([Parameter(Mandatory)][string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) { return $true }
    try {
        Remove-Item -LiteralPath $Path -Recurse -Force -ErrorAction Stop
        return $true
    } catch {
        $empty = New-Item -ItemType Directory -Path (Join-Path $env:TEMP ('hermes_empty_' + [guid]::NewGuid().ToString('N'))) -Force
        & robocopy $empty.FullName $Path /MIR /NFL /NDL /NJH /NJS /NC /NS /NP | Out-Null
        Remove-Item -LiteralPath $Path   -Recurse -Force -ErrorAction SilentlyContinue
        Remove-Item -LiteralPath $empty.FullName -Recurse -Force -ErrorAction SilentlyContinue
        return -not (Test-Path -LiteralPath $Path)
    }
}

function Get-Size {
    param([string]$Path)
    try {
        (Get-ChildItem -LiteralPath $Path -Recurse -Force -File -ErrorAction SilentlyContinue |
            Measure-Object -Property Length -Sum).Sum
    } catch { 0 }
}

Write-Host "Hermes 정리 재설치 - Mode=$Mode $(if ($dry) { '[미리보기]' } else { '[실제 실행]' })" -ForegroundColor White

# ------------------------------------------------------------ 0. 설치 폴더 탐색
Head '0. 설치 폴더 탐색'
if (-not $Roots -or $Roots.Count -eq 0) {
    $Roots = @(
        (Join-Path $env:LOCALAPPDATA 'hermes'),
        (Join-Path $env:APPDATA      'hermes'),
        (Join-Path $env:LOCALAPPDATA 'Programs\hermes'),
        (Join-Path $env:USERPROFILE  '.hermes')
    )
}
$Roots = $Roots | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -Unique
if ($Roots.Count -eq 0) {
    Warn '설치 폴더를 찾지 못했습니다. -Roots "C:\경로" 로 직접 지정하세요.'
    return
}
$Roots | ForEach-Object { Info "  $_" }

# ------------------------------------------------------------ 1. 프로세스 종료
Head '1. 실행 중인 Hermes 프로세스'
$targets = @()
foreach ($p in (Get-Process -ErrorAction SilentlyContinue)) {
    $path = $null
    try { $path = $p.Path } catch { }
    $underRoot = $false
    if ($path) { foreach ($r in $Roots) { if ($path -like "$r*") { $underRoot = $true; break } } }
    if ($p.ProcessName -match '^hermes' -or $underRoot) { $targets += $p }
}

if ($targets.Count -eq 0) {
    Ok '  종료할 프로세스 없음'
} else {
    foreach ($p in $targets) {
        Info ("  PID {0,-7} {1}  {2}" -f $p.Id, $p.ProcessName, $p.Path)
        if (-not $dry) {
            try { Stop-Process -Id $p.Id -Force -ErrorAction Stop; Ok "    → 종료됨" }
            catch { Warn "    → 종료 실패: $_" }
        }
    }
    if (-not $dry) { Start-Sleep -Seconds 2 }
}
Warn '  ※ 여기서 죽이는 것은 Hermes 설치 폴더에서 실행된 프로세스뿐입니다. 다른 node 작업은 건드리지 않습니다.'

# ------------------------------------------------------------ 2. 잠금 파일
Head '2. 잠금 파일 제거'
$locks = @()
foreach ($r in $Roots) {
    $locks += Get-ChildItem -LiteralPath $r -Recurse -Force -File -ErrorAction SilentlyContinue |
              Where-Object { $_.Extension -eq '.lock' -or $_.Name -like '*.lock' -or $_.Name -eq '__agent.lock' }
}
if ($locks.Count -eq 0) { Ok '  없음' }
foreach ($l in $locks) {
    Info ("  " + $l.FullName)
    if (-not $dry) { Remove-Item -LiteralPath $l.FullName -Force -ErrorAction SilentlyContinue }
}

# ------------------------------------------------------------ 3. node_modules / lock 파일
Head '3. node_modules / package-lock.json'
$mods = @()
$plocks = @()
foreach ($r in $Roots) {
    $mods += Get-ChildItem -LiteralPath $r -Recurse -Force -Directory -Filter 'node_modules' -ErrorAction SilentlyContinue |
             Where-Object { $_.FullName -notmatch 'node_modules[\\/].+[\\/]node_modules' }
    $plocks += Get-ChildItem -LiteralPath $r -Recurse -Force -File -ErrorAction SilentlyContinue |
               Where-Object { $_.Name -in @('package-lock.json','npm-shrinkwrap.json') -and $_.FullName -notmatch 'node_modules' }
}

if ($mods.Count -eq 0 -and $plocks.Count -eq 0) { Ok '  삭제할 항목 없음' }
foreach ($m in $mods) {
    $size = Get-Size $m.FullName
    Info ("  [{0,8:N1} MB] {1}" -f ($size / 1MB), $m.FullName)
    if (-not $dry) {
        if (Remove-Tree $m.FullName) { Ok '    → 삭제 완료' } else { Warn '    → 삭제 실패(파일 잠김 가능). 재부팅 후 다시 실행하세요.' }
    }
}
foreach ($f in $plocks) {
    Info ("  " + $f.FullName)
    if (-not $dry) { Remove-Item -LiteralPath $f.FullName -Force -ErrorAction SilentlyContinue }
}

# ------------------------------------------------------------ 4. Hard 모드: 백업 후 폴더 제거
if ($Mode -eq 'Hard') {
    Head '4. Hard 모드 - 설정 백업 후 설치 폴더 제거'
    $desktop   = [Environment]::GetFolderPath('Desktop')
    $backupDir = Join-Path $desktop ("hermes-backup-" + (Get-Date -Format 'yyyyMMdd-HHmmss'))

    $keepPatterns = @('*.json','*.env','*.yaml','*.yml','*.db','*.sqlite','*.sqlite3','*.log','*.md')
    $keepFiles = @()
    foreach ($r in $Roots) {
        foreach ($pat in $keepPatterns) {
            $keepFiles += Get-ChildItem -LiteralPath $r -Recurse -Force -File -Filter $pat -ErrorAction SilentlyContinue |
                          Where-Object { $_.FullName -notmatch 'node_modules' -and $_.Length -lt 20MB }
        }
    }
    Info ("  백업 대상 파일: {0}개 → {1}" -f $keepFiles.Count, $backupDir)
    if (-not $dry -and $keepFiles.Count -gt 0) {
        New-Item -ItemType Directory -Path $backupDir -Force | Out-Null
        foreach ($f in ($keepFiles | Select-Object -Unique)) {
            $rel = $f.FullName -replace '^[A-Za-z]:[\\/]', ''
            $dst = Join-Path $backupDir $rel
            New-Item -ItemType Directory -Path (Split-Path $dst -Parent) -Force | Out-Null
            Copy-Item -LiteralPath $f.FullName -Destination $dst -Force -ErrorAction SilentlyContinue
        }
        Ok "  → 백업 완료: $backupDir"
    }

    foreach ($r in $Roots) {
        # logs 는 원인 추적용으로 남긴다
        $children = Get-ChildItem -LiteralPath $r -Force -ErrorAction SilentlyContinue |
                    Where-Object { $_.Name -ne 'logs' }
        foreach ($c in $children) {
            Info ("  제거: " + $c.FullName)
            if (-not $dry) {
                if ($c.PSIsContainer) { Remove-Tree $c.FullName | Out-Null }
                else { Remove-Item -LiteralPath $c.FullName -Force -ErrorAction SilentlyContinue }
            }
        }
    }
    Warn '  logs 폴더는 원인 추적을 위해 남겨 두었습니다.'
}

# ------------------------------------------------------------ 5. npm 캐시
Head '5. npm 캐시 정리'
if ($SkipCacheClean) {
    Info '  -SkipCacheClean 지정으로 건너뜀'
} elseif ($dry) {
    Info '  실행 예정: npm cache clean --force'
} else {
    try { & npm cache clean --force 2>&1 | Out-Null; Ok '  → 완료' }
    catch { Warn "  → 실패(npm 미설치?): $_" }
}

# ------------------------------------------------------------ 마무리
Head '마무리'
if ($dry) {
    Warn '지금은 미리보기라 아무것도 지우지 않았습니다.'
    Warn '실제로 정리하려면 -Force 를 붙여 다시 실행하세요:'
    Warn "  powershell -ExecutionPolicy Bypass -File `"$PSCommandPath`" -Mode $Mode -Force"
} else {
    Ok '정리 완료. 이제 다음 중 하나를 하세요:'
    Ok '  1) Hermes 설치 창의 [Retry install] 클릭'
    Ok '  2) 창을 닫고 인스톨러를 다시 실행(가능하면 관리자 권한으로)'
    Ok '  3) 또 실패하면 hermes-install-diagnose.ps1 로 새 로그를 다시 진단'
}
