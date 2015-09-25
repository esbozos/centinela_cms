# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('centinela', '0002_auto_20150922_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=250, verbose_name='image', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 25, 0, 20, 40, 813272, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 25, 0, 20, 40, 814438, tzinfo=utc)),
        ),
    ]
