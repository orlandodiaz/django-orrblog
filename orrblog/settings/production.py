from .base import *

DEBUG = True

DATABASES['default'] = dj_database_url.config(
    conn_max_age=600, ssl_require=True)

SECRET_KEY = os.environ.get('SECRET_KEY')

# SECRET_KEY = S3Connection(os.environ['SECRET_KEY'], os.environ['SECRET_KEY'])
# print(SECRET_KEY)
