from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.article_list, name='list'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='detail'),
]
