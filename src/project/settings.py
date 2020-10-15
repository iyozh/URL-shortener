import os
from itertools import chain
from pathlib import Path

import dj_database_url
import sentry_sdk
from dynaconf import settings as _ds
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn=_ds.SENTRY_DSN,
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
)
BASE_DIR = Path(__file__).parent.parent
PROJECT_DIR = BASE_DIR / "project"
REPO_DIR = BASE_DIR.parent

SECRET_KEY = _ds.SECRET_KEY

DEBUG = _ds.DEBUG

INTERNAL_IPS = ["127.0.0.1"]
INTERNAL_HOSTS = ["localhost"]
ALLOWED_HOSTS = list(chain(_ds.ALLOWED_HOSTS or [], INTERNAL_IPS, INTERNAL_HOSTS))

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "applications.homepage.apps.HomepageConfig",
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

ROOT_URLCONF = "project.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"

development_database_url = _ds.DATABASE_URL
database_url = os.getenv("DATABASE_URL", development_database_url)
database_params = dj_database_url.parse(database_url)

DATABASES = {"default": database_params}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

if not DEBUG:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    PROJECT_DIR / "static",
]
STATIC_ROOT = REPO_DIR / ".static"

ACCOUNT_DEFAULT_HTTP_PROTOCOL = _ds.ACCOUNT_DEFAULT_HTTP_PROTOCOL
