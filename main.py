import logging.config
from os import path

import uvicorn
from fastapi import FastAPI
from errors import HandleHTTPErrorsMiddleware

from endpoints import (
    user,
    product_card,
    comment,
    utility
)

log_file_path = path.join(path.dirname(path.abspath(__file__)), "log_config.ini")
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)

app = FastAPI(title="CrazyBerries")

# Middlewares
app.add_middleware(HandleHTTPErrorsMiddleware)

# CrazyBerries routes
app.include_router(product_card.router, prefix="/product_card", tags=["product_card"])
app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(comment.router, prefix="/comment", tags=["comment"])
app.include_router(utility.router, tags=["utility"])

if __name__ == "__main__":
    uvicorn.run(app, reload=True)
