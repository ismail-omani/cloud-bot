git clone https://github.com/ismail-omani/cloud-bot.git
cd cloud-bot
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install aiogram asyncio aiohttp-socks
git update-index --skip-worktree users.txt
git update-index --skip-worktree output.log
git update-index --skip-worktree bot.pid
git ls-files files/ | ForEach-Object { git update-index --skip-worktree $_ }
git ls-files -v | Select-String "^S"
$token = Read-Host "Your bot token: "
(Get-Content bot.py) -replace "YOUR_TOKEN", $token | Set-Content bot.py
Start-Process -NoNewWindow python -ArgumentList "bot.py" -RedirectStandardOutput output.log -RedirectStandardError output.log
$pid = (Get-Process python | Where-Object {$_.StartTime -eq (Get-Process python | Sort-Object StartTime -Descending | Select-Object -First 1).StartTime}).Id
$pid | Out-File bot.pid
Write-Host "Installation complete. Send /start to your bot"
