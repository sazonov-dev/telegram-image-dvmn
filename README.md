<h1>Автоматизированный Telegram-канал с красивыми фото галактик и планет.</h1>

- Первым шагом необходимо установить все модули для использования проекта.
- ```pip install -r requirements.txt```
- Вторым шагом необходимо взять API токен на сайте - https://api.nasa.gov/
- Третьим шагом необходимо создать Telegram бота и взять его API токен - https://t.me/BotFather
- - Необходимо создать Telegram канал и добавить туда созданного Telegram бота администратором.
- Четвертым шагом необходимо создать .env файл в главной директории проекта.
- Пятым шагом необходимо создать папку images в главной директории проекта.
- Последним шагом необходимо загрузить картинки в папку images, это можно сделать с помощью запуска скрипта указава args:
- Если не указать ID, то скрипт запросит информацию о последнем SpaceX запуске, но у нее может не быть фотографии
- ```python3 main.py какой-то ID```

<h2>Настройка .env окружения</h2>

- NASA_API_TOKEN=здесь API токен с сайта https://api.nasa.gov/
- TG_BOT_TOKEN=здесь API токен от https://t.me/BotFather
- TG_CHAT_ID=здесь username телеграм канала
- COUNT_OF_UPLOAD=кол-во загрузок
- HOUR_OF_UPLOAD=в какой промежуток времени выкладывать фото