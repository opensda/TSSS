from datetime import datetime

from celery import shared_task
from django.conf import settings
from telebot import TeleBot

from habits.models import Habit

bot = TeleBot(settings.TELEGRAM_BOT_TOKEN, threaded=False)


@shared_task
def send_notifications():
    habits = Habit.objects.all()
    current_time = datetime.now().time()

    for habit in habits:
        if habit.time == current_time:
            if habit.user.user_id:
                bot.send_message(chat_id=habit.user.user_id, text=f'Пришло время привычки: {habit.action}')
