#!/usr/bin/env bash

DJANGO_API_DOCKER_NAME=docker_api_1

docker exec -ti "${DJANGO_API_DOCKER_NAME}" python manage.py "${@}"
