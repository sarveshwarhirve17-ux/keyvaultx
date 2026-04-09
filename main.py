from fastapi import FastAPI
from auth import generate_api_key

app = FastAPI()

@app.get("/")
def home():
    return{"message":"API is working"}

@app.post ("/generate-key")
def create_key():
    api_key = generate_api_key()
    return{
        "api_key":api_key, "status":"created"
    }
