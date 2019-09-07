import os

__STATIC_PATH = os.path.dirname(os.path.dirname(__file__))


STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(__STATIC_PATH, "../django_rest_react/static"),
)

STATIC_ROOT = os.path.join(__STATIC_PATH, '../static/')