### Installation

Download appropriate trained yolo v4 model and put them to `/model` directory to be able to run.

Update the telegram bot token and chat ID in `telegram_utils.py` file with your values.

After that, you could run the following commands to test the intrusion warning system:

```
pip install -r requirements.txt

python main.py
```


Sample environment variables:

```
TELEGRAM_BOT_TOKEN="6049425201:AAGaQ66LrqliNzeRsJ9S8PzfqJC3yHQOD4I"

TELEGRAM_CHAT_ID="-4226602153"
```