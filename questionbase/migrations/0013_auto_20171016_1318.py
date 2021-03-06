# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionbase', '0012_auto_20171016_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='alink1',
            field=models.FileField(blank=True, upload_to='img/answer/', verbose_name='Файл к ответу'),
        ),
        migrations.AlterField(
            model_name='question',
            name='alink2',
            field=models.FileField(blank=True, upload_to='img/answer/', verbose_name='Файл к ответу'),
        ),
        migrations.AlterField(
            model_name='question',
            name='alink3',
            field=models.FileField(blank=True, upload_to='img/answer/', verbose_name='Файл к ответу'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qlink1',
            field=models.FileField(blank=True, upload_to='img/question/', verbose_name='Файл к вопросу'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qlink2',
            field=models.FileField(blank=True, upload_to='img/question/', verbose_name='Файл к вопросу'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qlink3',
            field=models.FileField(blank=True, upload_to='img/question/', verbose_name='Файл к вопросу'),
        ),
    ]
