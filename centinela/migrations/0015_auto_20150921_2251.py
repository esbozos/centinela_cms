# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('centinela', '0014_auto_20150917_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='until_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 22, 3, 21, 39, 35244, tzinfo=utc), verbose_name='until'),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='until_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 22, 3, 21, 39, 36282, tzinfo=utc), verbose_name='until'),
        ),
    ]
