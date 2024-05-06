#!/bin/bash

# Send a POST request with a custom header
curl -X POST -H "X-Forwarded-For: 127.0.0.1" http://0.0.0.0:5000/catch_me

