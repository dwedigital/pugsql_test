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


if __name__ == "__main__":
    # user can add a number of users as an argument
    create_users(int(sys.argv[1]))
