from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^with_answers$', views.search_w_a, name='search_w_a'),
    url(r'^no_answers$', views.search_n_a, name='search_n_a'),
    url(r'^quest/new/$', views.quest_new, name='quest_new'),
    url(r'^quest/(?P<pk>[0-9]+)/edit/$', views.quest_edit, name='quest_edit'),
    url(r'^quest/(?P<pk>\d+)/remove/$', views.quest_remove, name='quest_remove'),
    url(r'^quest/(?P<pk>\d+)/delete_forever/$', views.delete_forever, name='delete_forever'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^deleted/$', views.deleted, name='deleted'),
    url(r'^quest/(?P<pk>\d+)/restore/$', views.quest_restore, name='quest_restore'),

]