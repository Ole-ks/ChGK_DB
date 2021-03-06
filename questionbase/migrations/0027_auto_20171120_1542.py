# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionbase', '0026_auto_20171116_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blitz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtext1', models.TextField(verbose_name='Вопрос 1')),
                ('qt1xt2', models.TextField(verbose_name='Вопрос 2')),
                ('qtext3', models.TextField(blank=True, verbose_name='Вопрос 3')),
                ('answer1', models.CharField(max_length=500, verbose_name='Ответ 1')),
                ('answer2', models.CharField(max_length=500, verbose_name='Ответ 2')),
                ('answer3', models.CharField(blank=True, max_length=500, verbose_name='Ответ 3')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='is_blitz',
            field=models.BooleanField(default=False, verbose_name='Блиц'),
        ),
        migrations.AddField(
            model_name='blitz',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blitz', to='questionbase.Question'),
        ),
    ]
