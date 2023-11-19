from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from books.models import Book, Favorite
from api.serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import RetrieveAPIView

from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genres', 'authors', 'publish_date']


class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AddToFavoritesView(APIView):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        user = request.user
        favorite, created = Favorite.objects.get_or_create(user=user, book=book)

        if created:
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
