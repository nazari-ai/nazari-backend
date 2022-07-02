from fastapi import FastAPI
from strawberry.asgi import GraphQL
from api.query import schema
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()
DATABASE_URL= "postgres://postgres:precillieo@127.0.0.1:5432/test"

graphql_app= GraphQL(schema)
app.add_route('/dashboard', graphql_app)
app.add_websocket_route("/dashboard", graphql_app)

register_tortoise(app,
    db_url= DATABASE_URL,
    modules= {"models": ["models"]},
    generate_schemas= True,
    add_exception_handlers= True
    )

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        }
    },
}