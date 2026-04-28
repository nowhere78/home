Write-Host "--- Starting Unsloth Installation for Alpha Agent ---" -ForegroundColor Cyan
pip install unsloth
pip install --no-deps "xformers<0.0.27" "trl<0.9.0" peft accelerate bitsandbytes
Write-Host "--- Installation Complete ---" -ForegroundColor Green
