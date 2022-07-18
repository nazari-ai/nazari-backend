from typing import Iterator
import asyncio

# test library
import pytest
from tortoise.contrib.test import finalizer, initializer
from fastapi.testclient import TestClient
from main import switch_to_test_mode, TORTOISE_ORM

switch_to_test_mode()
# Database
from .populate_db import (
    populate_twitter,
    populate_github,
    populate_comments,
    populate_post,
)
from main import app
import logging

## Database connection


DB_URL = "postgres://postgres:password@127.0.0.1:5432/test_{}"


@pytest.fixture(scope="session")
def event_loop() -> Iterator[asyncio.AbstractEventLoop]:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def client(event_loop: asyncio.BaseEventLoop) -> Iterator[TestClient]:
    initializer(TORTOISE_ORM["apps"]["models"]["models"], loop=event_loop)
    logging.info("Database Initialized")
    with TestClient(app) as c:
        yield c

    finalizer()


@pytest.fixture(scope="session")
def populate_db(client):
    client.portal.call(
        populate_twitter, populate_comments, populate_github, populate_post
    )
    logging.info("Database updated")
