 # Advanced Features and Security Project

This project implements advanced Django features including custom user models, permissions, groups, and security best practices.

## Features Implemented

### 1. Custom User Model
- Extended AbstractUser with additional fields: `date_of_birth` and `profile_photo`.
- Custom manager for user creation.
- Registered in Django admin with custom admin class.

### 2. Permissions and Groups
- Added custom permissions to the Book model: `can_view`, `can_create`, `can_edit`, `can_delete`.
- Views enforce permissions using `@permission_required` decorators.
- Role-based views using `@user_passes_test` for Admin, Librarian, Member roles.

### 3. Security Best Practices
- DEBUG set to False in production.
- Security settings: SECURE_SSL_REDIRECT, SECURE_HSTS_SECONDS, etc.
- CSRF tokens in forms.
- CSP middleware implemented.
- Secure cookies enabled.

### 4. HTTPS and Secure Redirects
- All security settings for HTTPS enforcement.
- Secure headers configured.

## Setup Instructions

1. Install dependencies: `pip install django`
2. Run migrations: `python manage.py makemigrations && python manage.py migrate`
3. Create superuser: `python manage.py createsuperuser`
4. Run server: `python manage.py runserver`

## Managing Permissions and Groups

1. Access Django admin at `/admin/`
2. Go to Groups section.
3. Create groups: Editors, Viewers, Admins.
4. Assign permissions:
   - Editors: can_create, can_edit
   - Viewers: can_view
   - Admins: all permissions
5. Assign users to groups.

## Testing

- Create test users and assign to groups.
- Test access to views based on permissions.
- Verify HTTPS redirects and security headers.
