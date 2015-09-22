# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('centinela', '0002_auto_20150909_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='posts',
        ),
        migrations.AlterField(
            model_name='slider',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 9, 6, 24, 5, 204141, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 9, 6, 24, 5, 205320, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
