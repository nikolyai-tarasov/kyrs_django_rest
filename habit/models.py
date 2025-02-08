from django.conf import settings
from django.db import models


NULLABLE = {"blank": True, "null": True}


class Habits(models.Model):

    IS_NICE_CHOICES = (
        (True, "Приятная"),
        (False, "Нет"),
    )

    PUBLIC_CHOICES = (
        (True, "Публичная"),
        (False, "Нет"),
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    place = models.CharField(max_length=200, verbose_name="Место")
    time = models.TimeField(verbose_name="Время, когда надо выполнить привычку")
    action = models.CharField(
        max_length=200, verbose_name="Действие, которое надо сделать"
    )
    is_nice = models.BooleanField(
        default=True, verbose_name="Приятная", choices=IS_NICE_CHOICES
    )
    related = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Связанная с другой привычкой",
        **NULLABLE,
    )
    periodicity = models.SmallIntegerField(
        default=1, verbose_name="Периодичность (в днях) - от 1 до 7"
    )
    prize = models.CharField(max_length=100, verbose_name="Вознаграждение", **NULLABLE)
    duration = models.SmallIntegerField(verbose_name="Время на выполнение (в минутах) ")
    is_public = models.BooleanField(
        default=True, verbose_name="Публичная", choices=PUBLIC_CHOICES
    )

    created_at = models.DateTimeField(
        **NULLABLE,
        verbose_name="Дата создания",
        help_text="Укажите дату создания",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        **NULLABLE,
        verbose_name="Дата изменения",
        help_text="Укажите дату изменения",
        auto_now=True,
    )

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ["-id"]
