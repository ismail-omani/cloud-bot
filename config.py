from aiogram import *
from aiogram.types import *
from aiogram.enums import ParseMode
from aiogram.filters import *
import asyncio
import os
from aiogram.types.input_file import FSInputFile
import shutil
from aiogram.client.session.aiohttp import AiohttpSession

PROXY_URL = "socks5://127.0.0.1:9050"
session = AiohttpSession(proxy=PROXY_URL)

API_TOKEN = 'YOUR_TOKEN'
bot = Bot(token=API_TOKEN, session=session)
