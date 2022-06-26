from typing import Optional
from datetime import date
from uuid import UUID
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from fastapi import FastAPI

app = FastAPI()


class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)


class UserLogin(UserBase):
    passw: str = Field(..., min_length=8)


class User(UserBase):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    birth_date: Optional[date] = Field(default=None)


class Tw(BaseModel):
    pass


@app.get(path="/")
def index():
    return {"TW API": "Working"}
