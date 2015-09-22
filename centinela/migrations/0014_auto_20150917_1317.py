# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('centinela', '0013_auto_20150917_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=100, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='until_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 17, 17, 47, 45, 51992, tzinfo=utc), verbose_name='until'),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='until_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 17, 17, 47, 45, 53862, tzinfo=utc), verbose_name='until'),
        ),
    ]
