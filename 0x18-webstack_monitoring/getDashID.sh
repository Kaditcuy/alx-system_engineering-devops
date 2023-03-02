#!/bin/bash


API_KEY="your api key"
APP_KEY="your app key"
URL="https://api.datadoghq.com/api/v1/dashboard"


curl -X GET $URL \
  -H "Content-Type: application/json" \
  -H "DD-API-KEY: $API_KEY" \
  -H "DD-APPLICATION-KEY: $APP_KEY"
