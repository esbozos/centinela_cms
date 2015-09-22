# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('centinela', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='menu_order',
            field=models.IntegerField(default=10, verbose_name='menu_order'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='until_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 9, 6, 17, 33, 343428, tzinfo=utc), verbose_name='until'),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='until_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 9, 6, 17, 33, 344392, tzinfo=utc), verbose_name='until'),
        ),
    ]
