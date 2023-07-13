FROM apache/apisix:${APISIX_IMAGE_TAG:-3.4.0-debian}

WORKDIR /

COPY configure_variables.sh .
# Copy custom apisix.yaml for standalone mode
COPY conf/apisix.yaml /usr/local/apisix/conf/apisix.yaml
# Copy custom config.yaml
COPY conf/config.yaml /usr/local/apisix/conf/config.yaml

USER root

RUN apt-get update && apt-get install -y gettext

RUN chmod +x configure_variables.sh
