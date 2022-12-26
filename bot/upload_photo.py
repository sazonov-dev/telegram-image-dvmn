import os
import random
import time
import glob
import telegram

from dotenv import load_dotenv
from PIL import Image
load_dotenv()
telegram_bot_token = os.environ['TG_BOT_TOKEN']

bot = telegram.Bot(token=telegram_bot_token)

def upload():
    uploads = 0
    while True:
        count_upload = int(os.environ['COUNT_OF_UPLOAD'])
        hour_upload = int(os.environ['HOUR_OF_UPLOAD'])
        images = glob.glob("../images/*")
        random_image_index = random.randint(0, len(images) - 1)
        seconds = hour_upload * 60 * 60
        random_image = images[random_image_index]
        file_stat = os.stat(random_image)
        tg_byte_limit = 20971520
        if file_stat.st_size > tg_byte_limit:
            break
        else:
            if uploads >= count_upload:
                uploads = 0
                time.sleep(seconds)
                break
            bot.send_photo(chat_id='@dvmn_image_channel_test', photo=open(random_image, 'rb'))
            uploads += 1

upload()
