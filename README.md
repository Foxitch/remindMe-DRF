## Installation and Setup ##
1. Clone the repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the required packages using the command pip install -r requirements.txt.
4. Set up the database by running the command python manage.py migrate.
5. Create a superuser using the command python manage.py createsuperuser.
6. Run the server using the command python manage.py runserver.

## Email Reminder ##
To enable email reminders, set up email settings in your Django settings file and run a celery worker using the command: 
```
celery -A remindMe worker -l info
```
The worker will periodically check for reminders that are due and send emails to the specified email addresses. Also, start Redis
