from fastapi import HTTPException

from fastapi import FastAPI, Depends
from fastapi.openapi.utils import get_openapi

from Model.Request.post_create_user import PostCreateUser
from Model.Request.post_user_login import PostUserLogin
from Repository.user_repository import UserRepository
from Service.UserService import create_user
from Service.auth_service import AuthService
from Utils.auth.utils import create_access_token, get_current_user

app = FastAPI()


@app.post("/auth/register")
async def register_user(payload: PostCreateUser):
    return create_user(username=payload.username, password=payload.password, email=payload.email)


@app.get("/auth/validate")
async def user_own(current_user: dict = Depends(get_current_user)):
    return current_user


@app.post("/auth/login")
async def login(payload: PostUserLogin):
    auth_service = AuthService()
    user_repo = UserRepository()
    if not auth_service.check_credentials(payload.username, payload.password):
        raise HTTPException(status_code=401, detail="Incorrect payload or inactive user")

    user = user_repo.get_by_username(payload.username)
    return {"token": create_access_token(user), "type": "bearer"}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FastAPI Boilerplate",
        version="1.0.0",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "bearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    }

    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"bearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
