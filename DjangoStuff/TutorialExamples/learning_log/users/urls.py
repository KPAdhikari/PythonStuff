"""Defines URL patterns for users"""
#from django.conf.urls import url
from django.urls import include, path, re_path
#from django.contrib.auth.views import login
#https://stackoverflow.com/questions/50669185/python-from-django-contrib-auth-views-import-logout-importerror-cannot-import-n
#from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from . import views

#kp: When I didn't have the app_name added, I got the following error:
#   django.core.exceptions.ImproperlyConfigured: Specifying a namespace in include() without providing an app_name is not supported. Set the app_name attribute in the included module, or pass a 2-tuple containing the list of patterns and app_name instead.
#   So, I googled about it and the following forum rescued me.
#https://stackoverflow.com/questions/48608894/improperlyconfigurederror-about-app-name-when-using-namespace-in-include
app_name = 'users'

urlpatterns = [
    ######### Login page ###########
    #url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    #re_path(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    #kp: Above line gave the following error (when tried to open http://localhost:8000/users/login/):
    #       TypeError: login() got an unexpected keyword argument 'template_name' (seen in the browser tab with above url)
    #    so I googled to get to https://stackoverflow.com/questions/55768131/typeerror-login-got-an-unexpected-keyword-argument-template-name
    #    which led me to use LoginView.as_view() instead of login, ...i.e. above line. And it worked
    re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),

    ########### Logout page ########
    # url(r'^logout/$', views.logout_view, name='logout'),
    re_path(r'^logout/$', views.logout_view, name='logout'),

    ########### Registration page ###############
    #url(r'^register/$', views.register, name='register'),
    re_path(r'^register/$', views.register, name='register'),

]
