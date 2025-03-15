from celery import shared_task
from users.models import User
from habit.services import send_telegram_message


@shared_task
def send_information_about_like(email):
    """Отправляет сообщение пользователю о поставленном лайке"""
    message = "Вашей собаке только что поставили лайк"
    user = User.objects.get(email=email)
    if user.tg_chat_id:
        send_telegram_message(user.tg_chat_id, message)
