#!/bin/bash
cd /posts_microservice

sudo docker compose up setup

sudo docker compose up -d

cd ../auth_microservice

sudo docker compose up -d

cd ../users_microservice

sudo docker compose up -d


cd ../

sudo docker compose up -d

sudo docker exec apisix-con bash -c "configure_variables.sh"
