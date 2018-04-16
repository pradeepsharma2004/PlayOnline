from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Album, Videos


class IndexView(generic.ListView):
    template_name = 'video/index.html'
    context_object_name = 'video_album_list'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    template_name = 'video/Detail.html'
    model = Album
