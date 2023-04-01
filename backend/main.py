from fastapi import FastAPI
from db import models
from db.database import engine
from routes import users
app = FastAPI()


models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
