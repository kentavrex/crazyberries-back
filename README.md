# crazyberries-back

## The backend service of project similar to the well-known Russian marketplace.

### For the program to work, you need
The **app.env** file containing the following options:
```
DATABASE_URL="url"
MINIO_CLIENT_ACCESS_KEY="login"
MINIO_CLIENT_SECRET_KEY="password"
```

## Used technologies
- Languages: Python3, Shell
- Frameworks: FastAPI
- Data storage: PostgreSQL database, MinIO S3 storage
- Alembic for migrations and Pydantic for validation
- SQLAlchemy ORM
- Docker
- Repository Pattern
