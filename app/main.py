from fastapi import FastAPI
from app.models import User
app=FastAPI()

@app.get("/")
def root():
    return{
        "message":"Ai Doc Search API"
        }

@app.post("/user")
def create_user(user:User):
    return{
        "message":f"hello{user.name}",
        "age":user.age
    }