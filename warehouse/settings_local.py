from dotenv import load_dotenv
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('NAME_PSQL'),
        'USER': os.getenv('USER_PSQL'),
        'PASSWORD': os.getenv('PASSWORD_PSQL'),
        'HOST': os.getenv('HOST_PSQL'),
        'PORT': os.getenv('PORT_PSQL')
    }
}

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

TIME_ZONE = 'Europe/Moscow'
