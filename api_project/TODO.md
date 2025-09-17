# TODO for Introduction to Building APIs with Django REST Framework

## Task 0: Setting Up a New Django Project with Django REST Framework
- [x] Create api_project directory
- [x] Set up Python virtual environment
- [x] Install Django and djangorestframework
- [x] Create Django project named api_project
- [x] Add 'rest_framework' to INSTALLED_APPS in settings.py
- [x] Create 'api' app
- [x] Add 'api' to INSTALLED_APPS
- [x] Define Book model with title and author in api/models.py
- [x] Run makemigrations
- [x] Run migrate
- [x] Run development server (system checks passed, port permission issue noted)

## Task 1: Building Your First API Endpoint with Django REST Framework
- [x] Create serializers.py in api app with BookSerializer
- [x] Create views.py with BookList view (ListAPIView)
- [x] Create urls.py in api app with URL pattern for books/
- [x] Update main api_project/urls.py to include api.urls
- [x] Test the API endpoint (system checks passed, port permission issue noted)

## Task 2: Implementing CRUD Operations with ViewSets and Routers in Django REST Framework
- [ ] Replace BookList with BookViewSet (ModelViewSet)
- [ ] Set up DefaultRouter in api/urls.py
- [ ] Register BookViewSet with router
- [ ] Update urlpatterns to include router.urls
- [ ] Test CRUD operations (GET, POST, PUT, DELETE)

## Task 3: Implementing Authentication and Permissions in Django REST Framework
- [ ] Add rest_framework.authtoken to INSTALLED_APPS
- [ ] Run migrate for token tables
- [ ] Add token authentication to DEFAULT_AUTHENTICATION_CLASSES
- [ ] Implement token retrieval view
- [ ] Add permission classes to ViewSet
- [ ] Test authentication and permissions
