import dj_database_url

from .settings import *

DATABASES['default'] = dj_database_url.config()

DEBUG = False

TEMPLATE_DEBUG = False


SECRET_KEY = 's_k*9nf9n2lygyz1@8nhgor-d(1m(q6ls2bx5(sqr$m&q-=xq'

ALLOWED_HOSTS = ['blogue-hexagone-tech.herokuapp.com']

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']