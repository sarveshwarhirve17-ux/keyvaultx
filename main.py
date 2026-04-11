from fastapi import FastAPI
from auth import generate_api_key 

from database import engine , Base , sessionLocal
from models import APIkey 

Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.get("/")
def home():
    return{"message":"API is working"}



@app.post("/generate-key")
def create_key(): 
    db = sessionLocal()  #database connection

    api_key = generate_api_key()

    new_key = APIkey(key=api_key)

    db.add(new_key)   # add to db
    db.commit()       #save
    db.refresh(new_key)  # refresh

    db.close()

    return{
        "api_key": api_key,"status": "saved in database"
    }

@app.get("/get-keys")
def get_keys():
    db = sessionLocal()

    keys = db.query(APIkey).all()
    db.close()
    return keys
    
@app.delete("/delete-key/{id}")
def delete_key(id:int):
    db = sessionLocal()

    key = db.query(APIkey).filter(APIkey.id==id).first()

    if key:
        db.delete(key)
        db.commit()
        db.close()
        return{"message":"Deleted"}
    db.close()
    return{"message":"Not found"}    
