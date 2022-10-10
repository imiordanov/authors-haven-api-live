from .base import *
from .base import env

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", 
    default='django-insecure-f50=fj_@5q=0m&98b6(v$z@er$$w8h-+cb^7f-=!fu3*yz^d1_'
    )

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhod")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "from_iordan@corpy.co.jp"
DOMAIN = env("DOMAIN")
SITE_NAME = "Authors Haven"