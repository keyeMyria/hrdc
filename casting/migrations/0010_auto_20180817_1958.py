# Generated by Django 2.1 on 2018-08-17 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casting', '0009_auto_20180129_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='cast_description',
            field=models.TextField(blank=True, help_text='Additional information for actors about this character.', verbose_name='Character Details'),
        ),
        migrations.AlterField(
            model_name='audition',
            name='status',
            field=models.CharField(choices=[('waiting', 'Waiting'), ('called', 'Fetched'), ('done', 'Auditioned')], default='waiting', max_length=20),
        ),
    ]
