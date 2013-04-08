### Settings for Local environment ###

# Keep this file out of Version Control! (.gitignore)

__author__ = '{{ AUTHOR_NAME }}'

ENV_STATE = 'PROD' # Either DEV, STAGING, or PROD,

# Development Database
DEV_DB = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',  # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Unique secret key -- do not share with anyone or post online
# Use http://www.miniwebtool.com/django-secret-key-generator/ to generate a new secret key
DEV_SECRET_KEY = 'n&mw-6bh7-wo1i7y2-#5q$qnmwbp%(@_&&hrark98r!kh9u!(9'

DEV_EMAIL_PASSWORD = ''
