from fastapi import FastAPI, HTTPException
import db
import models
app = FastAPI()

@app.get("/users/")
def get_users():
    users = db.get_users()
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = db.find_user_id(user_id)
    return {"user":user}


@app.post("/users/")
async def create_user(user: models.User):
    if (db.find_user_email(user.email)):
        raise HTTPException(status_code=400, detail="Email already registered")
    elif (db.find_user_phone(user.phone)):
        raise HTTPException(status_code=400, detail="Phone already registered")

    new_user = db.create_user(
    title = user.title,
    first_name = user.first_name,
    last_name = user.last_name,
    email = user.email,
    phone = user.phone)
    return {"user_id":new_user, "user":user}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    db.delete_user(user_id)
    return {"user_id":user_id,"status":"Deleted"}

@app.put("/users/{user_id}")
def update_user(user_id: int,user: models.User):
    db.update_user(user_id,user.title,user.first_name,user.last_name,user.email,user.phone)
    updated_user = db.find_user_id(user_id)
    return {"status": "updated","user":updated_user}
