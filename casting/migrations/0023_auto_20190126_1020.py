# Generated by Django 2.1.5 on 2019-01-26 15:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casting', '0022_auto_20190109_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='end',
            field=models.TimeField(choices=[('Common Times', ((datetime.time(18, 0), '06:00 PM'), (datetime.time(21, 0), '09:00 PM'), (datetime.time(23, 30), '11:30 PM'), (datetime.time(23, 59, 59), '11:59 PM'), (datetime.time(11, 0), '11:00 AM'), (datetime.time(19, 0), '07:00 PM'))), ('All Times', ((datetime.time(9, 0), '09:00 AM'), (datetime.time(9, 30), '09:30 AM'), (datetime.time(10, 0), '10:00 AM'), (datetime.time(10, 30), '10:30 AM'), (datetime.time(11, 0), '11:00 AM'), (datetime.time(11, 30), '11:30 AM'), (datetime.time(12, 0), '12:00 PM'), (datetime.time(12, 30), '12:30 PM'), (datetime.time(13, 0), '01:00 PM'), (datetime.time(13, 30), '01:30 PM'), (datetime.time(14, 0), '02:00 PM'), (datetime.time(14, 30), '02:30 PM'), (datetime.time(15, 0), '03:00 PM'), (datetime.time(15, 30), '03:30 PM'), (datetime.time(16, 0), '04:00 PM'), (datetime.time(16, 30), '04:30 PM'), (datetime.time(17, 0), '05:00 PM'), (datetime.time(17, 30), '05:30 PM'), (datetime.time(18, 0), '06:00 PM'), (datetime.time(18, 30), '06:30 PM'), (datetime.time(19, 0), '07:00 PM'), (datetime.time(19, 30), '07:30 PM'), (datetime.time(20, 0), '08:00 PM'), (datetime.time(20, 30), '08:30 PM'), (datetime.time(21, 0), '09:00 PM'), (datetime.time(21, 30), '09:30 PM'), (datetime.time(22, 0), '10:00 PM'), (datetime.time(22, 30), '10:30 PM'), (datetime.time(23, 0), '11:00 PM'), (datetime.time(23, 30), '11:30 PM')))]),
        ),
    ]
