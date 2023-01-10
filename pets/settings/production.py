from .settings import *
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]

SECRET_KEY = os.environ["SECRET_KEY"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "corteisjr",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
