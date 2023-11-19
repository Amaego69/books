from django.db import models
from django.conf import settings


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

    def update_average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            average = reviews.aggregate(models.Avg('rating'))['rating__avg']
            self.average_rating = average if average is not None else 0.0
            self.save()

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1, choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user} on {self.book}'

    class Meta:
        unique_together = ('book', 'user')


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='favorited_by')
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f'{self.book.title} favorited by {self.user}'
