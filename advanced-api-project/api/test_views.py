from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

# Unit tests for the API endpoints.
# Tests cover CRUD operations, filtering, searching, ordering, and permissions.
# Testing Strategy: 
# - Use APITestCase for API-specific testing with simulated requests.
# - Set up test data (users, authors, books) in setUp method.
# - Test happy paths (successful operations) and error paths (unauthenticated access).
# - Verify status codes, response data, and database state changes.
# - Run with: python manage.py test api.test_views
# - Coverage includes all endpoints, permissions, and query features.
class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create test author
        self.author = Author.objects.create(name='Test Author')
        # Create test book
        self.book = Book.objects.create(title='Test Book', publication_year=2020, author=self.author)
        # URLs for separate views
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', kwargs={'pk': self.book.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.pk})

    def test_list_books(self):
        # Test listing all books (read-only, no auth required)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_book(self):
        # Test retrieving a single book (read-only, no auth required)
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_create_book_authenticated(self):
        # Test creating a book when authenticated
        self.client.login(username='testuser', password='testpass')
        data = {'title': 'New Book', 'publication_year': 2021, 'author': self.author.pk}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        # Test creating a book when unauthenticated (should be forbidden)
        data = {'title': 'New Book', 'publication_year': 2021, 'author': self.author.pk}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        # Test updating a book when authenticated
        self.client.login(username='testuser', password='testpass')
        data = {'title': 'Updated Book', 'publication_year': 2020, 'author': self.author.pk}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_update_book_unauthenticated(self):
        # Test updating a book when unauthenticated (should be forbidden)
        data = {'title': 'Updated Book', 'publication_year': 2020, 'author': self.author.pk}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
        # Test deleting a book when authenticated
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_delete_book_unauthenticated(self):
        # Test deleting a book when unauthenticated (should be forbidden)
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_filter_books_by_title(self):
        # Test filtering books by title (on list view)
        response = self.client.get(self.list_url, {'title': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_books_by_author(self):
        # Test filtering books by author name (on list view)
        response = self.client.get(self.list_url, {'author__name': 'Test Author'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_books_by_publication_year(self):
        # Test filtering books by publication year (on list view)
        response = self.client.get(self.list_url, {'publication_year': 2020})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        # Test searching books by title (on list view)
        response = self.client.get(self.list_url, {'search': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_title(self):
        # Create another book for ordering test
        Book.objects.create(title='Another Book', publication_year=2019, author=self.author)
        # Test ordering by title (on list view)
        response = self.client.get(self.list_url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Another Book')
        self.assertEqual(response.data[1]['title'], 'Test Book')

    def test_order_books_by_publication_year(self):
        # Create another book for ordering test
        Book.objects.create(title='Another Book', publication_year=2019, author=self.author)
        # Test ordering by publication year (on list view)
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2019)
        self.assertEqual(response.data[1]['publication_year'], 2020)

    def test_validation_publication_year_future(self):
        # Test serializer validation for future publication year
        self.client.login(username='testuser', password='testpass')
        data = {'title': 'Invalid Book', 'publication_year': 2030, 'author': self.author.pk}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)
