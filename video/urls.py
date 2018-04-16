from . import views
from django.conf.urls import url

app_name = 'video'
urlpatterns =[
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

]