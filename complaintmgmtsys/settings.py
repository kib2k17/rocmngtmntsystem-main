"""
Django settings for complaintmgmtsys project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-))x7_tavyx&&6n!$%mq%_fomfq0!)mc58x!wj7#ulgl5!e#+4h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ngrok http --domain=engaging-elephant-curiously.ngrok-free.app 8000
#ngrok http --domain=engaging-elephant-curiously.ngrok-free.app 8000 --oauth=google --oauth-allow-email=hotline.focrg@dswd.gov.ph

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'engaging-elephant-curiously.ngrok-free.app',
    '172.31.242.12',
    'https://rocmngtmntsystem-main-production.up.railway.app/'# Add this
    # Add any other trusted origins
]


CSRF_TRUSTED_ORIGINS = [
    'https://engaging-elephant-curiously.ngrok-free.app',
]



#'192.168.1.16', 'localhost', '127.0.0.1'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cmsapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cmsapp.middleware.KeepSignedInMiddleware',
    'cmsapp.middleware.NewComplaintsMiddleware',
    'cmsapp.middleware.ActivityLoggerMiddleware', # Ito yung logger middleware
]

ROOT_URLCONF = 'complaintmgmtsys.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'complaintmgmtsys.wsgi.application'


# SQLITE3
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# # SQLITE3
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# #POSTGRESSQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'rocdb',
#         'USER': 'postgres',
#         'PASSWORD': '12345',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


#MYSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rocdb',
        'USER': 'root',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # For collectstatic
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATICSTORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'cmsapp.CustomUser'
KEEP_SIGNED_IN_EXPIRY = 30 * 24 * 60 * 60 

GOOGLE_API_KEY = ""

# settings.py

LOGIN_URL = '/login/'  # Path ng login page
LOGOUT_REDIRECT_URL = '/login/'  # Path after logout
