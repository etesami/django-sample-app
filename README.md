# Django Sample App
### Installation and Setup
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