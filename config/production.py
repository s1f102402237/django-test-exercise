import os
import dj_database_url
from .settings import ALLOWED_HOSTS, MIDDLEWARE, BASE_DIR

DEBUG = True
SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS.append(os.environ['RENDER_EXTERNAL_HOSTNAME'])

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

DATABASES = {
    'default': dj_database_url.config()
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
