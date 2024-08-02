# learned from https://fastapi.tiangolo.com/python-types/#pydantic-models

from datetime import datetime
from pydantic import BaseModel
from typing import Annotated


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2024-08-02 12:14",
    "friends": [1, "2", b"3"],
}

user = User(**external_data)
print(user.id)


def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"
