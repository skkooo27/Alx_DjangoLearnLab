# Advanced API Development with Django REST Framework

This project demonstrates advanced Django REST Framework concepts including custom serializers, generic views, filtering/searching/ordering, and unit testing for a simple book library API.

## Project Structure
- `advanced_api_project/`: Main Django project settings and URLs.
- `api/`: Django app containing models, serializers, views, URLs, and tests.
  - `models.py`: Author and Book models with one-to-many relationship.
  - `serializers.py`: Custom BookSerializer (with validation) and AuthorSerializer (nested books).
  - `views.py`: Separate generic views for List, Detail, Create, Update, Delete operations with permissions.
  - `urls.py`: API endpoints under `/api/`.
  - `test_views.py`: Comprehensive unit tests for CRUD, permissions, filtering, searching, ordering.
- `db.sqlite3`: SQLite database (ignored in .gitignore).

## Setup Instructions
1. Navigate to the project directory: `cd advanced-api-project`
2. Install dependencies: `pip install django djangorestframework django-filter`
3. Run migrations: `python manage.py makemigrations && python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Run the development server: `python manage.py runserver`
6. Access the API at `http://127.0.0.1:8000/api/`

## API Endpoints
All endpoints are under `/api/`:

### Read-Only (Unauthenticated Access Allowed)
- **List Books**: `GET /books/` - Retrieve all books with optional filtering (`?title=...&author__name=...&publication_year=...`), searching (`?search=...`), ordering (`?ordering=title` or `publication_year`).
- **Retrieve Book**: `GET /books/<int:pk>/` - Get a single book by ID.

### Authenticated Only (Use token or session authentication)
- **Create Book**: `POST /books/create/` - Add a new book. Body: `{"title": "Book Title", "publication_year": 2020, "author": 1}`. Validates publication year not in future.
- **Update Book**: `PUT/PATCH /books/update/<int:pk>/` - Modify a book. Body as above.
- **Delete Book**: `DELETE /books/delete/<int:pk>/` - Remove a book.

## Permissions
- Read operations (List, Retrieve): Open to all users.
- Write operations (Create, Update, Delete): Require authentication (`IsAuthenticated`).

## Customizations
- **Serializers**: BookSerializer validates `publication_year <= current year`. AuthorSerializer nests related books.
- **Filtering**: Uses DjangoFilterBackend for exact matches on title, author name, year.
- **Searching**: SearchFilter on title and author name.
- **Ordering**: OrderingFilter on title and publication year (default: title ascending).
- **Views**: Separate generic views for modularity. No custom methods needed beyond built-in features.

## Testing
- Tests in `api/test_views.py` cover:
  - CRUD operations with/without authentication.
  - Permissions enforcement (403 for unauthenticated writes).
  - Filtering, searching, ordering.
  - Serializer validation (e.g., future year rejected with 400).
- Run tests: `python manage.py test api.test_views`
- All 15 tests pass, verifying response data, status codes, and database integrity.

## Manual Testing
Use tools like Postman or curl:
- List: `curl http://127.0.0.1:8000/api/books/?search=Test&ordering=publication_year`
- Create (after login): `curl -X POST -H "Content-Type: application/json" -d '{"title":"New Book","publication_year":2020,"author":1}' http://127.0.0.1:8000/api/books/create/`

For authentication, use Django's session or DRF's token auth (configure as needed).

## Learning Objectives Achieved
- Custom serializers with validation and nesting.
- Generic views and mixins for CRUD.
- Advanced querying (filtering, searching, ordering).
- Comprehensive unit testing with Django's test framework.

This setup provides a robust, testable API for managing books and authors.
