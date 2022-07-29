import os
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.asgi import GraphQL
from api.query import schema

# DATABASE_URL = os.environ["DATABASE_URL"]
DATABASE_URL = "postgres://postgres:password@127.0.0.1:5432/mock_v2"


def init(app: FastAPI):
    register_tortoise(
        app,
        db_url=DATABASE_URL,
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


TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["models"],
            "default_connection": "default",
        }
    },
}
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
