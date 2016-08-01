#!/bin/bash
body='{
"request": {
  "message": "API triggered build", 
  "branch":"master"
}}'

curl -s -X POST \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "Travis-API-Version: 3" \
  -H "Authorization: token $TOASTER_CONTAINER_TOKEN" \
  -d "$body" \
  https://api.travis-ci.org/repo/crops%2Ftoaster-container/requests
