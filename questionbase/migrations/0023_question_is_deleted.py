# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionbase', '0022_auto_20171030_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Вопрос удален'),
        ),
    ]
