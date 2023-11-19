from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
