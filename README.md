# cloud-bot
Source code of https://t.me/ismail_cloud_bot

Better works on linux

Installation:
You need python3 and git installed.
```bash
./install.sh #for linux

./install.ps1   #for win, but not recommended
```

If you are in Russia or Telegram is banned in your country, I'd recommend you to configure TOR.
Here is instruction, how to install and use tor on PC with Linux and apt package manager: https://habr.com/ru/articles/797847/. Make sure that tor is running. File bot.py is already configured to use TOR. Comment strings
```bash
from aiogram.client.session.aiohttp import AiohttpSession
PROXY_URL = "socks5://127.0.0.1:9050"
session = AiohttpSession(proxy=PROXY_URL)
```
and remove
```bash
, session=session
```
from
```bash
bot = Bot(token=API_TOKEN, session=session)
```
if you don't need TOR.

If something stuck, press enter.
After installing change "YOUR_TOKEN" in "API_TOKEN = 'YOUR_TOKEN'" in bot.py to your bot token, then run 
```bash
python bot.py
```
being in directory cloud-bot.

If you need to run bot in the background on Linux, run
```bash
nohup python3 bot.py > output.log 2>&1 & echo $! > bot.pid
```
You will see PID, it wil be saved to bot.pid. When you will need to kill bot process - run 
```bash
kill $(echo bot.pid)
```

If you ran bot on your server, you will find all uploded files in cloud-bot/files/id, where id is your Telegram id. You can see it in bot using command 
```bash
/id
```
