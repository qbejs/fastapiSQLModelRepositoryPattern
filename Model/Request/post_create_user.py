from pydantic import BaseModel


class PostCreateUser(BaseModel):
    username: str
    password: str
    email: str