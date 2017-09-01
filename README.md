# Python Coding Assesment
A simple application to manage schedule

## Install Required Packages

The project only need a single Python package "Django", it was built and
tested with Django 1.11.4 version. To install it use the following command:

    pip install -r requirements.txt

## Running the Application

Before running the application we need to create the needed DB tables:

    python manage.py migrate
    python manage.py makemigrations coding_assesment_app
    python manage.py migrate

Now you can run the development web server:

    python manage.py runserver

To access the applications go to the URL <http://127.0.0.1:8000/>
