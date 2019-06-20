#!/usr/bin/env bash

# Add necessary permissions
chmod 777 /src/

gunicorn --reload -b 0.0.0.0:9000 app:api