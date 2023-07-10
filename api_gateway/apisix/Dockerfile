FROM apache/apisix:${APISIX_IMAGE_TAG:-3.4.0-debian}

# Copy custom config.yaml
COPY conf/config.yaml /usr/local/apisix/conf/config.yaml

# Copy custom routers_settings.sh for standalone mode
COPY routers_settings.sh .
