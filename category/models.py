from django.db import models

from movies.models import Movie


class Category(models.Model):
    name = models.CharField(max_length=256)
    movies = models.ManyToManyField(Movie)
