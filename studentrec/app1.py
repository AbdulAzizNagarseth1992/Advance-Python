django-admin startproject student_api
cd student_api
django-admin startapp students
# student_api/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'student_db',  # Name of your MongoDB database
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'students',  # Add the students app
    'rest_framework',  # To create REST APIs
]
