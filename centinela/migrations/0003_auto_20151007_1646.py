# -*- coding: utf-8 -*-
# rescue
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('centinela', '0002_auto_20151007_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='until_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 6, 21, 16, 46, 444071, tzinfo=utc), verbose_name='until'),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='place',
            field=models.CharField(choices=[('top', 'top'), ('lateral', 'Lateral'), ('after_post', 'After Post'), ('before_post', 'Before Post'), ('footer', 'footer')], verbose_name='Place', max_length=30, default='lateral'),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='until_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 6, 21, 16, 46, 445192, tzinfo=utc), verbose_name='until'),
        ),
    ]
