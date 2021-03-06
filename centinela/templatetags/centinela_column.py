# -*- coding: utf-8 -*-
from centinela.models import Category, Post, Widgets
from django import template
from django.conf import settings
from django.utils import timezone
import datetime
import os

register = template.Library()


@register.inclusion_tag("centinela/more_posts.html")
def get_more_read():
    om = timezone.now() - datetime.timedelta(days=30)
    more_read = Post.objects.filter(created_date__gt=om).filter(views_count__gt=0).filter(status='publish').order_by('-views_count')[:settings.CENTINELA['MAX_MORE_READ_RESULT']]
    more_recent = Post.objects.filter(status='publish', type='post').order_by('-created_date')[:settings.CENTINELA['MAX_MORE_READ_RESULT']]
    return {'more_read': more_read, 'more_recent': more_recent, 'title': 'Lo más Leido', 'category': 'all'}


@register.inclusion_tag("centinela/lateral_widgets.html")
def get_lateral_widgets():
    now = timezone.now()
    widgets = Widgets.objects.filter(until_date__gt=now).filter(status='active', place='lateral').order_by('order')
    return {'widgets': widgets}

@register.inclusion_tag("centinela/widgets.html")
def get_post_widgets(place):
    now = timezone.now()
    widgets = Widgets.objects.filter(until_date__gt=now).filter(status='active', place=place).order_by('order')
    return {'widgets': widgets}

@register.inclusion_tag("centinela/more_posts.html")
def get_more_in_category(category):
    om = timezone.now() - datetime.timedelta(days=30)
    more_read = Post.objects.filter(created_date__gt=om, views_count__gt=0, category=category, status='publish').order_by('-views_count')[:settings.CENTINELA['MAX_MORE_IN_CATEGORY']]
    more_recent = Post.objects.filter(status='publish', type='post').order_by('-created_date')[:settings.CENTINELA['MAX_MORE_IN_CATEGORY']]
    return {'more_read': more_read,'more_recent': more_recent, 'category': category.name}


@register.filter(name='getThumbnail')
def get_thumbnail(value):
    filename, file_extension = os.path.splitext(value)
    return filename + '_thumb' + file_extension


@register.filter(name='getMediumSize')
def get_thumbnail(value):
    filename, file_extension = os.path.splitext(value)
    return filename + '_medium' + file_extension


@register.filter(name='get600Size')
def get_thumbnail(value):
    filename, file_extension = os.path.splitext(value)
    return filename + '_600' + file_extension