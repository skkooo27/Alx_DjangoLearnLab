from django.urls import path
from .views import (
    BookListView, BookDetailView, BookCreateView, 
    BookUpdateView, BookDeleteView
)

# URL patterns for the api app.
# /books/ : List all books (GET) - read-only access
# /books/<int:pk>/ : Retrieve a specific book (GET) - read-only access
# /books/create/ : Create a new book (POST) - authenticated users only
# /books/<int:pk>/update/ : Update a specific book (PUT/PATCH) - authenticated users only
# /books/<int:pk>/delete/ : Delete a specific book (DELETE) - authenticated users only
urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
