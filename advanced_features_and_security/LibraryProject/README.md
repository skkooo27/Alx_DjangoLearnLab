# Advanced Features and Security Project

This Django project implements advanced features including custom user models, permissions, groups, and security best practices.

## Features Implemented

### 1. Custom User Model
- Extended AbstractUser with additional fields: date_of_birth, profile_photo
- Custom manager for user creation
- Integrated into Django admin

### 2. Permissions and Groups
- Custom permissions on Book model in bookshelf app: can_view, can_create, can_edit, can_delete
- Views in relationship_app enforce these permissions
- Groups can be created in Django admin:
  - Editors: can_edit, can_create
  - Viewers: can_view
  - Admins: all permissions

### 3. Security Best Practices
- DEBUG set to False in production
- CSRF tokens in forms
- CSP middleware for Content Security Policy
- Secure settings for XSS, clickjacking, etc.

### 4. HTTPS and Secure Redirects
- SECURE_SSL_REDIRECT = True
- HSTS settings
- Secure cookies

## Setup Instructions
1. Install dependencies
2. Run migrations
3. Create groups in admin
4. Configure web server for HTTPS

## Deployment
- Set ALLOWED_HOSTS
- Use SSL certificate
- Configure web server (e.g., Nginx) for HTTPS
