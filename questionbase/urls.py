from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.question_list, name='quest_list'),
    url(r'^quest/(?P<pk>[0-9]+)/$', views.quest_detail, name='quest_detail'),
    url(r'^quest/new/$', views.quest_new, name='quest_new'),
    url(r'^quest/(?P<pk>[0-9]+)/edit/$', views.quest_edit, name='quest_edit'),
    url(r'^search/$', views.search, name='search'),
    url(r'^quest/(?P<pk>\d+)/remove/$', views.quest_remove, name='quest_remove'),
]