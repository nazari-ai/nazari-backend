from typing import List, Optional

import pytest

from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Twitter, Reddit_Comment_Table, Reddit_Post_Table, Github
import strawberry
from strawberry.asgi import GraphQL


## Database connection
Base = declarative_base()


@pytest.fixture(autouse=True)
def setup_database(Base):
    url = "postgresql+pg8000://postgres:password@localhost:8080/test_db"
    engine = create_engine(url, connect_args={"check_same_thread": False})
    db_session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

    db = db_session()
    Base.metadata.create_all(engine)

    return db


## Populate database
@pytest.fixture
def populate_twitter_db(db=setup_database):
    pass


## strawberry schema\
@pytest.fixture
def schema(Query):
    schema = strawberry.Schema(query=Query)
    return schema

