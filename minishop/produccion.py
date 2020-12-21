from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'aventurerosdeleste@gmail.com'
EMAIL_HOST_PASSWORD = 'brdwubrlavflgmfx'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"