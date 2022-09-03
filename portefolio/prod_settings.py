from .settings import *

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['blogue-tech-hexa.herokuapp.com']


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"