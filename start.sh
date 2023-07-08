#!/bin/sh
chmod +x ./wait-for-it.sh
./wait-for-it.sh 0.0.0.0:5001 --timeout=5
alembic upgrade head
uvicorn main:app --host 0.0.0.0 --port 8000
