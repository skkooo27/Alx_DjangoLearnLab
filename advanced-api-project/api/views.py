from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# BookListView: Handles listing all books.
# Uses ListCreateAPIView for GET (list) and POST (create) operations.
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Authenticated for create, read-only for list

# BookDetailView: Handles retrieving, updating, and deleting a single book by ID.
# Uses RetrieveUpdateDestroyAPIView for GET, PUT, PATCH, DELETE operations.
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Authenticated for update/delete, read-only for retrieve
