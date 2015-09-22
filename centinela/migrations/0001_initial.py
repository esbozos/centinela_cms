# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.utils.timezone
from django.utils.timezone import utc
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='name', max_length=250)),
                ('slug', models.CharField(verbose_name='slug', max_length=250)),
                ('menu_type', models.CharField(choices=[('none', 'None'), ('main', 'Main Menu'), ('news', 'News Section')], verbose_name='menu type', max_length=10, default='none')),
                ('menu_order', models.IntegerField(verbose_name='menu_order', default=0)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='content')),
                ('created_date', models.DateTimeField(verbose_name='created', default=django.utils.timezone.now)),
                ('author', models.CharField(verbose_name='author', max_length=250)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('spam', 'Spam')], verbose_name='status', max_length=20, default='pending')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.CharField(max_length=20)),
                ('value', models.TextField()),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(verbose_name='author', max_length=250)),
                ('content', ckeditor.fields.RichTextField(verbose_name='content')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish'), ('trash', 'Trash')], verbose_name='status', max_length=20, default='draft')),
                ('title', models.CharField(verbose_name='title', max_length=250)),
                ('type', models.CharField(choices=[('page', 'Page'), ('post', 'Post')], verbose_name='type', max_length=20, default='post')),
                ('mime_type', models.CharField(null=True, verbose_name='mime_type', max_length=30)),
                ('slug', models.SlugField(verbose_name='slug', max_length=100)),
                ('menu_order', models.IntegerField(verbose_name='Menu Position', default=0)),
                ('created_date', models.DateTimeField(verbose_name='created', default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(verbose_name='updated', default=django.utils.timezone.now)),
                ('comment_status', models.BooleanField(verbose_name='Allow comments?', default=True)),
                ('comment_count', models.IntegerField(verbose_name='comment_count', default=0)),
                ('views_count', models.IntegerField(verbose_name='Views Count', default=0)),
                ('category', models.ForeignKey(to='centinela.Category')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='title', max_length=250)),
                ('image_file', models.ImageField(verbose_name='image', upload_to='sliders')),
                ('created_date', models.DateTimeField(verbose_name='created', default=django.utils.timezone.now)),
                ('link_target', models.CharField(verbose_name='link', blank=True, max_length=500)),
                ('status', models.CharField(choices=[('active', 'Active'), ('Inactive', 'Inactive')], verbose_name='status', max_length=20, default='active')),
                ('content', models.CharField(help_text='Text to show over slider', verbose_name='content', blank=True, max_length=250, default='')),
                ('until_date', models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 8, 6, 58, 28, 12816, tzinfo=utc))),
                ('order', models.IntegerField(verbose_name='order', blank=True, default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('posts', models.ManyToManyField(to='centinela.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Widgets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='title', max_length=250)),
                ('image_file', models.ImageField(verbose_name='Image', blank=True, upload_to='linksImages')),
                ('content', models.TextField(help_text='widget content, if image is set this will be hide', verbose_name='content', blank=True)),
                ('created_date', models.DateTimeField(verbose_name='creado', default=django.utils.timezone.now)),
                ('link_target', models.CharField(verbose_name='link', blank=True, max_length=500)),
                ('status', models.CharField(choices=[('active', 'Active'), ('Inactive', 'Inactive')], verbose_name='status', max_length=20, default=(('active', 'Active'), ('Inactive', 'Inactive')))),
                ('until_date', models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 8, 6, 58, 28, 13812, tzinfo=utc))),
                ('order', models.IntegerField(verbose_name='order', blank=True, default=10)),
            ],
            options={
                'verbose_name': 'widget',
                'verbose_name_plural': 'widgets',
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(to='centinela.Post'),
        ),
    ]
