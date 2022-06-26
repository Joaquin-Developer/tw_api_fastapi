"""main.py tw_api_fastapi"""

from typing import Optional, List
from datetime import date, datetime
import json
from uuid import UUID
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from fastapi import FastAPI
from fastapi import Body
from fastapi import status

app = FastAPI()


class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)


class UserLogin(UserBase):
    passw: str = Field(..., min_length=8, max_length=64)


class User(UserBase):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    birth_date: Optional[date] = Field(default=None)


class UserRegister(User):
    passw: str = Field(..., min_length=8, max_length=64)


class Tw(BaseModel):
    tw_id: UUID = Field(...)
    content: str = Field(..., min_length=1, max_length=256)
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)


# Path Operations


@app.get(path="/")
def index():
    return {"TW API": "Working"}


## Users:


@app.post(
    path="/signup", response_model=User, status_code=status.HTTP_201_CREATED, summary="Register a User", tags=["Users"]
)
def signup(user: UserRegister = Body):
    """
    register a user in the app

    parameters:
        - Request body parameter
            - user: UserRegister

    Returns a json with the basic user information.
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    with open("data/users.json", "r+", encoding="utf-8") as file:
        results: List = json.loads(file.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        file.seek(0)
        file.write(json.dumps(results))
        return user


@app.post(path="/login", response_model=User, status_code=status.HTTP_200_OK, summary="Login a User", tags=["Users"])
def login():
    pass


@app.get(
    path="/users", response_model=List[User], status_code=status.HTTP_200_OK, summary="Get all users", tags=["Users"]
)
def get_all_users():
    pass


@app.get(
    path="/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK, summary="Get  a User", tags=["Users"]
)
def get_specific_user():
    pass


@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"],
)
def delete_user():
    pass


@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"],
)
def update_user():
    pass


## Tw:


@app.get(path="/", response_model=List[Tw], status_code=status.HTTP_200_OK, summary="Get all tw", tags=["Tw"])
def get_all_tw():
    return {"TW api": "working"}


@app.post(path="/post", response_model=Tw, status_code=status.HTTP_201_CREATED, summary="post a tw", tags=["Tw"])
def post_tw():
    pass


@app.get(path="/tw/{tw_id}", response_model=Tw, status_code=status.HTTP_200_OK, summary="Get a tw", tags=["Tw"])
def get_specific_tw():
    pass


@app.delete(
    path="/tw/{tw_id}/delete", response_model=Tw, status_code=status.HTTP_200_OK, summary="Delete a tw", tags=["Tw"]
)
def delete_tw():
    pass


@app.put(
    path="/tw/{tw_id}/update", response_model=Tw, status_code=status.HTTP_200_OK, summary="Update a tw", tags=["Tw"]
)
def update_tw():
    pass
