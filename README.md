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
```
Win:
```bash
mkdir files
mkdir files\shared
.\venv\Scripts\Activate.ps1
pip install aiogram asyncio
```

If something stuck, press enter.
After installing change "YOUR_TOKEN" in "API_TOKEN = 'YOUR_TOKEN'" in bot.py to your bot token, then run 
```bash
python bot.py
```
being in directory cloud-bot
