from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=150)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=150)
    album_logo = models.FileField(upload_to='Image/album_logo', max_length=550)

    def __str__(self):
        return self.album_title


class Images(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    image_title = models.CharField(max_length=250)
    is_fav = models.BooleanField(default=False)
    image = models.FileField(upload_to='Image/images')

    def __str__(self):
        return self.image_title
