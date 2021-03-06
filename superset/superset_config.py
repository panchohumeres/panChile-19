import os

SERVER_NAME = os.getenv('DOMAIN_SUPERSET')
PUBLIC_ROLE_LIKE_GAMMA = True
SESSION_COOKIE_SAMESITE = None # One of [None, 'Lax', 'Strict']
SESSION_COOKIE_HTTPONLY = False
MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')
POSTGRES_DB=os.getenv('POSTGRES_DB')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD')
POSTGRES_USER=os.getenv('POSTGRES_USER')
POSTGRES_PORT=str(os.getenv('POSTGRES_PORT'))
HTTP_HEADERS = {'X-Frame-Options': 'ALLOWALL'}

sql_alchemy_string='postgresql+psycopg2://'+POSTGRES_USER+':'+POSTGRES_PASSWORD+'@postgres:'+POSTGRES_PORT+'/'+POSTGRES_DB

CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': 'redis',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': 1,
    'CACHE_REDIS_URL': 'redis://redis:6379/1'}
SQLALCHEMY_DATABASE_URI = \
    sql_alchemy_string
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'thisISaSECRET_1234'