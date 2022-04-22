from distutils.command.upload import upload
from email.policy import default
from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Movie(models.Model):
    def __str__(self):
        return self.moviename

    image = models.ImageField(upload_to="images", default='images/none/sample.jpgp')
    moviename = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    rating = models.FloatField()
    
