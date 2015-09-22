# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('centinela', '0011_auto_20150912_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=models.CharField(verbose_name='title', blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='slider',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 13, 3, 9, 8, 305386, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 13, 3, 9, 8, 306462, tzinfo=utc)),
        ),
    ]
