# Generated by Django 3.2.10 on 2022-01-03 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_emailverifyrecord_send_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 3, 23, 36, 18, 612573), verbose_name='发送时间'),
        ),
    ]
