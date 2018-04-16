from django.shortcuts import render
from django.views import generic
from .models import Album


class IndexView(generic.ListView):
    template_name = 'image/index.html'
    context_object_name = 'image_album_list'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    template_name = 'image/Detail.html'
    model = Album

