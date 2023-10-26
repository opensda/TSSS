import requests
from django.conf import settings

TOKEN = settings.TELEGRAM_BOT_TOKEN


def get_updates():
    response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    return response.json()
