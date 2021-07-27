from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Email
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'aventurerosdeleste@gmail.com'
# EMAIL_HOST_PASSWORD = 'blcqtxbxlawbvwsj'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
