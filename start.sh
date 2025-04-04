#!/bin/bash

# Ensure script is executable
chmod +x start.sh

# Render assigns a dynamic port
gunicorn -w 1 -k uvicorn.workers.UvicornWorker backend:app --bind 0.0.0.0:$PORT

