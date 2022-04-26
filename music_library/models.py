from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=40)
    artist = models.CharField(max_length=40)
    album = models.CharField(max_length=40)
    release_date = models.DateField()
    genre = models.CharField(max_length=40)
    liked = models.BooleanField()
    img_url = models.CharField(max_length=255, null=True, blank=True)
    num_likes = models.IntegerField(null=True)
