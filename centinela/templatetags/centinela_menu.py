from centinela.models import Category, Post
from django import template

register = template.Library()

@register.assignment_tag
def get_menu():
    menu = []
    menuitems = []
    c = ''
    for m in Post.objects.filter(type='page').order_by('category', 'menu_order'):
        if (0 < m.menu_order < 100) and m.status == 'publish':
            if c != m.category.name:
                if c != '':
                    menu.append({'name': c, 'menuitems': menuitems,})
                c = m.category.name
                menuitems = []
                menuitems.append({'pk': m.pk, 'name': m.title, 'slug': m.slug, 'menu': m.category.name, 'category': m.category.slug})
            else:
                menuitems.append({'pk': m.pk, 'name': m.title, 'slug': m.slug, 'menu': m.category.name, 'category': m.category.slug})
    menu.append({'name': c, 'menuitems': menuitems,})
    return menu

@register.assignment_tag
def get_sections():
    menu = []
    for c in Category.objects.filter(menu_type='news').order_by('menu_order'):
        menu.append({'name': c.name, 'slug': c.slug})
    return menu


