#!/bin/bash
source .env
echo $NODE_ENV

curl http://0.0.0.0:9180/apisix/admin/routes/1 \
-H 'X-API-KEY: edd1c9f034335f136f87ad84b625c8f1' -X PUT -i -d '
{
  "uri": "/users/info/\d+",
  "upstream": {
    "type": "roundrobin",
    "nodes": {
      "127.0.0.1:8001": 1
    }
  }
}'
