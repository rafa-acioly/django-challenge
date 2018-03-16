# How to run:

## Virtual env configuration

1. `sudo pip install virtualenv`
2. git clone https://github.com/rafa-acioly/django-challenge.git
3. `virtualenv django-challenge/env`
4. `cd django-challenge/`
5. `source env/bin/activate`

## Init the configuration
Insite the `django-challenge` folder run on your terminal:

1. `pip install -r requirements.txt`
2. `python manage.py makemigrations api`
3. `python manage.py migrate`

## Create User Admin

Inside the challenge folder run the follow command:

```sh
python manage.py createsuperuser
```

this command will ask for a username, email and password that you will use to login into the admin area.

## Run Project

`python manage.py runserver`
