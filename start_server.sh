#!/bin/bash
python3 -m gunicorn --access-logfile - --workers 3 --bind unix:/home/ubuntu/diettracker/diettracker.sock diettracker.wsgi:application --preload
