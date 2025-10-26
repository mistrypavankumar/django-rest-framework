# How to install and run django server

## Step-1

```
python -m venv venv
```

Activate venv and then install requirements

## Step-2

```
python install -r requirements.txt
```

## Step-3: use this when create or update models

```
python manage.py makemigrations
python manage.py migrate
```

## Step-4: To run the server

```
python manage.py runserver
```
