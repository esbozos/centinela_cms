# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('centinela', '0010_auto_20150912_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='location',
            field=models.CharField(verbose_name='location', max_length=20, default='home', choices=[('home', 'Home Page'), ('news', 'News Section')]),
        ),
        migrations.AlterField(
            model_name='slider',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 13, 1, 41, 28, 871749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 13, 1, 41, 28, 872790, tzinfo=utc)),
        ),
    ]
