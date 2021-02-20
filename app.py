import pugsql
from faker import Faker

from dotenv import load_dotenv
import sys
import os

# load the .env file
load_dotenv()

# initiate faker to create dummy data
fake = Faker()

DB = os.getenv("DATABASE")
queries = pugsql.module('queries/')
queries.connect(DB)


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
    print(user)

def update_user(id, first_name):
    queries.update_user(user_id = id, first_name = first_name)

def delete_user(id):
    queries.delete_user(user_id = id)

if __name__ == "__main__":
    # user can add a number of users as an argument
    if sys.argv[1] == "create":

        create_users(int(sys.argv[2]))
    elif sys.argv[1] == "find":
        find_user(sys.argv[2])
    
    elif sys.argv[1] == "update":
        update_user(sys.argv[2], sys.argv[3])

    elif sys.argv[1] == "delete":
        delete_user(sys.argv[2])

    else:
        print("No option selected")

