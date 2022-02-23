from fastapi import FastAPI

from app.transport.rest import users

app = FastAPI()

app.include_router(users.router)
