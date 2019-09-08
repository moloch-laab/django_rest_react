DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'apps.leads',
    'apps.frontend',
]

THRID_PARTY_APPS = [
    'rest_framework',
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THRID_PARTY_APPS