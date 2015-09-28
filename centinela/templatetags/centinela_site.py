from centinela.models import SocialShare
from django import template
from django.conf import settings
from centinela.models import Theme
register = template.Library()


@register.assignment_tag
def get_title():
    return {'title': settings.CENTINELA['SITE_TITLE']}


@register.assignment_tag
def get_theme():
    t = Theme.objects.filter(status=True)[:1]
    file_name = 'bootstrap.min.css'
    for th in t:
        file_name = th.file_name

    return {'file_name': file_name}