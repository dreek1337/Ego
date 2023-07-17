FROM swaggerapi/swagger-ui

ARG HOST_FOR_SWAGGER
ARG APISIX_ENV_PORT
ENV APISIX_HOST=$HOST_FOR_SWAGGER
ENV APISIX_PORT=$APISIX_ENV_PORT

# Fix envsubst when change env for openapi
ENV ref=\$ref

WORKDIR /

COPY openapi.yaml ./openapi_no_env.yaml

USER root

RUN apk update && apk add gettext

RUN /bin/sh -c "envsubst < openapi_no_env.yaml > openapi.yaml"
