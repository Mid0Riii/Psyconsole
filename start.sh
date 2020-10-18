#!/bin/sh

nohup gunicorn wsgi:application -c /home/ubuntu/psyconsole/gunicorn.py &
