# -*- coding: utf-8 -*-
from centinela.models import Category, Post, Widgets
from django import template
from django.conf import settings
from django.utils import timezone
import datetime

register = template.Library()


@register.inclusion_tag("centinela/more_posts.html")
def get_more_read():
    om = timezone.now() - datetime.timedelta(days=30)
    more_read = Post.objects.filter(created_date__gt=om).filter(views_count__gt=0).filter(status='publish').order_by('-views_count')[:settings.CENTINELA['MAX_MORE_READ_RESULT']]
    more_recent = Post.objects.filter(status='publish', type='post').order_by('-created_date')[:settings.CENTINELA['MAX_MORE_READ_RESULT']]
    return {'more_read': more_read, 'more_recent': more_recent, 'title': 'Lo más Leido', 'category': 'all'}


@register.inclusion_tag("centinela/widgets.html")
def get_widgets():
    now = timezone.now()
    widgets = Widgets.objects.filter(until_date__gt=now).filter(status='active').order_by('order')
    return {'widgets': widgets}


@register.inclusion_tag("centinela/more_posts.html")
def get_more_in_category(category):
    om = timezone.now() - datetime.timedelta(days=30)
    more_read = Post.objects.filter(created_date__gt=om, views_count__gt=0, category=category, status='publish').order_by('-views_count')[:settings.CENTINELA['MAX_MORE_IN_CATEGORY']]
    more_recent = Post.objects.filter(status='publish', type='post').order_by('-created_date')[:settings.CENTINELA['MAX_MORE_IN_CATEGORY']]
    return {'more_read': more_read,'more_recent': more_recent, 'category': category.name}