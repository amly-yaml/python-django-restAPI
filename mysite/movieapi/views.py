from django.shortcuts import render
from rest_framework import generics
from myapp.models import Movie
from .serializers import MovieSerializer

# Create your views here.
# make generics view API 

# only read function
# class MovieAPIView(generics.ListAPIView):
#     # fetch all the movie database models 
#     queryset = Movie.objects.all()
#     # make json format
#     serializer_class = MovieSerializer

class MovieAPIView(generics.ListCreateAPIView):
    # fetch all the movie database models 
    queryset = Movie.objects.all()
    # make json format
    serializer_class = MovieSerializer

# only retrieve function
# class MovieDetailAPI(generics.RetrieveAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


class MovieDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer