
"""
Django settings for hms_ccai project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from datetime import timedelta
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-et+d@@7n^2q87xmx1l@v=k-_*q+dx#i9*_wlt(5_n=e%6r$upf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DJONGO_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','51.20.55.76','www.carechainaihmsbackend.tech','carechainaihmsbackend.tech']

CSRF_TRUSTED_ORIGINS = ['https://carechainaihmsbackend.tech/','https://www.carechainaihmsbackend.tech/']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'patient',
    'hos_login',
    'opd',
    'accounts',
    'ipd',
    'doctor',
   'staff',
    'inventory',
    'hospital',
    'emergency',
    'appointment',
    # 'analytics',
    'corsheaders',
    'rest_framework',
    'pharmacy',
   # 'patient_dashboard',
    'rest_framework_simplejwt',
   # 'rest_framework.authtoken',
    'knox',
]
#AUTHENTICATION_BACKENDS = ['hos_login.backends.CustomUserModelBackend']
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',),
    #         'rest_framework_simplejwt.authentication.JWTAuthentication',
     'DEFAULT_PERMISSION_CLASSES': [
         'rest_framework.permissions.IsAuthenticated',
            'rest_framework.permissions.AllowAny',

     ]
}
CORS_ORIGIN_ALLOW_ALL = False  # Set to True if allowing all origins
CORS_ORIGIN_WHITELIST = [
    'https://ccaihms.tech',  # Example: Whitelist your frontend domain
    'https://carechainaihmsbackend.tech',
]
from rest_framework.settings import api_settings

KNOX_TOKEN_MODEL = 'knox.AuthToken'

REST_KNOX = {
#    'SECURE_HASH_ALGORITHM': 'hashlib.sha512',
  'AUTH_TOKEN_CHARACTER_LENGTH': 64,
'TOKEN_LIMIT_PER_USER': None,
  'AUTO_REFRESH': False,
  'MIN_REFRESH_INTERVAL': 60,
  'AUTH_HEADER_PREFIX': 'Token',
  'EXPIRY_DATETIME_FORMAT': api_settings.DATETIME_FORMAT,
  'TOKEN_MODEL': 'knox.AuthToken',

   'USER_SERIALIZER': 'hos_login.serializers.UserSerializer',
    'TOKEN_TTL': timedelta(hours=48)
}
#REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#          'rest_framework.authentication.TokenAuthentication',
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),
#      'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#            'rest_framework.permissions.AllowAny',

#     ]
# }

# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=50),
#     'ROTATE_REFRESH_TOKENS': True,
#     'BLACKLIST_AFTER_ROTATION': True,
#     'UPDATE_LAST_LOGIN': False,

#     'ALGORITHM': 'HS256',

#     'VERIFYING_KEY': None,
#     'AUDIENCE': None,
#     'ISSUER': None,
#     'JWK_URL': None,
#     'LEEWAY': 0,

#     'AUTH_HEADER_TYPES': ('Bearer',),
#     'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
#     'USER_ID_FIELD': 'id',
#     'USER_ID_CLAIM': 'user_id',
#     'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

#     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
#     'TOKEN_TYPE_CLAIM': 'token_type',
#     'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

#     'JTI_CLAIM': 'jti',

#     'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
#     'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
#     'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
# }
AUTH_USER_MODEL = 'hos_login.Custom_User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True



ROOT_URLCONF = 'hms_ccai.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'hms_ccai.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hms_ccai',       # Your database name
        'USER': 'root',   # Your database username
        'PASSWORD': 'ccai',   # Your database password
        'HOST': '127.0.0.1',        # Your database host, default is 'localhost'
        'PORT': '3306',   
         'OPTIONS': {
         "init_command": "SET foreign_key_checks = 0;",
    },                    # Your database port, default is '3306'
    }
}


# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = TrueSECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# LOGGING = {
#     'version': 1,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django.db.backends': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#     },
# }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    # Other paths, if any
    'C:\\Users\\ASUS\\OneDrive\\Desktop\\HMS\\hms_ccai\\frontend\\build\\static',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
