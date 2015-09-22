# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('centinela', '0005_auto_20150909_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='until_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 9, 6, 48, 32, 47093, tzinfo=utc), verbose_name='until'),
        ),
        migrations.AlterField(
            model_name='socialshare',
            name='html_code',
            field=models.TextField(blank=True, verbose_name='html code'),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='until_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 9, 6, 48, 32, 48061, tzinfo=utc), verbose_name='until'),
        ),
    ]
