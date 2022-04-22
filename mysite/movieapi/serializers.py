from email.mime import image
from unittest.util import _MAX_LENGTH
from myapp.models import Movie
from rest_framework import serializers

# operation taking the database data and convert it into json format
class MovieSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Movie
        fields = ('moviename', 'description', 'rating', 'image')
