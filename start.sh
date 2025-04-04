#!/bin/bash

# Ensure script is executable
chmod +x start.sh

# Run FastAPI with Gunicorn using Uvicorn worker
gunicorn -w 1 -k uvicorn.workers.UvicornWorker backend:app --bind 0.0.0.0:8000
