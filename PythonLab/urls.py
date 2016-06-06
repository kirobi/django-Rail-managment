from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', 'views.index', name='index'),
    url(r'^routes/$', 'views.routes', name='routes'),
]