# Django Sample App
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

### Views
