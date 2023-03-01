#!/bin/bash

API_KEY="184a88d75fdad14d5f0d88b27fba0681"
APP_KEY="45b91e338f42b2c566285b75346cb66a5bd33437"
URL="https://api.datadoghq.com/api/v1/hosts"

curl -X GET $URL \
  -H "Content-Type: application/json" \
  -H "DD-API-KEY: $API_KEY" \
  -H "DD-APPLICATION-KEY: $APP_KEY"
