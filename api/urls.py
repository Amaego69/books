from django.urls import path
from .views import BookListView, BookDetailView, AddToFavoritesView


urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/favorite/', AddToFavoritesView.as_view(), name='add-to-favorites'),
]
