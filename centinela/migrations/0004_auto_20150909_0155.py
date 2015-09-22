# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('centinela', '0003_auto_20150909_0154'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Logs',
        ),
        migrations.AlterField(
            model_name='slider',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 9, 6, 25, 12, 108552, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 9, 6, 25, 12, 109595, tzinfo=utc)),
        ),
    ]
