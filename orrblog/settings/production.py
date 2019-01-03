from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    '0.0.0.0', 'localhost', '127.0.0.1', 'orrblog.herokuapp.com',
    'orlandodiaz.co'
]

# Use Heroku Postgres database from the DATABASE_URL environmental config variable
DATABASES['default'] = dj_database_url.config(
    conn_max_age=600, ssl_require=True)

# Static FILES
MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
