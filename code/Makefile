.DEFAULT: help
.PHONY: help
help:


build:
	docker-compose -f ./.docker/docker-compose.yml --project-directory=.docker build

config:
	docker-compose -f ./.docker/docker-compose.yml --project-directory=.docker config

dev-run: build
	docker-compose -f ./.docker/docker-compose.yml --project-directory=.docker up

clean:
	docker-compose -f ./.docker/docker-compose.yml --project-directory=.docker rm
