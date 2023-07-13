#!/bin/bash

sudo docker compose -f posts_microservice/docker-compose.yaml up setup

sudo docker compose -f posts_microservice/docker-compose.yaml up -d

sudo docker compose -f auth_microservice/docker-compose.yaml up -d

sudo docker compose -f users_microservice/docker-compose.yaml up -d

sudo docker compose up -d

sudo docker exec apisix-con bash -c "./configure_variables.sh"
