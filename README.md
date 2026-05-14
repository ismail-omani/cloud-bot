# cloud-bot
Source code of https://t.me/ismail_cloud_bot

Installation (only for Linux):
You need python3, tmux, git and curl installed.

```bash
curl -O  https://raw.githubusercontent.com/ismail-omani/cloud-bot/main/install.sh

chmod +x install.sh && ./install.sh
```
Then you'll see instructions what to do to run bot
 
If you are in Russia or Telegram is banned in your country, I'd recommend you to configure TOR. You can find tutorials in Internet or ask AI
Be sure that tor is running. File bot.py is already configured to use TOR. 

If you don't need TOR, comment strings
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

If something stuck, press enter.

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
