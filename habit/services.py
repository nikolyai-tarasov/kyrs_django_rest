from config import settings
import requests

import json
from datetime import datetime, timedelta

from django_celery_beat.models import PeriodicTask, IntervalSchedule


def send_telegram_message(chat_id, message):
    """Функция отправки сообщения в телеграм"""
    params = {
        "text": message,
        "chat_id": chat_id,
    }

    requests.get(
        f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage", params=params
    )


def create_periodic_task(**kwargs):
    """Создает периодическую задачу"""

    schedule, created = IntervalSchedule.objects.get_or_create(
        every=10,
        period=IntervalSchedule.SECONDS,
    )

    PeriodicTask.objects.create(
        interval=schedule,
        name="Importing contacts",
        task="proj.tasks.import_contacts",
        args=json.dumps(["arg1", "arg2"]),
        kwargs=json.dumps(
            {
                "be_careful": True,
            }
        ),
        expires=datetime.utcnow() + timedelta(seconds=30),
    )

    name = kwargs.get("name")
    task = kwargs.get("task")
    schedule = kwargs.get("schedule")
    kwargs = kwargs.get("kwargs", {})
    expires = kwargs.get("expires")

    periodic_task, created = PeriodicTask.objects.get_or_create(
        name=name,
        task=task,
        interval=schedule,
        kwargs=kwargs,
    )

    if created:
        periodic_task.expires = expires
        periodic_task.save()

    return periodic_task
