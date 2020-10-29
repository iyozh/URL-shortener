import os
from itertools import chain
from pathlib import Path

import dj_database_url
import sentry_sdk
from django.urls import reverse_lazy
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
GEOIP_PATH = BASE_DIR / "geoip2"

SECRET_KEY = _ds.SECRET_KEY

DEBUG = _ds.DEBUG

INTERNAL_IPS = ["127.0.0.1"]
INTERNAL_HOSTS = ["localhost", "d43f5d5b1ea1.ngrok.io"]
ALLOWED_HOSTS = list(chain(_ds.ALLOWED_HOSTS or [], INTERNAL_IPS, INTERNAL_HOSTS))

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "social_django",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "applications.homepage.apps.HomepageConfig",
    "applications.onboarding.apps.OnboardingConfig",
    "applications.statistics.apps.StatisticsConfig",
    "applications.api_guide.apps.ApiGuideConfig",
    "applications.api.apps.ApiConfig",
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
        "BACKEND": "django.template.backends.jinja2.Jinja2",
        "DIRS": [
            PROJECT_DIR / "jinja2",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "environment": "project.utils.templates.build_jinja2_env",
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
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
                "social_django.context_processors.backends",
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

USE_TZ = False

if not DEBUG:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    PROJECT_DIR / "static",
]
STATIC_ROOT = REPO_DIR / ".static"

ACCOUNT_DEFAULT_HTTP_PROTOCOL = _ds.ACCOUNT_DEFAULT_HTTP_PROTOCOL

LOGIN_URL = reverse_lazy("onboarding:sign-in")

LOGIN_REDIRECT_URL = reverse_lazy("homepage:index")

SOCIAL_AUTH_POSTGRES_JSONFIELD = True

AUTHENTICATION_BACKENDS = (
    "social_core.backends.vk.VKOAuth2",
    "social_core.backends.google.GoogleOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

SOCIAL_AUTH_VK_OAUTH2_KEY = _ds.SOCIAL_AUTH_VK_OAUTH2_KEY
SOCIAL_AUTH_VK_OAUTH2_SECRET = _ds.SOCIAL_AUTH_VK_OAUTH2_SECRET

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = _ds.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = _ds.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET

AWS_ACCESS_KEY_ID = _ds.AWS_ACCESS_KEY_ID
AWS_S3_OBJECT_PARAMETERS = {"ACL": "public-read"}
AWS_QUERYSTRING_AUTH = False
AWS_S3_CODES_LOCATION = _ds.AWS_S3_CODES_LOCATION
AWS_S3_ADDRESSING_STYLE = "path"
AWS_S3_REGION_NAME = _ds.AWS_S3_REGION_NAME
AWS_SECRET_ACCESS_KEY = _ds.AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME = _ds.AWS_STORAGE_BUCKET_NAME


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication"
    ]
}
