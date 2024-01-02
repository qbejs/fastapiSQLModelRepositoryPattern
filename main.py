
from fastapi import FastAPI, Depends
from fastapi.openapi.utils import get_openapi

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


# Custom OpenAPI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FastAPI Boilerplate",
        version="1.0.0",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {"url": "URL_do_loga"}
    openapi_schema["components"]["securitySchemes"] = {
        "bearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    }

    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"bearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi