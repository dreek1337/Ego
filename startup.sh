#!/bin/bash

# Clean Docker
sudo docker stop $(sudo docker ps -qa)
sudo docker rm $(sudo docker ps -qa)
sudo docker rmi -f $(sudo docker images -qa)
sudo docker volume rm $(sudo docker volume ls -q)
sudo docker network rm $(sudo docker network ls -q)

# Configure Docker
sudo docker compose -f posts_microservice/docker-compose.yaml up setup
sudo docker compose -f posts_microservice/docker-compose.yaml up -d
sudo docker compose -f auth_microservice/docker-compose.yaml up -d
sudo docker compose -f users_microservice/docker-compose.yaml up -d
sudo docker compose up -d

# Start bash script into container
sudo docker exec apisix-con bash -c "./configure_variables.sh"
