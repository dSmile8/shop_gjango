# Интернет-магазин на Django.  

Для корректной работы проекта внесите настройки вашей базы данных в следующем файле: 

config/settings.py

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": 'your_db',
            'HOST': 'localhost',
            'USER': 'user',
            'PASSWORD': 'your_password',
        }
    } 
