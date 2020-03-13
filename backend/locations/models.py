from django.db import models


class Movie(models.Model):
    original_title = models.CharField(max_length=200)
    hungarian_title = models.CharField(max_length=200)
    year = models.IntegerField(default=1888)
    cities = models.ManyToManyField('City', blank=True)

    class Meta:
        ordering = ['original_title']

    def __str__(self):
        return self.original_title


class City(models.Model):
    name = models.CharField(max_length=170)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    movies = models.ManyToManyField('Movie', through=Movie.cities.through, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name