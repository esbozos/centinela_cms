# coding=UTF-8
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.template import defaultfilters
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

'''
Opciones de menu para categorias
'''
CATEGORIES_MENU_TYPE = (
    ('none', 'None'),
    ('main', _('Main Menu')),
    ('news', _('News Section')),
    )

SLIDER_LOCATION_CHOICES = (
    ('home', _('Home Page')),
    ('news', _('News Section'))
)

'''
Opciones para los post del centinela.
'''

POST_STATUS_CHOICES = (
        ('draft', _('Draft')),
        ('publish', _('Publish')),
        ('trash', _('Trash')),
    )

POST_TYPE_CHOICES = (
        ('page', _('Page')),
        ('post', _('Post')),
    )

'''
opciones para los comentarios de los post
'''

COMMENT_STATUS_CHOICES = (
    ('pending', _('Pending')),
    ('approved', _('Approved')),
    ('spam', _('Spam')),
)

# opciones de estado genericas
STATUS_CHOICES = (
    ('active', _('Active')),
    ('Inactive', _('Inactive')),
)

WIDGET_PLACES = (
    ('top', _('Top')),
    ('lateral', _('Lateral')),
    ('after_post', _('After Post')),
    ('before_post', _('Before Post')),
    ('footer', _('Footer')),
)

'''
    Modelos
'''


class Category(models.Model):
    name = models.CharField(_('name'), max_length=250)
    slug = models.CharField(_('slug'), max_length=100)
    menu_type = models.CharField(_('menu type'), max_length=10, choices=CATEGORIES_MENU_TYPE, default=CATEGORIES_MENU_TYPE[0][0])
    menu_order = models.IntegerField(_('menu_order'), default=10)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Post(models.Model):
    author = models.ForeignKey(User)
    content = RichTextField(_('content'))
    status = models.CharField(_('status'), max_length=20, choices=POST_STATUS_CHOICES, default=POST_STATUS_CHOICES[0][0])
    title = models.CharField(_('title'), max_length=250)
    type = models.CharField(_('type'), max_length=20, choices=POST_TYPE_CHOICES, default=POST_TYPE_CHOICES[1][0])
    image = models.CharField(_('image'), max_length=250, blank=True, null=True)
    mime_type = models.CharField(_('mime_type'), max_length=30, null=True)
    slug = models.SlugField(_('slug'), max_length=100)
    menu_order = models.IntegerField(_('Menu Position'), default=10)
    url_link = models.CharField(_('url_path'), max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(_('created'),default=timezone.now)
    updated_date = models.DateTimeField(_('updated'), default=timezone.now)
    comment_status = models.BooleanField(_('Allow comments?'), default=True)
    comment_count = models.IntegerField(_('comment_count'), default=0)
    category = models.ForeignKey(Category)
    views_count = models.IntegerField(_('Views Count'),default=0)

    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=30) <= self.created_date <= now

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        self.title.encode('utf-8')
        if self.type == 'page':
            self.url_link = '/' + self.category.slug + '/' + self.slug + '/' + str(self.pk)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class Comments(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField(_('content'))
    created_date = models.DateTimeField(_('created'), default= timezone.now)
    author = models.CharField(_('author'), max_length=250)
    status = models.CharField(_('status'), max_length=20, choices=COMMENT_STATUS_CHOICES, default=COMMENT_STATUS_CHOICES[0][0])

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')


class Slider(models.Model):
    title = models.CharField(_('title'), max_length=250, blank=True)
    image_file = models.ImageField(_('image'), upload_to='sliders')
    created_date = models.DateTimeField(_('created'), default=timezone.now)
    link_target = models.CharField(_('link'), max_length=500, blank=True)
    status = models.CharField(_('status'), max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    content = models.CharField(_('content'), max_length=500, default='', blank=True, help_text=_('Text to show over slider'))
    until_date = models.DateTimeField(_('until'), default=timezone.now() + datetime.timedelta(days=settings.CENTINELA['DEFAULT_UNTIL_DAYS']))
    order = models.IntegerField(_('order'), default=10, blank=True)
    location = models.CharField(_('location'), max_length=20, choices=SLIDER_LOCATION_CHOICES, default=SLIDER_LOCATION_CHOICES[0][0])

    def __unicode__(self):
        return self.title

    def is_active(self):
        now = timezone.now()
        return self.until_date >= now and self.status == 'active'


class Widgets(models.Model):
    title = models.CharField(_('title'), max_length=250)
    image_file = models.ImageField(_('Image'), upload_to='linksImages', blank=True)
    content = models.TextField(_('content'), blank=True, help_text=_('widget content, if image is set this will be hide'))
    created_date = models.DateTimeField(_('creado'), default=timezone.now)
    link_target = models.CharField(_('link'), max_length=500, blank=True)
    status = models.CharField(_('status'), max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES)
    until_date = models.DateTimeField(_('until'), default=timezone.now() + datetime.timedelta(days=settings.CENTINELA['DEFAULT_UNTIL_DAYS']))
    order = models.IntegerField(_('order'), default=10, blank=True)
    place = models.CharField(_('Place'), max_length=30, choices=WIDGET_PLACES, default='lateral')

    def __unicode__(self):
        return self.title

    def is_active(self):
        now = timezone.now()
        return self.until_date >= now and self.status == 'active'

    class Meta:
        verbose_name = _('widget')
        verbose_name_plural = _('widgets')


class SocialShare(models.Model):
    name = models.CharField(_('name'), max_length=100)
    html_code = models.TextField(_('html code'), blank=True)
    js_code = models.TextField(_('js code'), blank=True)
    status = models.CharField(_('status'), max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES)
    order = models.IntegerField(_('oder'), default=10)

    def __unicode__(self):
        return self.name

    def is_active(self):
        return self.status == 'active'

    class Meta:
        verbose_name = _('social share')
        verbose_name_plural = _('social shares')


class Theme(models.Model):
    name = models.CharField(_('name'), max_length=50)
    status = models.BooleanField(_('active'), default=False)
    file_name = models.CharField(_('file name'), max_length=100, help_text=_('file located in bootstrap/css folder'))
    created_date = models.DateTimeField(_('created'), default=timezone.now)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('theme')
        verbose_name_plural = _('themes')

