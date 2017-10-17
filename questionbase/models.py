from django.db import models
from django.utils import timezone


class Question(models.Model):
    qtext = models.TextField(verbose_name='Вопрос')
    answer = models.CharField(max_length=500, verbose_name='Ответ')
    altanswer = models.CharField(max_length=500, blank=True, verbose_name='Зачет')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    author = models.CharField(max_length=500, verbose_name='Автор')
    source = models.CharField(max_length=2000, blank=True, verbose_name='Источник')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата добавления')
    is_played = models.BooleanField(verbose_name='Игралось')
    is_bb = models.BooleanField(verbose_name='ЧЯ')
    qlink1 = models.FileField(upload_to='static/img/question/', blank=True, verbose_name='Файл к вопросу')
    qlink2 = models.FileField(upload_to='static/img/question/', blank=True, verbose_name='Файл к вопросу')
    qlink3 = models.FileField(upload_to='static/img/question/', blank=True, verbose_name='Файл к вопросу')
    alink1 = models.FileField(upload_to='static/img/answer/', blank=True, verbose_name='Файл к ответу')
    alink2 = models.FileField(upload_to='static/img/answer/', blank=True, verbose_name='Файл к ответу')
    alink3 = models.FileField(upload_to='static/img/answer/', blank=True, verbose_name='Файл к ответу')

    def __str__(self):
        return self.qtext
