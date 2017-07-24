# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casting', '0015_auto_20170720_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='allowed_signers',
            field=models.PositiveSmallIntegerField(default=1, help_text='Number of actors allowed to sign for this character.'),
        ),
        migrations.AlterField(
            model_name='signing',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='signing',
            name='response',
            field=models.NullBooleanField(choices=[(True, 'Accept this Role'), (False, 'Reject this Role'), (None, 'No Response')]),
        ),
    ]