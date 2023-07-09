#!/bin/bash

# Set the etcd endpoint
export ETCDCTL_ENDPOINTS=http://127.0.0.1:2379

# Enable authentication
etcdctl user add root --interactive=false
etcdctl auth enable

# Create user and role for apisix
etcdctl user add apisix --interactive=false
etcdctl role add apisix
etcdctl user grant-role apisix apisix

# Grant permissions to apisix role
etcdctl role grant-permission apisix readwrite /apisix/
