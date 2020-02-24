"""
Django settings for source-finder project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""


import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition

INSTALLED_APPS = [
    "training",
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "8fdhkjfs(!t678fhe37e%^3764dgys_@%6gjskksR67b"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "source_finder",
        "USER": "source_finder",
        "PASSWORD": "source_finder",
        "HOST": "localhost",
        "PORT": "5432",
    }
}