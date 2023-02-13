import os
from pathlib import Path

from configurations import Configuration, values


class Base(Configuration):
    BASE_DIR = Path(__file__).resolve().parent.parent

    SECRET_KEY = values.Value("django-insecure-secret-key")

    DEBUG = values.BooleanValue(False)

    ALLOWED_HOSTS = values.ListValue([])

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        # App locals
        "src.apps.core.apps.CoreConfig",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "src.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ]
            },
        }
    ]

    WSGI_APPLICATION = "src.wsgi.application"

    DATABASES = values.DatabaseURLValue("sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3"))

    AUTH_PASSWORD_VALIDATORS = [
        {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
        {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
        {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
        {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
    ]

    LANGUAGE_CODE = values.Value("en-us")

    TIME_ZONE = values.Value("UTC")

    USE_I18N = values.BooleanValue(True)

    USE_L10N = values.BooleanValue(True)

    USE_TZ = values.BooleanValue(True)

    STATIC_URL = "/static/"

    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

    EMAIL = values.EmailURLValue("console://")

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


class Dev(Base):
    CACHES = values.CacheURLValue("dummy://")

    Base.INSTALLED_APPS.insert(0, "whitenoise.runserver_nostatic")


class Prod(Base):
    DEBUG = values.BooleanValue(True)

    SECURE_HSTS_SECONDS = values.Value(3600)

    SECURE_SSL_REDIRECT = values.BooleanValue(True)

    SESSION_COOKIE_SECURE = values.BooleanValue(True)

    CSRF_COOKIE_SECURE = values.BooleanValue(True)
