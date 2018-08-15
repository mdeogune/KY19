import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "yqmjpc%wx0-=4ov&td)5i!$1cbx(7m)b7tcb5^g^n40=&2#sak"


DEBUG = True
#for heroku
if os.environ.get('production', '') == 'True':
    DEBUG = False

USE_TZ = True
APPEND_SLASH  = True

# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'django.contrib.auth',
    'django.contrib.sites',
    'API',
    #'django.contrib.sites',
    'etc',
    'event',
    'users',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'corsheaders',

    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'allauth.socialaccount.providers.google',
    # Disable Django's own staticfiles handling in favour of WhiteNoise, for
    # greater consistency between gunicorn and `./manage.py runserver`. See:
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ORIGIN_WHITELIST = (
    'localhost:4200',
)

ROOT_URLCONF = 'kashiyatra.urls'

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

                'django.template.context_processors.i18n',
                # Required by allauth template tags
 #               "django.core.context_processors.request",
          ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'kashiyatra.wsgi.application'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)
AUTH_USER_MODEL = 'users.KYProfile'

# X_FRAME_OPTIONS = 'ALLOWALL'

# XS_SHARING_ALLOWED_METHODS = ['POST','GET','OPTIONS', 'PUT', 'DELETE']
#LOGIN_URL = '/form'
LOGIN_URL= '/form'
LOGIN_URL_email= '/email_reg/'
LOGIN_URL_social= '/accounts/'

SOCIALACCOUNT_QUERY_EMAIL = True
LOGIN_REDIRECT_URL = "/dashboard/"

ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USER_EMAIL_FIELD = 'email'
ACCOUNT_EMAIL_VERIFICATION=False
ACCOUNT_USER_USERNAME_FIELD = None


SENDGRID_API_KEY =''
EMAIL_BACKEND = "sgbackend.SendGridBackend"

ACCOUNT_FORMS = {
    # 'signup': 'users.forms.RegisterForm'
    'reset_password': 'users.forms.MyResetPasswordForm'
}

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        # 'LOCALE_FUNC': '',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.4',

    },
	
'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }


    
}
# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

'''
NOTE: angular builds static files with same name in dev mode. so make sure to run either ca or user build 
at a time
'''
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "templates/angular/user/"), 
    os.path.join(BASE_DIR, "templates/angular/ca/"),
    # os.path.join(BASE_DIR, "templates/events/"),

    os.path.join(BASE_DIR, "static/meta/"),

]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
SITE_ID=1

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#SENDGRID_API_KEY = os.environ.get('sgkey', '')
