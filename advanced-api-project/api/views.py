from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer

# BookListView: Retrieves all books with filtering, searching, and ordering capabilities.
# Allows read-only access for unauthenticated users.
# Filtering: by title, author__name, publication_year
# Searching: on title and author__name
# Ordering: by title and publication_year (default: title)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering

# BookDetailView: Retrieves a single book by ID.
# Allows read-only access for unauthenticated users.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# BookCreateView: Handles creating a new book.
# Restricted to authenticated users only.
# Includes data validation via serializer.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# BookUpdateView: Handles updating an existing book by ID.
# Restricted to authenticated users only.
# Ensures proper form submission handling and validation.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# BookDeleteView: Handles deleting a book by ID.
# Restricted to authenticated users only.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
