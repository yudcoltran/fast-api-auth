from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routers import route

config = dotenv_values()

app = FastAPI()

#connect mongodb
@app.on_event("startup")
def startup():
    app.mongodb_client = MongoClient(config["MONGO_URL"])
    app.database = app.mongodb_client[config["MONGO_DB"]]

#close connect mongodb
@app.on_event("shutdown")
def shutdown():
    app.mongodb_client.close()

@app.get("/")
async def hello():
    return {"message": "Hello World"}

app.include_router(route.router)