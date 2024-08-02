from fastapi import FastAPI
import requests
from pydantic import BaseModel
from typing import Literal

app = FastAPI()


class Joke(BaseModel):
    category: Literal["Programming", "Miscellaneous", "Dark", "Pun", "Spooky"]


@app.get("/joke")
def get_joke(category: str | None = None):
    response = requests.get(f"https://v2.jokeapi.dev/joke/{category or 'Any'}")
    return response.json()
