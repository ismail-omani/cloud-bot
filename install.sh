#!/bin/bash

git clone https://github.com/ismail-omani/cloud-bot.git
cd cloud-bot
python -m venv venv
source venv/bin/activate
pip install aiogram asyncio aiohttp-socks
git update-index --skip-worktree users.txt
git update-index --skip-worktree output.log
git update-index --skip-worktree bot.pid
git ls-files files/ | xargs git update-index --skip-worktree
git ls-files -v | grep ^S

read -p "Your bot token: " token
sed -i "s/YOUR_TOKEN/$token/g" bot.py

nohup python3 bot.py > output.log 2>&1 & echo $! > bot.pid
echo Installation complete. Send /start to your bot
