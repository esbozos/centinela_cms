# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('centinela', '0004_auto_20150909_0155'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='name', max_length=100)),
                ('html_code', models.CharField(verbose_name='html code', blank=True, max_length=500)),
                ('js_code', models.TextField(verbose_name='js code', blank=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('Inactive', 'Inactive')], max_length=20, verbose_name='status', default=(('active', 'Active'), ('Inactive', 'Inactive')))),
                ('order', models.IntegerField(verbose_name='oder', default=10)),
            ],
            options={
                'verbose_name': 'social share',
                'verbose_name_plural': 'social shares',
            },
        ),
        migrations.AlterField(
            model_name='slider',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 9, 6, 47, 34, 471104, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 9, 6, 47, 34, 472079, tzinfo=utc)),
        ),
    ]
