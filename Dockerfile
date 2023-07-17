FROM swaggerapi/swagger-ui

ARG APISIX_ENV_HOST
ARG APISIX_ENV_PORT
ENV APISIX_HOST=$APISIX_ENV_HOST
ENV APISIX_PORT=$APISIX_ENV_PORT

# Fix envsubst when change env for openapi
ENV ref=\$ref

WORKDIR /

COPY openapi.yaml ./openapi_no_env.yaml

USER root

RUN apk update && apk upgrade

RUN /bin/sh -c "envsubst < openapi_no_env.yaml > openapi.yaml"
