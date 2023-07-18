from pydantic import BaseModel, Field
import uuid
from typing import Union

class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "_id": "12345-678",
                "name": "alan",
                "email": "alan@gmail.com",
                "password":"alan123"
            }
        }

class UpdateUser(BaseModel):
    name: str | None
    email: str | None
    password: str | None
    class Config:
        schema_extra = {
            "example": {
                "name": "alan",
                "email": "alan@gmail.com",
                "password":"alan123"
            }
        }