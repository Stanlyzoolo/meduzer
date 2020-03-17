"""
Django settings for meduzer project.

Generated by 'django-admin startproject' using Django 1.11.28.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from pathlib import Path
import dj_database_url
from django.urls import reverse_lazy
from dynaconf import settings as _settings

BASE_DIR = Path(__file__).parent.parent.resolve()
PROJECT_DIR = BASE_DIR / "meduzer"
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = _settings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = _settings.DEBUG

ALLOWED_HOSTS = _settings.ALLOWED_HOSTS

# Application definition
SITE_ID = 1
INSTALLED_APPS = [
    "account.apps.AccountConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog.apps.BlogConfig",
    "taggit",
    "django.contrib.sites",
    "django.contrib.sitemaps",
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

ROOT_URLCONF = "meduzer.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [PROJECT_DIR / "templates"],
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

WSGI_APPLICATION = "meduzer.wsgi.application"

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

db_url = _settings.DATABASE_URL
if _settings.ENV_FOR_DYNACONF == "heroku":
    db_url = os.getenv("DATABASE_URL")

DATABASES = {"default": dj_database_url.parse(db_url, conn_max_age=600)}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_ROOT_DIR = BASE_DIR / "static"
STATIC_ROOT_DIR.mkdir(exist_ok=True)
STATIC_ROOT = STATIC_ROOT_DIR.as_posix()

STATIC_URL = "/static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "/media/")
STATICFILES_DIRS = [PROJECT_DIR / "static"]

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "stanlyzoolo@gmail.com"
EMAIL_HOST_PASSWORD = "vovka51088"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

LOGIN_REDIRECT_URL = reverse_lazy("blog:post_list")
LOGIN_URL = "login"
LOGOUT_URL = "logout"
