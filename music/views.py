from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Album, Songs
from django.template import loader
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    content_type = 'album_list'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    template_name = 'music/Detail.html'
    model = Album


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class SongCreate(CreateView):
    model = Songs
    fields = ['album', 'file_type', 'song_title', 'is_fav', 'song', ]


class AllSongs(generic.ListView):
    template_name = 'music/AllSongs.html'
    content_type = 'songs_list'
    context_object_name = 'song_list'

    def get_queryset(self):
        return Songs.objects.all()







































































#def index(request):
   # all_album = Album.objects.all()
  #  context = {'all_album': all_album}
 #   return render(request, 'accounts/index.html', context)

#def detail(request,album_id):

#   #try:
#     #   album = Album.objects.get(pk=album_id)
#    #except(Album.DoesNotExist):
#    #   raise Http404('Album Does Not Exist')
#   album=get_object_or_404(Album,pk=album_id)
#   return render(request, 'accounts/Detail.html', {'album': album})

#def favourite(request,album_id):
#   album = get_object_or_404(Album, pk=album_id)
#   try:
#       selected_song = album.songs_set.get(pk=request.POST['song'])
#   except (KeyError,Songs.DoesNotExist):
#       return render(request, 'accounts/Detail.html', {'album': album, 'error_message':'You Didnot select a valid song',})
#    else:
#      selected_song.is_fav = True
#      selected_song.save()
#       return render(request, 'accounts/Detail.html', {'album': album})







