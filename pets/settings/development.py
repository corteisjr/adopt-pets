from .settings import *
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]

SECRET_KEY = os.environ["SECRET_KEY"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
