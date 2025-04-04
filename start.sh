#!/bin/bash

# Ensure the script is executable
chmod +x start.sh

# Run FastAPI with Gunicorn (use only 1 worker to avoid CPU overload)
gunicorn -w 1 -k uvicorn.workers.UvicornWorker backend:app --bind 0.0.0.0:8000
