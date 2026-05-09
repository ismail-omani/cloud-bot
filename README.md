# cloud-bot
Source code of https://t.me/ismail_cloud_bot

Better works on Linux

Installation:
You need python3, git and curl installed. Windows installer is not updated, use WSL

```bash
curl -O  https://raw.githubusercontent.com/ismail-omani/cloud-bot/main/install.sh  #for everything

chmod +x install.sh && ./install.sh  #for linux

./install.ps1   #for windows, but not recommended
```

If you are in Russia or Telegram is banned in your country, I'd recommend you to configure TOR.
Here is instruction, how to install and use tor on PC with Linux and apt package manager: https://habr.com/ru/articles/797847/. Make sure that tor is running. File config.py is already configured to use TOR. Comment strings

```python
from aiogram.client.session.aiohttp import AiohttpSession
PROXY_URL = "socks5://127.0.0.1:9050"
session = AiohttpSession(proxy=PROXY_URL)
```
and remove
```python
, session=session
```
from
```python
bot = Bot(token=API_TOKEN, session=session)
```
if you don't need TOR.

If something stuck, press enter.

To run bot, run
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
To update bot run:
```bash
cd cloud-bot
./botupd
```

If you ran bot on your server, you will find all uploded files in cloud-bot/files/id, where id is your Telegram id. You can see it in bot using command 
```Telegram
/id
```

For all questions contact me: https://t.me/osint_nigeria
