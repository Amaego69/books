from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)
    description = models.TextField(blank=True)
    publish_date = models.DateField()
    average_rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title
