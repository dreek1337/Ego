#!/bin/bash

# Enable authentication
etcdctl user add root:rootpass

etcdctl auth enable

# Create user and role for apisix
etcdctl --user root:rootpass user add apisix:apisix
etcdctl --user root:rootpass role add apisix
etcdctl --user root:rootpass user grant-role apisix apisix

# Grant permissions to apisix role
etcdctl --user root:rootpass role grant-permission apisix readwrite /apisix/
