FROM apache/apisix:${APISIX_IMAGE_TAG:-3.4.0-debian}

ARG APISIX_ENV_USERS_MS_HOST
ARG APISIX_ENV_USERS_MS_PORT
ARG APISIX_ENV_AUTH_MS_HOST
ARG APISIX_ENV_AUTH_MS_PORT
ARG APISIX_ENV_POSTS_MS_HOST
ARG APISIX_ENV_POSTS_MS_PORT

ENV APISIX_USERS_MS_HOST=$APISIX_ENV_USERS_MS_HOST
ENV APISIX_USERS_MS_PORT=$APISIX_ENV_USERS_MS_PORT
ENV APISIX_AUTH_MS_HOST=$APISIX_ENV_AUTH_MS_HOST
ENV APISIX_AUTH_MS_PORT=$APISIX_ENV_AUTH_MS_PORT
ENV APISIX_POSTS_MS_HOST=$APISIX_ENV_POSTS_MS_HOST
ENV APISIX_POSTS_MS_PORT=$APISIX_ENV_POSTS_MS_PORT

WORKDIR /
# Copy custom apisix.yaml for standalone mode
COPY conf/apisix.yaml ./apisix_no_env.yaml
# Copy custom config.yaml
COPY conf/config.yaml /usr/local/apisix/conf/config.yaml

USER root

RUN apt-get install -y gettext

RUN /bin/sh -c "envsubst < apisix_no_env.yaml > /usr/local/apisix/conf/apisix.yaml"
