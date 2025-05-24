# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/hello")
def read_hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}
