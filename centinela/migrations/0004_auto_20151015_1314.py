# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('centinela', '0003_auto_20151007_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='status',
            field=models.CharField(max_length=20, default='active', choices=[('active', 'Active'), ('inactive', 'Inactive')], verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 11, 14, 17, 44, 0, 503612, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='socialshare',
            name='status',
            field=models.CharField(max_length=20, default=(('active', 'Active'), ('inactive', 'Inactive')), choices=[('active', 'Active'), ('inactive', 'Inactive')], verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='status',
            field=models.CharField(max_length=10, default='active', choices=[('active', 'Active'), ('inactive', 'Inactive')], verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='place',
            field=models.CharField(max_length=30, default='lateral', choices=[('top', 'Top'), ('lateral', 'Lateral'), ('after_post', 'After Post'), ('before_post', 'Before Post'), ('footer', 'Footer')], verbose_name='Place'),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='status',
            field=models.CharField(max_length=20, default=(('active', 'Active'), ('inactive', 'Inactive')), choices=[('active', 'Active'), ('inactive', 'Inactive')], verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='until_date',
            field=models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 11, 14, 17, 44, 0, 504733, tzinfo=utc)),
        ),
    ]
