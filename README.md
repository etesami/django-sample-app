# Django Sample App

- [Django Sample App](#django-sample-app)
    - [Installation and Setup](#installation-and-setup)
  - [High-level Steps](#high-level-steps)
  - [Interactive Shell](#interactive-shell)
  - [djangorestframework](#djangorestframework)
  - [Authentication using Simple JWT](#authentication-using-simple-jwt)
    - [Views](#views)


### Installation and Setup
The following instructions are based on the official guide [here](https://docs.djangoproject.com/en/4.2/intro/tutorial01/).

```bash
pip install Django
django-admin startproject mysite
```

```bash
python manage.py runserver
```

To create an app:
```bash
python manage.py startapp polls
```

Database prepration:
```bash
# The migrate command looks at the INSTALLED_APPS setting 
# and creates any necessary database tables
python manage.py migrate

# By running makemigrations, you’re telling Django that you’ve made 
# some changes to your models and that you’d like the changes to 
# be stored as a migration.
python manage.py makemigrations polls
# python manage.py sqlmigrate polls 0001


# The migrate command takes all the migrations that haven’t been applied 
# and runs them against your database
python manage.py migrate
```

Access the site:
```
http://localhost:8000/polls
http://127.0.0.1:8000/admin
```

Create a superuser:
```bash
python manage.py createsuperuser
```

## High-level Steps

- Write a view for `polls` app
- Config `urls.py` in `polls`
- Point the root URLconf (`mysite/urls.py`) at the `polls.urls` module
- Run `python manage.py migrate`
- Create models
- Include the app in the project by adding a reference to its configuration class in the `INSTALLED_APPS`
- you’ve made some changes to your models and that you’d like the changes to be stored as a migration: `python manage.py makemigrations polls`
- Create model tables in your database: `python manage.py migrate`
- Create an admin user
- Make the `polls` app modifiable in the admin by editing `polls/admin.py`
- Write a view. A view serves a specific function and has a specific template
- Use class based views instead of function base views


## Interactive Shell
```bash
python manage.py shell
```

## djangorestframework
Django REST framework is a powerful and flexible toolkit for building Web APIs.
Helps with writing RESTful APIs and provides JSON parser, CRUD views, permissions, and serializers.

```bash
pip install djangorestframework

# Markdown support for the browsable API.
pip install markdown       
```
Once installed add `rest_framework` to the installed apps. Additionally in `urls.py` and `settings.py`:
```python
path('api-auth/', include('rest_framework.urls')),
```

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # Use Django's standard `django.contrib.auth` permissions,
        # or allow read-only access for unauthenticated users
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        # No authentication required (test only)
        # 'rest_framework.permissions.AllowAny' 
    ]
}
```
Then
- Define serializers `serializers.py`
- Define views `UserViewSet` and `GroupViewSet`


## Authentication using Simple JWT
```bash
pip install djangorestframework-simplejwt
```
You may follow the [official guide page](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html). The guide includes the following steps:
- Project Configuration (modify `settings.py`)
- In `urls.py` include routes for Simple JWT’s views
- To protect each view, use `authentication_classes` with `JWTAuthentication`. 


### Views
