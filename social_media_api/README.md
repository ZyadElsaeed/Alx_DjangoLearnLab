# Social Media API - Production Ready
Final capstone project for ALX Back-End Web Development.

## Deployment Details
- **Database**: PostgreSQL (configured via dj-database-url)
- **WSGI Server**: Gunicorn
- **Static Files**: Served via WhiteNoise
- **Security**: DEBUG set to False, Security headers enabled

## Setup
1. Run `pip install -r requirements.txt`
2. Run `python manage.py collectstatic`
3. Set up environment variables for DATABASE_URL and SECRET_KEY.
