"""Defines URL patterns for learning_logs."""
#from django.conf.urls import url  #old version of Django < 1.9?
#https://stackoverflow.com/questions/44130643/django-admin-urls says:
#https://docs.djangoproject.com/en/3.2/topics/http/urls/
#

#from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    #url(r'^$', views.index, name='index'),
    #path(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
    #path('', views.IndexView.as_view(), name='index'),

    # Show all topics.
    #url(r'^topics/$', views.topics, name='topics'),
    #path(r'^topics/$', views.topics, name='topics'), #kp: with this the url in the browser 
    #     (when clicked on 'Topics' linked showed up like 'http://127.0.0.1:8000/^topics$/'
    path(r'topics/', views.topics, name='topics'),

    # Detail page for a single topic
    #url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'), #To Utilize Regex, we must use re_path() instead
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # Page for adding a new topic
    # url(r'^new_topic/$', views.new_topic, name='new_topic'),
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # Page for editing an entry
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

]
