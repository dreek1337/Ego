#!/bin/bash
# Add variables
source .env

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

# Block ports and accept host for blocked ports
export APISIX_CON_IP=$(sudo docker container inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $APISIX_HOST)

for service_port in $APISIX_USERS_MS_PORT $APISIX_AUTH_MS_PORT $APISIX_POSTS_MS_PORT
do
    sudo iptables -I DOCKER 1 -p tcp --dport $service_port -j DROP
    sudo iptables -I DOCKER 1 -p tcp --dport $service_port  -s $APISIX_CON_IP -j ACCEPT
done
