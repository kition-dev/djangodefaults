from django.core.management.utils import get_random_secret_key

from .default_static import *

DEBUG = os.getenv("DEBUG", "false").lower() == "true"
SECRET_KEY = os.getenv("SECRET_KEY", get_random_secret_key())
