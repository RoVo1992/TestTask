from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):

    """Модель наших пользователей"""

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class TicketQueue(models.Model):

    """Модель с очередями тикетов"""
    title = models.CharField(
        max_length=25,
        verbose_name='Состояние'
    )

    class Meta:
        verbose_name = 'Состояние тикета'
        verbose_name_plural = 'Состояния тикетов'

    def __str__(self):
        return self.title


class Ticket(models.Model):

    """Модель тикетов"""
    issue = models.TextField(
        blank=False,
        verbose_name='Проблема',
        editable=False
    )
    time_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    author = models.ForeignKey(
        'AppUser',
        on_delete=models.DO_NOTHING,
        verbose_name='Автор',
        related_name='ticket_author'
    )
    queue = models.ForeignKey(  # В каком состояннии тикет находится
        'TicketQueue',
        on_delete=models.DO_NOTHING,
        verbose_name='Состояние'
    )
    answers = models.ManyToManyField(  # Все сообщения в тикете
        'Messages',
        verbose_name='Ответы'
    )

    class Meta:
        verbose_name = 'Тикет'
        verbose_name_plural = 'Тикеты'

    def __str__(self):
        return self.pk, self.time_created, self.queue


class Messages(models.Model):

    """Ответы пользователей и саппортов"""
    author = models.ForeignKey(
        'AppUser',
        verbose_name='Автор',
        on_delete=models.DO_NOTHING,
        related_name='message_author'
    )
    time_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )
    message = models.TextField(
        blank=False,
        verbose_name='Текст сообщения'
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.pk, self.author, self.time_created
