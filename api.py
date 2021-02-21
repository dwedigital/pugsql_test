from fastapi import FastAPI
import db
import models
app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = db.find_user(user_id)
    print(user)
    return {"user":user}

@app.get("/users/")
def get_users():
    users = db.get_users()
    return {users}

@app.post("/users/")
async def create_user(user: models.User):
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
    updated_user = db.find_user(user_id)
    return {"status": "updated","user":updated_user}
