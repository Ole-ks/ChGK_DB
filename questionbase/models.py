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

    def ext_q1(self):
        type = 'non'
        ext = str(self.qlink1).split('.')[-1]
        if len(ext) > 0:
            if ext in ['jpg', 'jpeg', 'bmp']:
                type = 'img'
            elif ext in ['amv', 'avi', 'flv', 'mov', 'mp4', 'mpg', 'mpeg', 'ogg', 'vob', 'wmv']:
                type = 'video'
            elif ext in ['mp3']:
                type = 'audio'
            else:
                type = 'other'
        return type

    def ext_q2(self):
        type = 'non'
        ext = str(self.qlink2).split('.')[-1]
        if len(ext) > 0:
            if ext in ['jpg', 'jpeg', 'bmp']:
                type = 'img'
            elif ext in ['amv', 'avi', 'flv', 'mov', 'mp4', 'mpg', 'mpeg', 'ogg', 'vob', 'wmv']:
                type = 'video'
            elif ext in ['mp3']:
                type = 'audio'
            else:
                type = 'other'
        return type

    def ext_q3(self):
        type = 'non'
        ext = str(self.qlink3).split('.')[-1]
        if len(ext) > 0:
            if ext in ['jpg', 'jpeg', 'bmp']:
                type = 'img'
            elif ext in ['amv', 'avi', 'flv', 'mov', 'mp4', 'mpg', 'mpeg', 'ogg', 'vob', 'wmv']:
                type = 'video'
            elif ext in ['mp3']:
                type = 'audio'
            else:
                type = 'other'
        return type

    def ext_a1(self):
        type = 'non'
        ext = str(self.alink1).split('.')[-1]
        if len(ext) > 0:
            if ext in ['jpg', 'jpeg', 'bmp']:
                type = 'img'
            elif ext in ['amv', 'avi', 'flv', 'mov', 'mp4', 'mpg', 'mpeg', 'ogg', 'vob', 'wmv']:
                type = 'video'
            elif ext in ['mp3']:
                type = 'audio'
            else:
                type = 'other'
        return type

    def ext_a2(self):
        type = 'non'
        ext = str(self.alink2).split('.')[-1]
        if len(ext) > 0:
            if ext in ['jpg', 'jpeg', 'bmp']:
                type = 'img'
            elif ext in ['amv', 'avi', 'flv', 'mov', 'mp4', 'mpg', 'mpeg', 'ogg', 'vob', 'wmv']:
                type = 'video'
            elif ext in ['mp3']:
                type = 'audio'
            else:
                type = 'other'
        return type

    def ext_a3(self):
        type = 'non'
        ext = str(self.alink3).split('.')[-1]
        if len(ext) > 0:
            if ext in ['jpg', 'jpeg', 'bmp']:
                type = 'img'
            elif ext in ['amv', 'avi', 'flv', 'mov', 'mp4', 'mpg', 'mpeg', 'ogg', 'vob', 'wmv']:
                type = 'video'
            elif ext in ['mp3']:
                type = 'audio'
            else:
                type = 'other'
        return type