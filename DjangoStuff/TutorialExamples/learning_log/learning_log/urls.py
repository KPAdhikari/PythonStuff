"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.conf.urls import include, url #needed only for Django < 1.9
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),

    #url(r'^users/', include('users.urls', namespace='users')),
    re_path(r'^users/', include('users.urls', namespace='users')),

    #Above line is was already there, followin is added later
    #    according to the text-book instruction (page 413)
    #   May be using url() method is wrong or just a typo. However, the following
    #  forum indicated that above line with path() should be used for the new Django 
    #  versions than the old one with 'url()' and 'include()'. Perhaps this was the
    #  the reason why I failed to sail smoothly last time I tried this example
    # https://stackoverflow.com/questions/44130643/django-admin-urls says:
    #   # In Django 1.9+, you don't need to use include. Use the callable admin.site.urls, not the string 'admin.site.urls'.      url(r'^admin/', admin.site.urls),
    #   # In Django 2.0+, you can use path() instead of url().         path('admin/', admin.site.urls),
    #   # In Django < 1.9 you pass admin.site.urls to include.           url(r'^admin/', include(admin.site.urls)),
    #   # To reverse the admin index url, change the url tag in your template to:       {% url "admin:index" %}
    #
    #url(r'^admin/', include(admin.site.urls)),
    #
    # https://docs.djangoproject.com/en/3.2/topics/http/urls/
    #url(r'', include('learning_logs.urls', namespace='learning_logs')), #old django
    path('',include('learning_logs.urls', namespace='learning_logs'))
]
