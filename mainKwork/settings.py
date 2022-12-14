"""
Django settings for mainKwork project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zcjh89a_b@njx_3u5&z_xfp2@kf0^z5-)^56!kwfr6mfcn-pqn'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.kworkclone.herokuapp.com','kworkclone.herokuapp.com']

TIME_ZONE ="UTC"

INSTALLED_APPS = [
    'jazzmin',
    "kworkapp.apps.kworkAppConfig",
    'django_summernote',
    'django_cleanup.apps.CleanupConfig',
    'social_django',
    'sslserver',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'channels',
    'channels_postgres',
    'django_crontab',
    'notifications',
    'taggit',
    'django_countries',
    'django.contrib.humanize',
    'django_apscheduler',
]



AUTH_USER_MODEL = 'kworkapp.User'


# APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"  # Default

SCHEDULER_DEFAULT = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware', # <-- Here
]

CSRF_TRUSTED_ORIGINS = ['https://kworkclone.herokuapp.com']

TIME_ZONE = 'UTC'

ROOT_URLCONF = 'mainKwork.urls'

TAGGIT_CASE_INSENSITIVE = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'kworkapp.context_processors.message_processor',
                'kworkapp.context_processors.menu_procesor',
                'social_django.context_processors.backends',  # <-- Here
                'social_django.context_processors.login_redirect', # <-- Here
            ],
        },
    },
]

WSGI_APPLICATION = 'mainKwork.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {   
     "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd5d74m1d4o1c7b', 
        'USER': 'nhqjfuleidgiof', 
        'PASSWORD': '4f236a835955197986223617b4bbe49374b79210a2fb4538c877b368142d7d6b',
        'HOST': 'ec2-44-199-9-102.compute-1.amazonaws.com', 
        'PORT': '5432',
    },
    'channels_postgres': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd5d74m1d4o1c7b', 
        'USER': 'nhqjfuleidgiof', 
        'PASSWORD': '4f236a835955197986223617b4bbe49374b79210a2fb4538c877b368142d7d6b',
        'HOST': 'ec2-44-199-9-102.compute-1.amazonaws.com', 
        'PORT': '5432',
	}
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE =  'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

ASGI_APPLICATION = "mainKwork.asgi.application"


CHANNEL_LAYERS = {
     'default': {
         'BACKEND': 'channels_postgres.core.PostgresChannelLayer',
         'CONFIG': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'd5d74m1d4o1c7b', 
            'USER': 'nhqjfuleidgiof', 
            'PASSWORD': '4f236a835955197986223617b4bbe49374b79210a2fb4538c877b368142d7d6b',
            'HOST': 'ec2-44-199-9-102.compute-1.amazonaws.com', 
            'PORT': '5432',
         },
     },
 }

STATIC_URL = "/static/"

STATIC_ROOT = "static"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_ROOT = "media"

MEDIA_URL = "/media/"

X_FRAME_OPTIONS = 'SAMEORIGIN'
SUMMERNOTE_THEME = 'bs4'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_COOKIE_AGE = 300 
AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'kworkapp.backends.MyAuthBackend','django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = '286705580139249'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '4a436cb463ccc80ce51d2885d4f16ea0' 

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "948370186990-gholq7ua8ehflg3vqolq6ujup1lt5lo8.apps.googleusercontent.com"        # App ID
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "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" 


# Social Auth Login 
SOCIAL_AUTH_LOGIN_URL = '/'
SOCIAL_AUTH_LOGIN_ERROR_URL = 'register'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'dashboard'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.get_username',
    'kworkapp.social_auth.social_user',
    # 'users.pipeline.require_email',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'kworkapp.pipeline.get_avatar',
)
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email', 
}
FACEBOOK_EXTENDED_PERMISSIONS = ['email']
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [                 # add this
    ('name', 'name'),
    ('email', 'email'),
    ('picture', 'picture'),
    ('link', 'profile_url'),
]

SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE = True

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
'https://www.googleapis.com/auth/userinfo.email',
'https://www.googleapis.com/auth/userinfo.profile'
]

JAZZMIN_SETTINGS = {
    "site_title": "Letworkbedone Admin",

    "site_header": "Letworkbedone",

    "site_brand": "Letworkbedone",

    "site_logo": None,

    "login_logo": None,

    "login_logo_dark": None,

    "site_logo_classes": "img-circle",

    "site_icon": None,

    "welcome_sign": "Welcome to the library",

    "copyright": "Acme Library Ltd",

    "search_model": "auth.User",

    "user_avatar": None,

    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        {"model": "auth.User"},

        {"app": "books"},
    ],


    "usermenu_links": [
        #{"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    "show_sidebar": True,

    "navigation_expanded": True,

    "hide_apps": [],

    "hide_models": [],

    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    "custom_links": {
        "books": [{
            "name": "Make Messages", 
            "url": "make_messages", 
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },    
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    "related_modal_active": False,

    "custom_css": None,
    "custom_js": None,
    "show_ui_builder": False,

    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
   # "language_chooser": True,
}





