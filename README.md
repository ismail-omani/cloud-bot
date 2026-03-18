# cloud-bot
Source code of https://t.me/ismail_cloud_bot

Better works on linux

Installation:
You need python3 and git installed.
```bash
git clone https://github.com/ismail-omani/cloud-bot.git
```
```bash
cd cloud-bot
```
```bash
python -m venv venv
```
Linux:
```bash
mkdir files && mkdir files/shared
source venv/bin/activate
pip install aiogram asyncio
pip install aiohttp-socks #if you need tor
```
Win:
```bash
mkdir files
mkdir files\shared
.\venv\Scripts\Activate.ps1
pip install aiogram asyncio
pip install aiohttp-socks #if you need tor
```
If you are from Russia or Telegram is banned in your country, I'd recommend you to configure tor.
Here is instruction, how to install and use tor on PC with Linux and apt package manager: https://habr.com/ru/articles/797847/. Make sure that tor is running. File bot.py is already configured to use tor. Comment strings
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
if you don't need tor.

If something stuck, press enter.
After installing change "YOUR_TOKEN" in "API_TOKEN = 'YOUR_TOKEN'" in bot.py to your bot token, then run 
```bash
python bot.py
```
being in directory cloud-bot

If you launched bot on your server, you will find all uploded files in cloud-bot/files/id, where id is your telegram id. You can see it in bot using command 
```bash
/id
```
