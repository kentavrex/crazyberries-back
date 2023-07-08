"""Here will be stored variables which are related with app"""
import os

DATABASE_URL = os.environ.get("DATABASE_URL")
MINIO_CLIENT_ACCESS_KEY = os.environ.get("MINIO_CLIENT_ACCESS_KEY")
MINIO_CLIENT_SECRET_KEY = os.environ.get("MINIO_CLIENT_SECRET_KEY")
