# Generated by Django 2.1 on 2018-08-19 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dramaorg', '0007_user_gender_pref'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='suspended_until',
            field=models.DateField(blank=True, null=True),
        ),
    ]
