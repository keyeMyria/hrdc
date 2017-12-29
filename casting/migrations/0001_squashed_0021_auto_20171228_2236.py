# Generated by Django 2.0 on 2017-12-29 03:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dramaorg', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CastingMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('callback_description', models.TextField(blank=True)),
                ('cast_list_description', models.TextField(blank=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Audition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signed_in', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('waiting', 'Waiting'), ('called', 'Called'), ('done', 'Auditioned')], default='waiting', max_length=20)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casting.CastingMeta')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Callback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CastingReleaseMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_callbacks', models.DateTimeField(blank=True, null=True)),
                ('publish_casts', models.DateTimeField(blank=True, null=True)),
                ('signing_opens', models.DateTimeField(blank=True, null=True)),
                ('second_signing_opens', models.DateTimeField(blank=True, null=True)),
                ('stage', models.PositiveSmallIntegerField(choices=[(0, 'Auditions'), (1, 'Callback Lists Released'), (2, 'First-Round Casting Released'), (3, 'Cast Lists Released'), (4, 'Signing Open'), (5, 'Alternate Signing Open')], default=0)),
                ('publish_first_round_casts', models.DateTimeField(blank=True, null=True)),
                ('prevent_advancement', models.BooleanField(default=False, help_text='If this is set, the stage will not advance until it is cleared again, regardless of set times.')),
            ],
            options={
                'verbose_name': 'Casting Release Group',
                'verbose_name_plural': 'Casting Release Settings',
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Character Name')),
                ('callback_description', models.TextField(blank=True, help_text='Extra information about callbacks for this character.', verbose_name='Character Callback Information')),
                ('allowed_signers', models.PositiveSmallIntegerField(default=1)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casting.CastingMeta')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField(choices=[('Common Times', ((datetime.time(18, 0), '06:00 PM'), (datetime.time(21, 0), '09:00 PM'), (datetime.time(23, 30), '11:30 PM'), (datetime.time(23, 59, 59), '11:59 PM'), (datetime.time(11, 0), '11:00 AM'), (datetime.time(19, 0), '07:00 PM'), (datetime.time(0, 0), '12:00 AM'))), ('All Times', ((datetime.time(9, 0), '09:00 AM'), (datetime.time(9, 30), '09:30 AM'), (datetime.time(10, 0), '10:00 AM'), (datetime.time(10, 30), '10:30 AM'), (datetime.time(11, 0), '11:00 AM'), (datetime.time(11, 30), '11:30 AM'), (datetime.time(12, 0), '12:00 PM'), (datetime.time(12, 30), '12:30 PM'), (datetime.time(13, 0), '01:00 PM'), (datetime.time(13, 30), '01:30 PM'), (datetime.time(14, 0), '02:00 PM'), (datetime.time(14, 30), '02:30 PM'), (datetime.time(15, 0), '03:00 PM'), (datetime.time(15, 30), '03:30 PM'), (datetime.time(16, 0), '04:00 PM'), (datetime.time(16, 30), '04:30 PM'), (datetime.time(17, 0), '05:00 PM'), (datetime.time(17, 30), '05:30 PM'), (datetime.time(18, 0), '06:00 PM'), (datetime.time(18, 30), '06:30 PM'), (datetime.time(19, 0), '07:00 PM'), (datetime.time(19, 30), '07:30 PM'), (datetime.time(20, 0), '08:00 PM'), (datetime.time(20, 30), '08:30 PM'), (datetime.time(21, 0), '09:00 PM'), (datetime.time(21, 30), '09:30 PM'), (datetime.time(22, 0), '10:00 PM'), (datetime.time(22, 30), '10:30 PM'), (datetime.time(23, 0), '11:00 PM'), (datetime.time(23, 30), '11:30 PM')))])),
                ('end', models.TimeField(choices=[('Common Times', ((datetime.time(18, 0), '06:00 PM'), (datetime.time(21, 0), '09:00 PM'), (datetime.time(23, 30), '11:30 PM'), (datetime.time(23, 59, 59), '11:59 PM'), (datetime.time(11, 0), '11:00 AM'), (datetime.time(19, 0), '07:00 PM'), (datetime.time(0, 0), '12:00 AM'))), ('All Times', ((datetime.time(9, 0), '09:00 AM'), (datetime.time(9, 30), '09:30 AM'), (datetime.time(10, 0), '10:00 AM'), (datetime.time(10, 30), '10:30 AM'), (datetime.time(11, 0), '11:00 AM'), (datetime.time(11, 30), '11:30 AM'), (datetime.time(12, 0), '12:00 PM'), (datetime.time(12, 30), '12:30 PM'), (datetime.time(13, 0), '01:00 PM'), (datetime.time(13, 30), '01:30 PM'), (datetime.time(14, 0), '02:00 PM'), (datetime.time(14, 30), '02:30 PM'), (datetime.time(15, 0), '03:00 PM'), (datetime.time(15, 30), '03:30 PM'), (datetime.time(16, 0), '04:00 PM'), (datetime.time(16, 30), '04:30 PM'), (datetime.time(17, 0), '05:00 PM'), (datetime.time(17, 30), '05:30 PM'), (datetime.time(18, 0), '06:00 PM'), (datetime.time(18, 30), '06:30 PM'), (datetime.time(19, 0), '07:00 PM'), (datetime.time(19, 30), '07:30 PM'), (datetime.time(20, 0), '08:00 PM'), (datetime.time(20, 30), '08:30 PM'), (datetime.time(21, 0), '09:00 PM'), (datetime.time(21, 30), '09:30 PM'), (datetime.time(22, 0), '10:00 PM'), (datetime.time(22, 30), '10:30 PM'), (datetime.time(23, 0), '11:00 PM'), (datetime.time(23, 30), '11:30 PM')))])),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casting.CastingMeta')),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dramaorg.Space')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Audition'), (1, 'Callback')], default=0)),
                ('day', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='castingmeta',
            name='release_meta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casting.CastingReleaseMeta', verbose_name='Casting Release Settings'),
        ),
        migrations.AddField(
            model_name='castingmeta',
            name='show',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='casting_meta', to='dramaorg.Show'),
        ),
        migrations.AddField(
            model_name='callback',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casting.Character'),
        ),
        migrations.AlterModelOptions(
            name='castingmeta',
            options={'verbose_name': 'Casting Information', 'verbose_name_plural': 'Casting Information'},
        ),
        migrations.AddField(
            model_name='audition',
            name='space',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dramaorg.Space'),
        ),
        migrations.AddField(
            model_name='castingmeta',
            name='callbacks_submitted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='castingmeta',
            name='cast_submitted',
            field=models.BooleanField(default=False, verbose_name='Full Cast List Submitted'),
        ),
        migrations.AddField(
            model_name='castingmeta',
            name='first_cast_submitted',
            field=models.BooleanField(default=False, verbose_name='First-round Cast List Submitted'),
        ),
        migrations.AlterField(
            model_name='castingmeta',
            name='callback_description',
            field=models.TextField(blank=True, help_text='Extra information about all callbacks (location, etc).', verbose_name='Callback Information'),
        ),
        migrations.AlterField(
            model_name='callback',
            name='actor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='castingmeta',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Show Contact Email'),
        ),
        migrations.AlterField(
            model_name='castingmeta',
            name='cast_list_description',
            field=models.TextField(blank=True, help_text='Extra information to display with the cast list.', verbose_name='Cast List Information'),
        ),
        migrations.CreateModel(
            name='Signing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('response', models.NullBooleanField(choices=[(True, 'Accept this Role'), (False, 'Reject this Role'), (None, 'No Response')])),
                ('actor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casting.Character')),
                ('timed_out', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('character__show', 'character', 'order'),
            },
        ),
        migrations.AddField(
            model_name='character',
            name='added_for_signing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='allowed_signers',
            field=models.PositiveSmallIntegerField(default=1, help_text='Number of actors allowed to sign, can be increased to cast ensemble roles.'),
        ),
        migrations.AlterField(
            model_name='character',
            name='allowed_signers',
            field=models.PositiveSmallIntegerField(default=1, help_text='Number of actors allowed to sign for this character.'),
        ),
        migrations.AlterModelOptions(
            name='castingmeta',
            options={'verbose_name': 'Casting-Enabled Show'},
        ),
        migrations.AlterField(
            model_name='castingmeta',
            name='release_meta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casting.CastingReleaseMeta', verbose_name='Casting Release Group'),
        ),
    ]
