$model = "qwen2.5:14b"
$maxRetries = 20
$retryCount = 0

Write-Host "🚀 [$model] 무한 이어받기 모드를 시작합니다..." -ForegroundColor Cyan

while ($retryCount -lt $maxRetries) {
    Write-Host "🔄 [$($retryCount + 1)/$maxRetries] 다운로드 시도 중..." -ForegroundColor Yellow
    ollama pull $model
    
    # 모델이 리스트에 있는지 확인
    $check = ollama list | Select-String $model
    if ($check) {
        Write-Host "✅ [$model] 다운로드 및 설치 완료!" -ForegroundColor Green
        break
    } else {
        Write-Host "⚠️ 다운로드 중단됨. 5초 후 다시 이어받기를 시작합니다..." -ForegroundColor Red
        $retryCount++
        Start-Sleep -Seconds 5
    }
}
