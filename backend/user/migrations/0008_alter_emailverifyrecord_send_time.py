<<<<<<< HEAD
# Generated by Django 3.2.10 on 2022-01-03 16:08
=======
# Generated by Django 4.0 on 2022-01-08 14:43
>>>>>>> bb807b22e7e5dbb0ece8ef34acdc486c3b25d636

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_emailverifyrecord_send_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
<<<<<<< HEAD
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 4, 0, 8, 9, 234522), verbose_name='发送时间'),
=======
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 8, 22, 43, 36, 334346), verbose_name='发送时间'),
>>>>>>> bb807b22e7e5dbb0ece8ef34acdc486c3b25d636
        ),
    ]
