import os
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.asgi import GraphQL
from api.query import schema

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")

config={
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "database": DB_NAME,
                "host": DB_HOST,
                "password": DB_PASSWORD,
                "user": DB_USER,
                "port": DB_PORT
            }
        }
    },
    "apps": {
        "models": {
            "models": ["models"],
            "default_connection": "default",
        }
    }
}

def init(app: FastAPI):
    register_tortoise(
        app,
        config=config,
        modules={"models": ["models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )


def switch_to_test_mode():
    global TORTOISE_ORM, generate_schemas
    TORTOISE_ORM["connections"][
        "default"
    ] = "postgres://postgres:password@127.0.0.1:5432/test_{}"
    generate_schemas = True


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


init(app)

graphql_app = GraphQL(schema)
app.add_route("/analytics", graphql_app)
app.add_websocket_route("/analytics", graphql_app)
