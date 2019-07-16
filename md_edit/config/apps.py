# Application definition

DJANGO_DEFAULT_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize'
]

THIRD_PARTY_APPS = [
    'debug_toolbar',
    'silk',
]

CUSTOM_APPS = []

SITE_ID = 1

INSTALLED_APPS = DJANGO_DEFAULT_APPS + THIRD_PARTY_APPS + CUSTOM_APPS
