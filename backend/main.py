from fastapi import FastAPI
from db import models
from db.database import engine
from routes import users, planer
app = FastAPI()


models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(planer.router)