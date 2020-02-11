#!/usr/bin/env bash

db_migrations() {
    python manage.py migrate
}

runserver() {
    python manage.py runserver 0.0.0.0:8000
}

case "${1}" in
     *)
       db_migrations
       runserver
       ;;
esac
