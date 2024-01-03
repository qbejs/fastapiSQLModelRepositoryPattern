from pydantic import BaseModel


class PostUserLogin(BaseModel):
    username: str
    password: str