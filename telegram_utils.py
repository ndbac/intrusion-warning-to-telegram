import telegram
import asyncio

async def send_telegram(photo_path):
    try:
        my_token = "6049425201:AAGaQ66LrqliNzeRsJ9S8PzfqJC3yHQOD4I"
        bot = telegram.Bot(token=my_token)
        await bot.send_photo(chat_id="-4226602153", photo=open(photo_path, "rb"), caption="New intrusion, please check immediately!")
        print("Send success")
    except Exception as ex:
        print("Can not send message telegram ", ex)

def send_telegram_thread(photo_path):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(send_telegram(photo_path))
    loop.close()
