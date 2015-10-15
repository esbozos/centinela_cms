# -*- coding: utf-8 -*-
# rescue
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone
from django.utils.timezone import utc
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='name', max_length=250)),
                ('slug', models.CharField(verbose_name='slug', max_length=100)),
                ('menu_type', models.CharField(default='none', verbose_name='menu type', choices=[('none', 'None'), ('main', 'Main Menu'), ('news', 'News Section')], max_length=10)),
                ('menu_order', models.IntegerField(default=10, verbose_name='menu_order')),
            ],
            options={
                'verbose_name_plural': 'categories',
                'verbose_name': 'category',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='content')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created')),
                ('author', models.CharField(verbose_name='author', max_length=250)),
                ('status', models.CharField(default='pending', verbose_name='status', choices=[('pending', 'Pending'), ('approved', 'Approved'), ('spam', 'Spam')], max_length=20)),
            ],
            options={
                'verbose_name_plural': 'comments',
                'verbose_name': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('content', ckeditor.fields.RichTextField(verbose_name='content')),
                ('status', models.CharField(default='draft', verbose_name='status', choices=[('draft', 'Draft'), ('publish', 'Publish'), ('trash', 'Trash')], max_length=20)),
                ('title', models.CharField(verbose_name='title', max_length=250)),
                ('type', models.CharField(default='post', verbose_name='type', choices=[('page', 'Page'), ('post', 'Post')], max_length=20)),
                ('image', models.CharField(blank=True, null=True, verbose_name='image', max_length=250)),
                ('mime_type', models.CharField(null=True, verbose_name='mime_type', max_length=30)),
                ('slug', models.SlugField(verbose_name='slug', max_length=100)),
                ('menu_order', models.IntegerField(default=10, verbose_name='Menu Position')),
                ('url_link', models.CharField(blank=True, null=True, verbose_name='url_path', max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created')),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated')),
                ('comment_status', models.BooleanField(default=True, verbose_name='Allow comments?')),
                ('comment_count', models.IntegerField(default=0, verbose_name='comment_count')),
                ('views_count', models.IntegerField(default=0, verbose_name='Views Count')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(to='centinela.Category')),
            ],
            options={
                'verbose_name_plural': 'posts',
                'verbose_name': 'post',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(blank=True, verbose_name='title', max_length=250)),
                ('image_file', models.ImageField(upload_to='sliders', verbose_name='image')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created')),
                ('link_target', models.CharField(blank=True, verbose_name='link', max_length=500)),
                ('status', models.CharField(default='active', verbose_name='status', choices=[('active', 'Active'), ('Inactive', 'Inactive')], max_length=20)),
                ('content', models.CharField(blank=True, help_text='Text to show over slider', default='', verbose_name='content', max_length=500)),
                ('until_date', models.DateTimeField(default=datetime.datetime(2015, 11, 6, 21, 12, 32, 663912, tzinfo=utc), verbose_name='until')),
                ('order', models.IntegerField(blank=True, default=10, verbose_name='order')),
                ('location', models.CharField(default='home', verbose_name='location', choices=[('home', 'Home Page'), ('news', 'News Section')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SocialShare',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='name', max_length=100)),
                ('html_code', models.TextField(blank=True, verbose_name='html code')),
                ('js_code', models.TextField(blank=True, verbose_name='js code')),
                ('status', models.CharField(default=(('active', 'Active'), ('Inactive', 'Inactive')), verbose_name='status', choices=[('active', 'Active'), ('Inactive', 'Inactive')], max_length=20)),
                ('order', models.IntegerField(default=10, verbose_name='oder')),
            ],
            options={
                'verbose_name_plural': 'social shares',
                'verbose_name': 'social share',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='name', max_length=50)),
                ('status', models.BooleanField(default=False, verbose_name='active')),
                ('file_name', models.CharField(help_text='file located in bootstrap/css folder', verbose_name='file name', max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created')),
            ],
            options={
                'verbose_name_plural': 'themes',
                'verbose_name': 'theme',
            },
        ),
        migrations.CreateModel(
            name='Widgets',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='title', max_length=250)),
                ('image_file', models.ImageField(blank=True, upload_to='linksImages', verbose_name='Image')),
                ('content', models.TextField(blank=True, help_text='widget content, if image is set this will be hide', verbose_name='content')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='creado')),
                ('link_target', models.CharField(blank=True, verbose_name='link', max_length=500)),
                ('status', models.CharField(default=(('active', 'Active'), ('Inactive', 'Inactive')), verbose_name='status', choices=[('active', 'Active'), ('Inactive', 'Inactive')], max_length=20)),
                ('until_date', models.DateTimeField(default=datetime.datetime(2015, 11, 6, 21, 12, 32, 665018, tzinfo=utc), verbose_name='until')),
                ('order', models.IntegerField(blank=True, default=10, verbose_name='order')),
            ],
            options={
                'verbose_name_plural': 'widgets',
                'verbose_name': 'widget',
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(to='centinela.Post'),
        ),
    ]
