from django.db import models


class Movie(models.Model):
    dvd_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)


class Category(models.Model):
    title = models.CharField(max_length=200)
    movies = models.ManyToManyField(Movie)
