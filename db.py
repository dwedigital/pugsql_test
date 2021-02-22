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

def find_user_id(id):
    user = queries.find_user_id(user_id = id)
    return(user)

def find_user_email(email):
    user = queries.find_user_email(user_email = email)
    return(user)

def find_user_phone(phone):
    user = queries.find_user_phone(user_phone = phone)
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
    return users

def get_count():
    count = queries.get_count()
    return count