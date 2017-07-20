# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casting', '0007_auto_20170715_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='castingreleasemeta',
            name='publish_first_round_casts',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='castingreleasemeta',
            name='stage',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Auditions'), (1, 'Callback Lists Released'), (2, 'First-Round Casting Released'), (3, 'Cast Lists Released')], default=0),
        ),
    ]