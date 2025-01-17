web: gunicorn complaintmgmtsys.wsgi:application --bind 127.0.0.1/:$PORT
#or works good with external database
web: python manage.py migrate && gunicorn complaintmgmtsys.wsgi