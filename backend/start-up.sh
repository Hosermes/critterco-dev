#!/bin/bash



while true; do
    
    python3 manage.py migrate --no-input
    python3 manage.py collectstatic
    python3 manage.py runserver 0.0.0.0:8000
    sleep 5s
done