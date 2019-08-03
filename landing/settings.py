"""
Django settings for landing project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mdi_h$@x93+^d1)acq3xh%$p5j)1*c2kvlo$%r$fv6#$4zc@-c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'sslserver',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',


    'mail',
    'userprofile',
    'authentication',
]

# AUTH_USER_MODEL = 'userprofile.User'

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'userprofile.serializers.UserSerializer',
}


SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


    #'social_django.middleware.SocialAuthExceptionMiddleware', #social
]

ROOT_URLCONF = 'landing.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                #'social_django.context_processors.backends',  #social
                #'social_django.context_processors.login_redirect', #social
            ],
        },
    },
]

REST_FRAMEWORK = {
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    )
}

REST_USE_JWT = True

CORS_ALLOW_METHODS = [
    '*'
]

CORS_ALLOW_HEADERS = [
    '*'
]
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_ALLOW_ALL = True


WSGI_APPLICATION = 'landing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'bbsydljiuqteeyawp58n-postgresql.services.clever-cloud.com',
        'NAME': 'bbsydljiuqteeyawp58n',
        'USER': 'u1czhnpifeqn0es6ayj8',
        'PASSWORD': 'GvS2ek1Mt0NoCVwWmqMF',
        'PORT': '5432',
    }
}

AUTHENTICATION_BACKENDS = (

    # Others auth providers (e.g. Google, OpenId, etc)
    

    # Facebook OAuth2
    #'social_core.backends.facebook.FacebookAppOAuth2',
    #'social_core.backends.facebook.FacebookOAuth2',

    # django-rest-framework-social-oauth2
    #'rest_framework_social_oauth2.backends.DjangoOAuth2',

    # Django
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',

)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILE_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'smartstartcommunity@gmail.com'
EMAIL_HOST_PASSWORD = 'u998470273'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER



# SOCIAL_AUTH_FACEBOOK_KEY = 428456044438034
# SOCIAL_AUTH_FACEBOOK_SECRET = '1d0c88eb142c41fe3bb574d083b000c1'
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/login/'
# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
# FACEBOOK_EXTENDED_PERMISSIONS = ['email']
# SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
# SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True


# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
#     'fields':'id, name, email'
# }

# SOCIAL_AUTH_PIPELINE = (
# 'social_core.pipeline.social_auth.social_details',
# 'social_core.pipeline.social_auth.social_uid',
# 'social_core.pipeline.social_auth.auth_allowed',
# 'social_core.pipeline.social_auth.social_user',
# 'social_core.pipeline.user.get_username',
# 'social_core.pipeline.social_auth.associate_by_email',
# 'social_core.pipeline.user.create_user',
# 'social_core.pipeline.social_auth.associate_user',
# 'social_core.pipeline.social_auth.load_extra_data',
# 'social_core.pipeline.user.user_details', )

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'rerequest'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'birthday',
            'verified',
            'locale',
            'timezone',
            'link',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'VERIFIED_EMAIL': False,
        'VERSION': 'v4.0',
    }
}
ACCOUNT_ADAPTER = 'apps.authentication.allauth.AllAuthAccountAdapter'
LOGIN_REDIRECT_URL = 'http://localhost:8000/'
# SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_EMAIL_VERIFICATION = 'none'

# FACEBOOK
FACEBOOK_CLIENT_ID = '428456044438034'
FACEBOOK_CLIENT_SECRET = '1d0c88eb142c41fe3bb574d083b000c1'
FACEBOOK_REDIRECT_URI = 'http://localhost:8000/'

# GOOGLE

# TWITTER
