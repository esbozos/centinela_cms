# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('centinela', '0012_auto_20150912_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url_link',
            field=models.CharField(verbose_name='url_path', blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='menu_order',
            field=models.IntegerField(verbose_name='Menu Position', default=10),
        ),
        migrations.AlterField(
            model_name='slider',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 17, 17, 11, 21, 821488, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 17, 17, 11, 21, 823173, tzinfo=utc)),
        ),
    ]
