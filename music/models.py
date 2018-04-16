from django.db import models
from django.urls import reverse


class Album(models.Model):
    artist = models.CharField(max_length=150)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=150)
    album_logo = models.FileField(upload_to='Music/album_logo',max_length=550)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk},)


    def __str__(self):
        return self.album_title


class Songs(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_fav = models.BooleanField(default=False)
    song = models.FileField(upload_to='Music/songs')

    def get_absolute_url(self):
        return reverse('music:index', kwargs={})

    def __str__(self):
        return self.song_title
