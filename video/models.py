from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=150)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=150)
    album_logo = models.FileField(upload_to='video/album_logo', max_length=550)

    def __str__(self):
        return self.artist


class Videos(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    video_title = models.CharField(max_length=250)
    video_thumbnail = models.FileField(upload_to='Video/video_thumbnail')
    is_fav = models.BooleanField(default=False)
    video = models.FileField(upload_to='Video/video')

    def __str__(self):
        return self.video_title
