import os

from dotenv import load_dotenv

load_dotenv()

BACKEND_HOST = os.environ.get('BACKEND_HOST')
BACKEND_PORT = os.environ.get('BACKEND_PORT')
BACKEND_WORKERS = os.environ.get('BACKEND_WORKERS')
BACKEND_RELOAD = os.environ.get('BACKEND_RELOAD')
BACKEND_LOG_LEVEL = os.environ.get('BACKEND_LOG_LEVEL')

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')

DB_HOST_TEST = os.environ.get('DB_HOST_TEST')
DB_PORT_TEST = os.environ.get('DB_PORT_TEST')
DB_NAME_TEST = os.environ.get('DB_NAME_TEST')
DB_USER_TEST = os.environ.get('DB_USER_TEST')
DB_PASS_TEST = os.environ.get('DB_PASS_TEST')

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')

SECRET_AUTH = os.environ.get('SECRET_AUTH')
