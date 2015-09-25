# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('centinela', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='content',
            field=models.CharField(default='', verbose_name='content', max_length=500, blank=True, help_text='Text to show over slider'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='until_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 22, 16, 5, 52, 231200, tzinfo=utc), verbose_name='until'),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='until_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 22, 16, 5, 52, 232202, tzinfo=utc), verbose_name='until'),
        ),
    ]
