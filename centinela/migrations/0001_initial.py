# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
from django.conf import settings
import django.utils.timezone
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('slug', models.CharField(max_length=100, verbose_name='slug')),
                ('menu_type', models.CharField(max_length=10, verbose_name='menu type', default='none', choices=[('none', 'None'), ('main', 'Main Menu'), ('news', 'News Section')])),
                ('menu_order', models.IntegerField(verbose_name='menu_order', default=10)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('content', models.TextField(verbose_name='content')),
                ('created_date', models.DateTimeField(verbose_name='created', default=django.utils.timezone.now)),
                ('author', models.CharField(max_length=250, verbose_name='author')),
                ('status', models.CharField(max_length=20, verbose_name='status', default='pending', choices=[('pending', 'Pending'), ('approved', 'Approved'), ('spam', 'Spam')])),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('content', ckeditor.fields.RichTextField(verbose_name='content')),
                ('status', models.CharField(max_length=20, verbose_name='status', default='draft', choices=[('draft', 'Draft'), ('publish', 'Publish'), ('trash', 'Trash')])),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('type', models.CharField(max_length=20, verbose_name='type', default='post', choices=[('page', 'Page'), ('post', 'Post')])),
                ('mime_type', models.CharField(max_length=30, verbose_name='mime_type', null=True)),
                ('slug', models.SlugField(max_length=100, verbose_name='slug')),
                ('menu_order', models.IntegerField(verbose_name='Menu Position', default=10)),
                ('url_link', models.CharField(max_length=200, verbose_name='url_path', blank=True, null=True)),
                ('created_date', models.DateTimeField(verbose_name='created', default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(verbose_name='updated', default=django.utils.timezone.now)),
                ('comment_status', models.BooleanField(verbose_name='Allow comments?', default=True)),
                ('comment_count', models.IntegerField(verbose_name='comment_count', default=0)),
                ('views_count', models.IntegerField(verbose_name='Views Count', default=0)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=250, verbose_name='title', blank=True)),
                ('image_file', models.ImageField(verbose_name='image', upload_to='sliders')),
                ('created_date', models.DateTimeField(verbose_name='created', default=django.utils.timezone.now)),
                ('link_target', models.CharField(max_length=500, verbose_name='link', blank=True)),
                ('status', models.CharField(max_length=20, verbose_name='status', default='active', choices=[('active', 'Active'), ('Inactive', 'Inactive')])),
                ('content', models.CharField(max_length=250, verbose_name='content', blank=True, default='', help_text='Text to show over slider')),
                ('until_date', models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 22, 5, 47, 8, 666133, tzinfo=utc))),
                ('order', models.IntegerField(verbose_name='order', default=10, blank=True)),
                ('location', models.CharField(max_length=20, verbose_name='location', default='home', choices=[('home', 'Home Page'), ('news', 'News Section')])),
            ],
        ),
        migrations.CreateModel(
            name='SocialShare',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('html_code', models.TextField(verbose_name='html code', blank=True)),
                ('js_code', models.TextField(verbose_name='js code', blank=True)),
                ('status', models.CharField(max_length=20, verbose_name='status', default=(('active', 'Active'), ('Inactive', 'Inactive')), choices=[('active', 'Active'), ('Inactive', 'Inactive')])),
                ('order', models.IntegerField(verbose_name='oder', default=10)),
            ],
            options={
                'verbose_name': 'social share',
                'verbose_name_plural': 'social shares',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('status', models.BooleanField(verbose_name='status', default=False)),
                ('file_name', models.CharField(max_length=100, verbose_name='file name', help_text='file located in bootstrap/css folder')),
                ('created_date', models.DateTimeField(verbose_name='created', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'theme',
                'verbose_name_plural': 'themes',
            },
        ),
        migrations.CreateModel(
            name='Widgets',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('image_file', models.ImageField(verbose_name='Image', blank=True, upload_to='linksImages')),
                ('content', models.TextField(verbose_name='content', blank=True, help_text='widget content, if image is set this will be hide')),
                ('created_date', models.DateTimeField(verbose_name='creado', default=django.utils.timezone.now)),
                ('link_target', models.CharField(max_length=500, verbose_name='link', blank=True)),
                ('status', models.CharField(max_length=20, verbose_name='status', default=(('active', 'Active'), ('Inactive', 'Inactive')), choices=[('active', 'Active'), ('Inactive', 'Inactive')])),
                ('until_date', models.DateTimeField(verbose_name='until', default=datetime.datetime(2015, 10, 22, 5, 47, 8, 667140, tzinfo=utc))),
                ('order', models.IntegerField(verbose_name='order', default=10, blank=True)),
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
