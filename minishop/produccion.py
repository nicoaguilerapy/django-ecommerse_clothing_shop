from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'uverodevpy$djando-casafenix',
            'USER': 'uverodevpy',
            'PASSWORD': 'MejoresPrendas.357',
            'HOST': 'uverodevpy.mysql.pythonanywhere-services.com',
            'PORT': '3306',
        }
    }

# Email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'aventurerosdeleste@gmail.com'
EMAIL_HOST_PASSWORD = 'blcqtxbxlawbvwsj'
EMAIL_PORT = 587
EMAIL_USE_TLS = True