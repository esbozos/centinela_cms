from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.conf import settings
from django.utils import timezone
import datetime

from .models import Post, Category, Slider, Widgets


class IndexView(generic.ListView):
    model = Post
    template_name = 'centinela/index.html'
    context_object_name = 'latest_post_list'
    paginate_by = settings.CENTINELA['PAGINATE_BY']

    def get_context_data(self):
        context = super(IndexView, self).get_context_data()
        sliders = Slider.objects.filter(location='home').order_by('order')
        context['active_sliders_list'] = sliders
        context['site'] = settings.CENTINELA
        return context

    def get_queryset(self):
        return Post.objects.filter(type='post').filter(status='publish').order_by('-created_date')[:8]


def detail(request, slug, post_id):
    try:
        p = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    p.views_count +=1
    p.save()
    sliders = Slider.objects.filter(location='news').order_by('order')
    return render(request, 'centinela/detail.html', {
        'post': p,
        'active_sliders_list': sliders,
        'site': settings.CENTINELA,
    })


def page(request, category, slug, post_id):
    try:
        p = Post.objects.get(pk=post_id)
    except Post.DoesNoExist:
        raise Http404("Page does not exist")
    p.views_count += 1
    p.save()
    sliders = Slider.objects.filter(location='news').order_by('order')
    return render(request, 'centinela/detail.html', {
        'post': p,
        'active_sliders_list': sliders,
        'site': settings.CENTINELA,
    })


class NewsView(generic.ListView):
    model = Post
    template_name = 'centinela/news.html'
    context_object_name = 'latest_post_list'
    paginate_by = settings.CENTINELA['PAGINATE_BY']

    def get_context_data(self):
        context = super(NewsView, self).get_context_data()
        middle = round(settings.CENTINELA['PAGINATE_BY'] / 4,0)
        context['midle'] = middle
        context['site'] = settings.CENTINELA
        sliders = Slider.objects.filter(location='news').order_by('order')
        context['active_sliders_list'] = sliders

        return context

    def get_queryset(self):
        return Post.objects.filter(type='post', status='publish').order_by('-created_date')


class CategoryPostList(generic.ListView):
    model = Post
    template_name = 'centinela/news.html'
    context_object_name = 'latest_post_list'
    paginate_by = settings.CENTINELA['PAGINATE_BY']

    def get_success_url(self):
        return reverse('category_post_list')

    def get_context_data(self):
        context = super(CategoryPostList, self).get_context_data()
        middle = round(settings.CENTINELA['PAGINATE_BY'] / 4,0)
        context['midle'] = middle
        context['category'] = self.kwargs['category']
        sliders = Slider.objects.filter(location='news').order_by('order')
        context['active_sliders_list'] = sliders
        context['site'] = settings.CENTINELA
        return context

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category'])
        return Post.objects.filter(category=self.category, type='post', status='publish').order_by('-created_date')
