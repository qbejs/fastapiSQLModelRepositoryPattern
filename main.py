
from fastapi import FastAPI, Depends

from Service.UserService import create_user
from Utils.auth.utils import create_access_token, get_current_user

app = FastAPI()


@app.get("/")
def root():
    user = create_user()
    return {"token": create_access_token(user)}


@app.get("/token")
async def say_hello(current_user: dict = Depends(get_current_user)):
    return {"message": "Protected endpoint", "logged_user": current_user}
