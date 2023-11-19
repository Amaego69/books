from django.contrib import admin
from .models import Book, Author, Genre, Review, Favorite


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'average_rating')
    # Добавьте другие параметры админ-панели здесь по мере необходимости


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    # Дополнительные настройки админки для автора


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # Настройки для жанра


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'created_at')
    # Настройки для отзывов


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'added_on')
    # Настройки для списка избранных книг
