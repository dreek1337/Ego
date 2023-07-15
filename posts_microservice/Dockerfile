FROM python:3.11
WORKDIR /
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
USER root
RUN sudo apt-get update && sudo apt-get install iptables
RUN iptables -A INPUT -p tcp --dport $SITE_PORT -s $APISIX_HOST -j ACCEPT
RUN iptables -A INPUT -p tcp --dport $SITE_PORT -j DROP
