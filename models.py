from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    title: str
    first_name: str
    last_name: str
    email: str
    phone: str