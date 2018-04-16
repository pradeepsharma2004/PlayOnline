from django.conf.urls import url
from . import views
from django.contrib import admin
app_name = 'music'
urlpatterns =[
    #/music/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /music/no
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    url(r'song/add/$', views.SongCreate.as_view(), name='song-add'),
    url(r'allsongs/$', views.AllSongs.as_view(), name='songs-all'),
   # url(r'searchsong/$', views.AllSongs.as_view(), name='songs-all'),


    #url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite')
]