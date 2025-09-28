from django.shortcuts import render
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

# BookListView: Handles listing all books with filtering, searching, and ordering capabilities.
# Uses ListCreateAPIView for GET (list) and POST (create) operations.
# Filtering: by title, author__name, publication_year
# Searching: on title and author__name
# Ordering: by title and publication_year
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Authenticated for create, read-only for list
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering

# BookDetailView: Handles retrieving, updating, and deleting a single book by ID.
# Uses RetrieveUpdateDestroyAPIView for GET, PUT, PATCH, DELETE operations.
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Authenticated for update/delete, read-only for retrieve
