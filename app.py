import pugsql
from dotenv import load_dotenv
import os
load_dotenv()

DB = os.getenv("DATABASE")
queries = pugsql.module('queries/')
queries.connect(DB)

queries.create_user({
    'first_name': "Dave",
    "last_name": "Edwards",
    "email": "Dave@test2.com",
    "phone": "01234567"})
