from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^with_answers$', views.search_w_a, name='search_w_a'),
    url(r'^no_answers$', views.search_n_a, name='search_n_a'),
    url(r'^quest/new/$', views.quest_new, name='quest_new'),
    url(r'^blitz_quest/new/$', views.blitz_quest_new, name='blitz_quest_new'),
    url(r'^quest/(?P<pk>\d+)/edit/$', views.quest_edit, name='quest_edit'),
    url(r'^blitz_quest/(?P<pk>\d+)/edit/$', views.blitz_quest_edit, name='blitz_quest_edit'),
    url(r'^quest/(?P<pk>\d+)/remove/$', views.quest_remove, name='quest_remove'),
    url(r'^quest/(?P<pk>\d+)/delete_forever/$', views.delete_forever, name='delete_forever'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^deleted/$', views.deleted, name='deleted'),
    url(r'^quest/(?P<pk>\d+)/restore/$', views.quest_restore, name='quest_restore'),

    url(r'^pkg/new/$', views.pkg_new, name='pkg_new'),
    url(r'^pkg_list/$', views.pkg_list, name='pkg_list'),
    url(r'^pkg_detail/(?P<pk>\d+)/$', views.pkg_detail, name='pkg_detail'),
    url(r'^add_quest_to_pkg/$', views.add_quest_to_pkg, name='add_quest_to_pkg'),

]