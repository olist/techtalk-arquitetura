from pathlib import Path

import belogging
from dj_database_url import parse as parse_db_url
from prettyconf import config

from utils import get_project_package

# Project Structure
BASE_DIR = Path(__file__).absolute().parents[2]
PROJECT_DIR = Path(__file__).absolute().parents[1]
FRONTEND_DIR = PROJECT_DIR / "frontend"

# Debug & Development
DEBUG = config("DEBUG", default=False, cast=config.boolean)

# Database
DATABASES = {"default": config("DATABASE_URL", cast=parse_db_url)}
DATABASES["default"]["CONN_MAX_AGE"] = config("CONN_MAX_AGE", cast=config.eval, default="None")

# Security & Signup/Signin
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*", cast=config.list)
SECRET_KEY = config("SECRET_KEY")

# i18n & l10n
TIME_ZONE = "UTC"
USE_I18N = False
USE_L10N = False
USE_TZ = True
LANGUAGE_CODE = "en-us"

# Miscelaneous
_project_package = get_project_package(PROJECT_DIR)
ROOT_URLCONF = "{}.urls".format(_project_package)
WSGI_APPLICATION = "{}.wsgi.application".format(_project_package)

# Media & Static
MEDIA_URL = "/media/"
STATIC_URL = "/static/"
STATIC_ROOT = FRONTEND_DIR / "static"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(FRONTEND_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": config("TEMPLATE_DEBUG", default=DEBUG, cast=config.boolean),
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
            ],
        },
    }
]

# Application
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

INSTALLED_APPS = (
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    # 3rd party libs
    "rest_framework",
    "django_extensions",
    "django_filters",
    # apps
    "apps.matches",
)


# Logging
_log_level = config("LOG_LEVEL", default="INFO")
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler",},},
    "loggers": {"django": {"handlers": ["console"], "level": _log_level,},},
}

# Django REST Framework
REST_FRAMEWORK = {
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "UNAUTHENTICATED_USER": None,
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": [],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 25,
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ),
}

# SNS
SNS_ENDPOINT_URL = config("SNS_ENDPOINT_URL", default=None)
SNS_DRY_RUN = config("SNS_DRY_RUN", default=False, cast=config.boolean)

MATCH_CREATED_TOPIC_ARN = config("MATCH_CREATED_TOPIC_ARN")
MATCH_UPDATED_TOPIC_ARN = config("MATCH_UPDATED_TOPIC_ARN")
