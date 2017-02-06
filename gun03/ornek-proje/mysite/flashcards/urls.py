from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  # home page
    url(r'^next/(?P<card_id>[0-9]+)$', views.next_card, name='next_card'),  # next card
    url(r'^correct/(?P<card_id>[0-9]+)$', views.correct, name='correct'),  # correct
    url(r'^correct-list/$', views.correct_list, name='correct_list'),  # correct list
    url(r'^pending-list/$', views.pending_list, name='pending_list'),  # pending list
]
