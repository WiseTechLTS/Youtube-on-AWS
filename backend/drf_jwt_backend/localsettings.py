SECRET_KEY = 'qwerty123456!@#$%^qwerty123456!@#$%^'


DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_clone_database',
        'USER': 'root',
        'PASSWORD': 'password',
        'PORT': '3306',
        'HOST': 'db',
    }
}
