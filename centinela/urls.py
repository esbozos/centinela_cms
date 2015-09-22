from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [

    url(r'^nosotros/$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[a-zA-Z0-9-]+)/(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.NewsView.as_view(), name='news'),
    url(r'^(?P<category>[a-zA-Z0-9-]+)/$', views.CategoryPostList.as_view(), name='category_post_list'),
    url(r'^(?P<category>[a-zA-Z0-9-]+)/(?P<slug>[a-zA-Z0-9-]+)/(?P<post_id>[0-9]+)/$', views.page, name='page')
]

urlpatterns += staticfiles_urlpatterns()
