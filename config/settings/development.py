import os
from dotenv import load_dotenv
from config.settings.common import *


DEBUG = os.getenv("DEBUG", True)


ALLOWED_HOSTS = ["localhost"]


STATICFILES_DIRS = [
    BASE_DIR / "static",
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


load_dotenv()

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# Create your own `SECRET_KEY` here for use in Development.
# This one is provided here for user to get the DjangoCustomUserStarter up and running quickly.
# Ideally, you would not run with `SECRET_KEY` exposed in development either.
# You can set a `SECRET_KEY` on you development computer system.
# Create a specific `SECRET_KEY` for development and use it in development only.
# Create a specific `SECRET_KEY` for production and use it in production only.

# Get `SECRET_KEY` (first method argument) from environment variable
# `SECRET_KEY`, if it exists, or use the default one (second method argument)
# provided here:
# If user has a `SECRET_KEY` set in their environment variable, it will be used.
# Otherwise, the default one provided here will be used.
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-mm8cx0al6wo$$0hhv3&eevzsst9dbw&(5p$#9k(1rx%e@j+=$l",
)

# To create a new `SECRET_KEY`:
"""
    python manage.py shell
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
"""
