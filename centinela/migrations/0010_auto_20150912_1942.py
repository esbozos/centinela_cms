# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('centinela', '0009_auto_20150910_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='until_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 13, 0, 12, 33, 462877, tzinfo=utc), verbose_name='until'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='file_name',
            field=models.CharField(max_length=100, verbose_name='file name', help_text='file located in bootstrap/css folder'),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='until_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 13, 0, 12, 33, 463934, tzinfo=utc), verbose_name='until'),
        ),
    ]
