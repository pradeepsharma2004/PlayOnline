from django.conf.urls import url
from . import views
from django.urls import path, include
from django.contrib import admin

app_name = 'image'


urlpatterns =[
    #/image/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

]
