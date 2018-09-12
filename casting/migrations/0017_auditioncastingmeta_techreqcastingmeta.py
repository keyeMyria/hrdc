# Generated by Django 2.1 on 2018-09-12 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casting', '0016_character_allow_multiple_signatures'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditionCastingMeta',
            fields=[
            ],
            options={
                'verbose_name': 'Casting-Enabled Show - Audition Info',
                'verbose_name_plural': 'Casting-Enabled Shows - Audition Info',
                'proxy': True,
                'indexes': [],
            },
            bases=('casting.castingmeta',),
        ),
        migrations.CreateModel(
            name='TechReqCastingMeta',
            fields=[
            ],
            options={
                'verbose_name': 'Casting-Enabled Show - Tech Req Info',
                'verbose_name_plural': 'Casting-Enabled Shows - Tech Req Info',
                'proxy': True,
                'indexes': [],
            },
            bases=('casting.castingmeta',),
        ),
    ]
