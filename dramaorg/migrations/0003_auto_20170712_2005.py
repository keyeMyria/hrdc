# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dramaorg', '0002_user_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Phone Number'),
        ),
    ]