import pugsql
from faker import Faker

from dotenv import load_dotenv
import os

# load the .env file
load_dotenv()

# initiate faker to create dummy data
fake = Faker()

DB = os.getenv("DATABASE")
queries = pugsql.module('queries/')
queries.connect(DB)

def create_user(
    title,
    first_name,
    last_name,
    email,
    phone):
    user = queries.create_user({
        "title": title,
        'first_name': first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone})
    return user

def create_users(qty):
    for i in range(qty):
        queries.create_user({
            "title": fake.prefix(),
            'first_name': fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "phone": fake.phone_number()})

def find_user(id):
    user = queries.find_user(user_id = id)
    return(user)

def update_user(id,
title,
first_name,
last_name,
email,
phone):
    queries.update_user(
        user_id = id, 
        title = title,
        first_name = first_name,
        last_name =last_name,
        email = email,
        phone = phone)

def delete_user(id):
    queries.delete_user(user_id = id)

def get_users():
    users =  queries.get_users()
    print(users)
    return users