PROXY_URL = "socks5://127.0.0.1:9050"
session = AiohttpSession(proxy=PROXY_URL)

API_TOKEN = 'YOUR_TOKEN'
bot = Bot(token=API_TOKEN, session=session)
