from pathlib import Path
import os, sys
import logging
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-57usab^u_#cvrcvzut02+==ia&z@a^+_*(1+8p&00_!!&du%%y'
DEBUG = True

ALLOWED_HOSTS = []

sys.path.append(
    os.path.join(BASE_DIR, "apps")
)


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',
    'bootstrapform',
    'corsheaders',
]

INSTALLED_APPS += [
    'base',
    'users',
]


CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'skin': "moono-lisa",
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['NumberedList', 'BulletedList', 'Print', 'Outdent', 'Indent', '-', 'JustifyLeft', 
            'JustifyCenter', 'JustifyRight', 'JustifyBlock','RemoveFormat', 'SelectAll','Maximize','Strike','Select','Save'],
            
            ['Cut', 'Copy', 'Paste', 'Undo', 'Redo','Bold', 'Italic', 'Underline','Image','Link',
            'Unlink','TextColor', 'BGColor','Find','Preview','NewPage','PageBreak','a11yhelp','Table','About'],
            
            ['Styles', 'Format', 'Font', 'FontSize'],
        ],'width': '100%'
    },
    'DescricaoServico': {
        'skin': "moono-lisa",
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['NumberedList', 'BulletedList', 'Print', 'Outdent', 'Indent', 'color', 'JustifyLeft', 
            'JustifyCenter', 'JustifyRight', 'JustifyBlock','RemoveFormat', 'SelectAll','Maximize','Strike','Select','Save'],
            
            ['Cut', 'Copy', 'Paste', 'Undo','Redo','Bold', 'Italic', 'Underline','','Link',
            'Unlink','TextColor', 'BGColor','Find','Preview','NewPage','PageBreak','a11yhelp','Table','About'],
            
            ['Styles', 'Format', 'Font', 'FontSize'],
        ],'width': '100%'
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True   
ROOT_URLCONF = 'configuration.urls'

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

WSGI_APPLICATION = 'configuration.wsgi.application'
AUTH_USER_MODEL = "users.User" 
LOGIN_REDIRECT_URL = 'solicitacoes'
LOGIN_URL = 'login'
LOGOUT_URL = ''
LOGOUT_REDIRECT_URL = ''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL='/media/'
MEDIA_ROOT='media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
