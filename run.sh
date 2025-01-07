#!/bin/sh
set -e
gunicorn complaintmgmtsys.wsgi.application --log-file -