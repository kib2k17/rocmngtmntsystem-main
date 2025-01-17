web: gunicorn rocmngtmntsystem-main.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn rocmngtmntsystem-main.wsgi