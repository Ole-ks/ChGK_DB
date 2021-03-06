# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-23 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionbase', '0030_package_packagedetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagedetail',
            name='pkg_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pkg_detail', to='questionbase.Package'),
        ),
        migrations.AlterField(
            model_name='packagedetail',
            name='quest_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_in_pkg', to='questionbase.Question'),
        ),
    ]
