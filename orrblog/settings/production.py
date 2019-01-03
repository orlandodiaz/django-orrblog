from .base import *
from boto.s3.connection import S3Connection

DEBUG = True

DATABASES['default'] = dj_database_url.config(
    conn_max_age=600, ssl_require=True)

SECRET_KEY = 'whatever'

# SECRET_KEY = S3Connection(os.environ['SECRET_KEY'], os.environ['SECRET_KEY'])
# print(SECRET_KEY)
