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

#MY EMAIL SETTING
EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.cremark.com.py'  
EMAIL_USE_TLS = True
EMAIL_PORT = 587  #This will be different based on your Host, for Namecheap I use this`
EMAIL_HOST_USER = 'testeo@cremark.com.py' # Ex: info@pure.com
EMAIL_HOST_PASSWORD = 'bC+^G23eP]HB' # for the email you created through cPanel. The password for that

CKEDITOR_UPLOAD_PATH = "uploads/"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER