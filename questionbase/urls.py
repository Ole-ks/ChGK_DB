from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^quest/new/$', views.quest_new, name='quest_new'),
    url(r'^quest/(?P<pk>[0-9]+)/edit/$', views.quest_edit, name='quest_edit'),
    url(r'^quest/(?P<pk>\d+)/remove/$', views.quest_remove, name='quest_remove'),
    url(r'^to_full_form', views.to_full_form, name='to_full_form'),
    url(r'^to_empty_form', views.to_empty_form, name='to_empty_form'),
    url(r'^password/$', views.change_password, name='change_password'),
]