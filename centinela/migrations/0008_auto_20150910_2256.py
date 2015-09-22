# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('centinela', '0007_auto_20150910_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='file',
        ),
        migrations.AddField(
            model_name='theme',
            name='file_name',
            field=models.CharField(verbose_name='file name', max_length=100, default='bootstrap.simplex.min.css'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='slider',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 11, 3, 25, 19, 132481, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 11, 3, 25, 19, 133758, tzinfo=utc)),
        ),
    ]
