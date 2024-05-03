import telegram
import asyncio
import os

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

async def send_telegram(photo_path):
    try:
        bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
        await bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(photo_path, "rb"), caption="New intrusion, please check immediately!")
        print("Send success")
    except Exception as ex:
        print("Cannot send message to telegram ", ex)

def send_telegram_thread(photo_path):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(send_telegram(photo_path))
    loop.close()
