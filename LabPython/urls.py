"""LabPython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from PythonLab import views

urlpatterns = patterns('',
    #url(r'^$', include(urls)),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^trains/$', views.trains, name='trains'),
    url(r'^cabinet/$', views.cabinet, name='cabinet'),
    url(r'^add_invoice/$', views.add_invoice, name='add_invoice'),
    url(r'^pay_invoice/$', views.pay_invoice, name='pay_invoice'),

    #Sessions
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^login_view/$', views.login_view, name='login_view'),
    url('^register/', CreateView.as_view(template_name='register.html', form_class=UserCreationForm, success_url='/login/')),
)
