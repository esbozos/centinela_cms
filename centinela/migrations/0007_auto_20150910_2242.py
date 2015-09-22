# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('centinela', '0006_auto_20150909_0218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='name', max_length=50)),
                ('status', models.BooleanField(verbose_name='status', default=False)),
                ('file', models.FileField(verbose_name='file', upload_to='/static/bootstrap/css/')),
                ('created_date', models.DateTimeField(verbose_name='created', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'theme',
                'verbose_name_plural': 'themes',
            },
        ),
        migrations.AlterField(
            model_name='slider',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 11, 3, 12, 19, 395113, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 11, 3, 12, 19, 396346, tzinfo=utc)),
        ),
    ]
