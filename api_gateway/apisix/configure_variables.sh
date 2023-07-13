#!/bin/bash

envsubst < /usr/local/apisix/conf/apisix.yaml > /usr/local/apisix/conf/apisix2.yaml

mv /usr/local/apisix/conf/apisix2.yaml /usr/local/apisix/conf/apisix.yaml
