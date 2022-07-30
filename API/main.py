import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from api.query import schema


DATABASE_URL = "postgres://postgres:password@127.0.0.1:5432/asalytics"


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

init(app)

graphql_app = GraphQL(schema)
app.add_route("/analytics", graphql_app)
app.add_websocket_route("/analytics", graphql_app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
