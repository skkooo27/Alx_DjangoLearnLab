# TODO List for Fixing Django Project Checks

## Task 1: Fix Library Import in views.py
- [x] Ensure `from .models import Library` is present in `relationship_app/views.py`
- [x] Verify the LibraryDetailView uses the Library model correctly

## Task 2: Update URL Patterns for Authentication Views
- [x] Import `LoginView` and `LogoutView` from `django.contrib.auth.views` in `relationship_app/urls.py`
- [x] Change login URL to use `LoginView.as_view(template_name='relationship_app/login.html')`
- [x] Change logout URL to use `LogoutView.as_view(template_name='relationship_app/logout.html')`

## Task 3: Ensure Permission Decorator Import in views.py
- [x] Verify `from django.contrib.auth.decorators import permission_required` is present in `relationship_app/views.py`
- [x] Confirm permission_required is used on add, edit, delete book views

## Task 4: Test the Changes
- [ ] Run the Django server and test the views
- [ ] Verify all checks pass
