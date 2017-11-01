from django.db import models
from django.utils import timezone


class Question(models.Model):
    qtext = models.TextField(verbose_name='Вопрос')
    qtextlower = models.TextField(blank=True, verbose_name='Вопрос')
    answer = models.CharField(max_length=500, verbose_name='Ответ')
    answerlower = models.CharField(max_length=500, blank=True, verbose_name='Ответ')
    altanswer = models.CharField(max_length=500, blank=True, verbose_name='Зачет')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    commentlower = models.TextField(blank=True, verbose_name='Комментарий')
    author = models.CharField(max_length=500, verbose_name='Автор')
    source = models.CharField(max_length=2000, blank=True, verbose_name='Источник')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата добавления')
    is_played = models.BooleanField(default=False, verbose_name='Игралось')
    is_bb = models.BooleanField(default=False, verbose_name='ЧЯ')
    qlink1 = models.FileField(upload_to='static/img/question/', blank=True, verbose_name='Файл к вопросу 1')
    qlink2 = models.FileField(upload_to='static/img/question/', blank=True, verbose_name='Файл к вопросу 2')
    qlink3 = models.FileField(upload_to='static/img/question/', blank=True, verbose_name='Файл к вопросу 3')
    alink1 = models.FileField(upload_to='static/img/answer/', blank=True, verbose_name='Файл к ответу 1')
    alink2 = models.FileField(upload_to='static/img/answer/', blank=True, verbose_name='Файл к ответу 2')
    alink3 = models.FileField(upload_to='static/img/answer/', blank=True, verbose_name='Файл к ответу 3')
    q_has_img = models.BooleanField(default=False, verbose_name='Вопрос с картинкой')
    q_has_video = models.BooleanField(default=False, verbose_name='Вопрос с видео')
    q_has_audio = models.BooleanField(default=False, verbose_name='Вопрос с аудио')
    q_has_media = models.BooleanField(default=False, verbose_name='Вопрос с медиа файлом')
    wow = models.CharField(
        max_length=3,
        choices=(
            ('-', '-'),
            ('WOW', 'WOW'),
            ('FOO', 'FOO')
        ),
        default='-',
    )
    is_deleted = models.BooleanField(default=False, verbose_name='Вопрос удален')

    def has_media(self):
        for link in [self.qlink1, self.qlink2, self.qlink3, self.alink1, self.alink2, self.alink3]:
            if len(str(link)) > 0:
                return True
        return False

    def has_img(self):
        for link in [self.qlink1, self.qlink2, self.qlink3, self.alink1, self.alink2, self.alink3]:
            if len(str(link)) > 0:
                ext = str(link).split('.')[-1]
                if ext in ['jpg', 'jpeg', 'bmp']:
                    return True
        return False

    def has_video(self):
        for link in [self.qlink1, self.qlink2, self.qlink3, self.alink1, self.alink2, self.alink3]:
            if len(str(link)) > 0:
                ext = str(link).split('.')[-1]
                if ext in ['amv', 'avi', 'flv', 'mov', 'mp4', 'mpg', 'mpeg', 'ogg', 'vob', 'wmv']:
                    return True
        return False

    def has_audio(self):
        for link in [self.qlink1, self.qlink2, self.qlink3, self.alink1, self.alink2, self.alink3]:
            if len(str(link)) > 0:
                ext = str(link).split('.')[-1]
                if ext in ['mp3']:
                    return True
        return False

    def ext_q_list(self):
        list = []
        linklist = [self.qlink1, self.qlink2, self.qlink3]
        i = 1
        for link in linklist:
            type = 'non'
            if len(str(link)) > 0:
                ext = str(link).split('.')[-1]
                if ext in ['jpg', 'jpeg', 'bmp']:
                    type = 'img'
                elif ext in ['amv', 'avi', 'flv', 'mov', 'mp4', 'mpg', 'mpeg', 'ogg', 'vob', 'wmv']:
                    type = 'video'
                elif ext in ['mp3']:
                    type = 'audio'
                else:
                    type = 'other'
            list.append([link, type, i])
            i = i + 1
        return list

    def ext_a_list(self):
        list = []
        linklist = [self.alink1, self.alink2, self.alink3]
        i = 1
        for link in linklist:
            type = 'non'
            if len(str(link)) > 0:
                ext = str(link).split('.')[-1]
                if ext in ['jpg', 'jpeg', 'bmp']:
                    type = 'img'
                elif ext in ['amv', 'avi', 'flv', 'mov', 'mp4', 'mpg', 'mpeg', 'ogg', 'vob', 'wmv']:
                    type = 'video'
                elif ext in ['mp3']:
                    type = 'audio'
                else:
                    type = 'other'
            list.append([link, type, i])
            i = i + 1
        return list

    def __str__(self):
        return self.qtext
