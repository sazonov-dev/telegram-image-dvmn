import os
import random
import time
import glob
import telegram
import argparse
from dotenv import load_dotenv

from fetch_spacex_images import fetch_spacex_image

def main():
    load_dotenv()
    parser = argparse.ArgumentParser(argument_default=None)
    parser.add_argument('id', nargs='*')
    args = parser.parse_args()
    fetch_spacex_image(args.id)
    telegram_bot_token = os.environ['TG_BOT_TOKEN']
    telegram_chat_id = os.environ['TG_CHAT_ID']
    bot = telegram.Bot(token=telegram_bot_token)

    uploads = 0
    while True:
        count_upload = int(os.environ['COUNT_OF_UPLOAD'])
        hour_upload = int(os.environ['HOUR_OF_UPLOAD'])
        images = glob.glob("./images/*")
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
            with open(random_image, 'rb') as photo_file:
                bot.send_photo(chat_id=telegram_chat_id, photo=photo_file)
            uploads += 1

if __name__ == '__main__':
    main()
