from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=40)
    artist = models.CharField(max_length=40)
    album = models.CharField(max_length=40)
    release_date = models.DateField()
    genre = models.CharField(max_length=40)