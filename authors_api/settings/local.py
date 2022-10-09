from .base import *
from .base import env

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", 
    default='django-insecure-f50=fj_@5q=0m&98b6(v$z@er$$w8h-+cb^7f-=!fu3*yz^d1_'
    )

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

