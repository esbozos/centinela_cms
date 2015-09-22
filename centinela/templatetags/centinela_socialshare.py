from centinela.models import SocialShare
from django import template

register = template.Library()


@register.assignment_tag
def get_share_buttons():
    buttons = SocialShare.objects.filter(status='active').order_by('order')
    return {'buttons': buttons}