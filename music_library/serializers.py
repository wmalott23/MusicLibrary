from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'release_date', 'genre', 'liked', 'img_url', 'num_likes']
        depth = 1