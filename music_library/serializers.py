from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'album', 'release_date', 'genre', 'liked']
        depth = 1