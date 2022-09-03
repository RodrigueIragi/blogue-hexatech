from .settings import *

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['blogue-tech-hexa.herokuapp.com']

INSTALLED_APPS = ['whitenoise.runserver_nostatic',]


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"