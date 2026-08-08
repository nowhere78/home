#Requires -Version 5.1
<#
.SYNOPSIS
    Hermes 설치를 막는 npm EBADENGINE 문제를 자동으로 진단·수정한다.

.DESCRIPTION
    Hermes(hermes-agent@1.0.0)의 engine 요구사항:
        node: >=22.22.0
        npm : <11.10.0 || >=11.17.0      ← 11.10.0~11.16.x 구간이 금지됨

    설치된 node/npm 을 읽어 어느 쪽이 어긋났는지 판정하고,
    npm 이 문제면 현재 Node 로 설치 가능한 최신 npm(11.19.0)을 설치한다.

    npm@latest 를 쓰지 않는 이유: latest(12.x)는 node ^24.15.0 이상을 요구해서
    Node 24.14.1 같은 환경에서 도리어 EBADENGINE 으로 실패한다.
    npm 11.19.0 은 engines 가 ">=22.9.0" 이라 Hermes 조건을 만족하는 모든 Node 에서 설치된다.

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .\scripts\hermes-fix-npm.ps1
    powershell -ExecutionPolicy Bypass -File .\scripts\hermes-fix-npm.ps1 -WhatIfOnly
#>
[CmdletBinding()]
param(
    # 실제로 설치하지 않고 판정 결과만 보고 싶을 때
    [switch]$WhatIfOnly
)

$ErrorActionPreference = 'Continue'

# --- Hermes 요구사항 (hermes-agent package.json engines) ---
$HermesNodeMin = [version]'22.22.0'
$NpmBadLow     = [version]'11.10.0'   # 이상
$NpmBadHigh    = [version]'11.17.0'   # 미만  → [11.10.0, 11.17.0) 구간이 금지
$NpmTarget     = '11.19.0'            # 설치할 npm (11.x 최신)
$NpmTargetNode = [version]'22.9.0'    # npm 11.19.0 이 요구하는 최소 Node

function Info { param($m) Write-Host $m -ForegroundColor Gray }
function Warn { param($m) Write-Host $m -ForegroundColor Yellow }
function Ok   { param($m) Write-Host $m -ForegroundColor Green }
function Bad  { param($m) Write-Host $m -ForegroundColor Red }
function Head { param($m) Write-Host ''; Write-Host "== $m" -ForegroundColor Cyan }

function ConvertTo-Ver {
    # "v24.14.1" / "12.0.2-beta.1" → [version]
    param([string]$Raw)
    if (-not $Raw) { return $null }
    $t = ($Raw.Trim() -replace '^v', '')
    $t = ($t -split '[-+]')[0]
    try { return [version]$t } catch { return $null }
}

Write-Host 'Hermes npm 버전 문제 진단·수정' -ForegroundColor White

# ------------------------------------------------------------ 1. 현재 버전
Head '1. 현재 설치된 버전'

$nodeRaw = $null; $npmRaw = $null
try { $nodeRaw = (& node -v 2>&1 | Select-Object -First 1) } catch { }
try { $npmRaw  = (& npm  -v 2>&1 | Select-Object -First 1) } catch { }

$node = ConvertTo-Ver $nodeRaw
$npm  = ConvertTo-Ver $npmRaw

if (-not $node) {
    Bad 'Node.js 를 찾을 수 없습니다. 먼저 Node.js 를 설치하세요.'
    Warn '  winget install OpenJS.NodeJS.LTS'
    Warn '  또는 https://nodejs.org 에서 LTS 설치 후 PowerShell 을 새로 열고 다시 실행하세요.'
    return
}
if (-not $npm) {
    Bad 'npm 을 찾을 수 없습니다. Node.js 를 다시 설치하면 함께 설치됩니다.'
    return
}

Info ("  node : {0}" -f $node)
Info ("  npm  : {0}" -f $npm)

# ------------------------------------------------------------ 2. 판정
Head '2. Hermes 요구사항 대조'
Info ("  요구  node >= {0}" -f $HermesNodeMin)
Info ("  요구  npm  <  {0}  또는  >= {1}" -f $NpmBadLow, $NpmBadHigh)

$nodeOk = ($node -ge $HermesNodeMin)
$npmOk  = ($npm -lt $NpmBadLow) -or ($npm -ge $NpmBadHigh)

if ($nodeOk) { Ok  ("  node {0} → 통과" -f $node) }
else         { Bad ("  node {0} → 미달 (>= {1} 필요)" -f $node, $HermesNodeMin) }

if ($npmOk) { Ok  ("  npm  {0} → 통과" -f $npm) }
else        { Bad ("  npm  {0} → 금지 구간 [{1}, {2}) 에 걸림" -f $npm, $NpmBadLow, $NpmBadHigh) }

# ------------------------------------------------------------ 3. 조치
Head '3. 조치'

if ($nodeOk -and $npmOk) {
    Ok '두 버전 모두 조건을 만족합니다. EBADENGINE 은 원인이 아닙니다.'
    Warn '설치가 계속 실패한다면 다른 원인이니 진단 스크립트를 돌리세요:'
    Warn '  .\scripts\hermes-install-diagnose.ps1'
    return
}

if (-not $nodeOk) {
    Bad ("Node 가 너무 낮습니다({0}). Node 부터 올려야 합니다." -f $node)
    Warn '  winget install OpenJS.NodeJS.LTS'
    Warn '  또는 https://nodejs.org 에서 LTS 설치'
    Warn 'Node 설치 후 PowerShell 을 새로 열고 이 스크립트를 다시 실행하세요.'
    Warn '(새 Node 에 딸려오는 npm 이 다시 금지 구간일 수 있어 재확인이 필요합니다.)'
    return
}

# 여기부터는 node 는 OK, npm 만 문제인 경우
if ($node -lt $NpmTargetNode) {
    Bad ("npm {0} 은(는) Node >= {1} 을 요구하는데 현재 Node 가 {2} 입니다." -f $NpmTarget, $NpmTargetNode, $node)
    Warn 'Node 를 먼저 올리세요.'
    return
}

$isAdmin = ([Security.Principal.WindowsPrincipal] `
            [Security.Principal.WindowsIdentity]::GetCurrent()
           ).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Warn '관리자 권한이 아닙니다. 권한 오류(EACCES/EPERM)가 나면'
    Warn 'PowerShell 을 "관리자 권한으로 실행"해서 다시 시도하세요.'
}

Info ("실행할 명령: npm install -g npm@{0}" -f $NpmTarget)
if ($WhatIfOnly) {
    Warn '-WhatIfOnly 지정으로 실제 설치는 하지 않았습니다.'
    return
}

Write-Host ''
& npm install -g "npm@$NpmTarget"
$exit = $LASTEXITCODE

Head '4. 결과 확인'
$npmAfter = ConvertTo-Ver (& npm -v 2>&1 | Select-Object -First 1)
Info ("  npm : {0}" -f $npmAfter)

if ($npmAfter -and (($npmAfter -lt $NpmBadLow) -or ($npmAfter -ge $NpmBadHigh))) {
    Ok '수정 완료. Hermes 창의 [Retry install] 을 누르세요.'
} else {
    Bad ("아직 조건을 만족하지 않습니다 (npm install 종료 코드 {0})." -f $exit)
    Warn 'PowerShell 을 닫고 새로 연 뒤 npm -v 를 다시 확인해 보세요(반영이 늦는 경우가 있습니다).'
    Warn '그래도 그대로면 반대쪽 구간으로 내려도 됩니다:  npm install -g npm@11.9.0'
}
