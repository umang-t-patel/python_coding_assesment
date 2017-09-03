# Python Coding Assessment - Appointment Scheduler
A simple application to manage schedule

The project only need a single Python 3.6 with Django 1.11.4 version.

## Download and run app on local machine

### Clone the app on local machine

    git clone https://github.com/umang-t-patel/python_coding_assessment.git

### Run Appointment Scheduler app on local machine
1. To run this app on your local machine, you'll need a Python(3.6) set up, including Python, pip, and virtualenv
2. Create an isolated Python environment, and install django
    
    For windows,
 
        virtualenv env
        env\scripts\activate
        pip install -r requirements.txt
    
    For linux,
 
        virtualenv env
        source env/bin/activate
        pip install -r requirements.txt

3. Run the Django migrations to set up your models:

        python manage.py makemigrations coding_assessment_app
        python manage.py migrate

4. Now you can run the development web server:

        python manage.py runserver

5. To access the applications go to the URL <http://127.0.0.1:8000/>
