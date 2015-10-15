# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('centinela', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='widgets',
            name='place',
            field=models.CharField(verbose_name='Place', choices=[('top', 'top'), ('lateral', 'Lateral'), ('after_post', 'After Post'), ('before_post', 'Before Post'), ('footer', 'footer')], max_length=30, default='top'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 11, 6, 21, 16, 0, 221260, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 11, 6, 21, 16, 0, 222375, tzinfo=utc)),
        ),
    ]
