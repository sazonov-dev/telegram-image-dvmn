import telegram
import os

from dotenv import load_dotenv
load_dotenv()
telegram_bot_token = os.environ['TG_BOT_TOKEN']

bot = telegram.Bot(token=telegram_bot_token)
bot.send_message(chat_id='@dvmn_image_channel_test', text="I'm sorry Dave I'm afraid I can't do that.")
bot.send_photo(chat_id='@dvmn_image_channel_test', photo=open('../images/epic_0.png', 'rb'))


print(bot.get_me())