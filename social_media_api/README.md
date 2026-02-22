# Social Media API
Built with Django REST Framework.

## Deployment Instructions
1. Set DEBUG=False in settings.py.
2. Run 'pip install -r requirements.txt'.
3. Use 'python manage.py collectstatic' for static files.
4. Deployed using Gunicorn as the WSGI server.

## Endpoints
- /api/accounts/register/
- /api/accounts/login/
- /api/posts/
- /api/notifications/
