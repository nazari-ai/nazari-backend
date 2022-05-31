from typing import List, Optional, Generator

# test library
import pytest

# Database
from tortoise import Tortoise
from tortoise.contrib.test import finalizer, initializer
from models import Twitter, RedditCommentTable, RedditPostTable, Github

# API librabries/modules
import strawberry
from strawberry.asgi import GraphQL
from schema import Query

## Database connection


@pytest.fixture(scope="session", autouse=True)
def initialize_db(request):
    db_url = "postgres://postgres:@127.0.0.1:5432/test_{}"
    initializer(["models"], db_url=db_url)
    request.addfinalizer(finalizer)


## Populate database
@pytest.fixture(session="session")
def populate_twitter_db():
    Twitter.create(
        tweet_id=1213245124,
        tweet="Hey first tweet! Great!",
        posted_at="2021-03-01",
        likes=50,
        retweets=32,
        sentiment_score=0.7,
        asa_id="ChoiceCoin",
    )
    Twitter.create(
        tweet_id=1611245324,
        tweet="Hey! Second tweet!",
        posted_at="2021-03-06",
        likes=3,
        retweets=12,
        sentiment_score=0.4,
        asa_id="ChoiceCoin",
    )
    Twitter.create(
        tweet_id=1213245107,
        tweet="Third tweet! Just there",
        posted_at="2021-03-08",
        likes=5,
        retweets=45,
        sentiment_score=0.6,
        asa_id="ChoiceCoin",
    )
    Twitter.create(
        tweet_id=1213245891,
        tweet="Bad!!",
        posted_at="2021-03-15",
        likes=0,
        retweets=2,
        sentiment_score=0.3,
        asa_id="ChoiceCoin",
    )
    Twitter.create(
        tweet_id=4321451234,
        tweet="Bad, not good!",
        posted_at="2021-03-21",
        likes=0,
        retweets=4,
        sentiment_score=0.3,
        asa_id="ChoiceCoin",
    )


@pytest.fixture(scope="session")
def populate_post_table():
    RedditPostTable(
        post_id="auiwes4",
        title="Great Post",
        text="Heyy! Yo! This coin is to the moon !!",
        score=41,
        num_of_comments=5,
        time_created="2021-02-28",
        url="getpost.com",
        sentiment_score=0.8,
        asa_id="YieldlyFinance",
    )


@pytest.fixture(scope="session")
def populate_comment_table():
    RedditCommentTable(
        comment_id="iegedo3e8",
        body="comment 1",
        score=50,
        time_created="2021-03-01",
        sentiment_score=0.7,
        post_id="auiwes4",
    )
    RedditCommentTable(
        comment_id="iegeddfde8",
        body="comment 2",
        score=3,
        time_created="2021-03-06",
        sentiment_score=0.4,
        post_id="auiwes4",
    )
    RedditCommentTable(
        comment_id="iegd3e4548",
        body="comment 3",
        score=5,
        time_created="2021-03-08",
        sentiment_score=0.6,
        post_id="auiwes4",
    )
    RedditCommentTable(
        comment_id="i334edo3e8",
        body="comment 4",
        score=0,
        time_created="2021-03-15",
        sentiment_score=0.3,
        post_id="auiwes4",
    )
    RedditCommentTable(
        comment_id="iejjed3e8",
        body="comment 5",
        score=0,
        time_created="2021-03-21",
        sentiment_score=0.3,
        post_id="auiwes4",
    )


@pytest.fixture(scope="session")
def populate_github_table():
    Github(
        repo_name="repo1",
        repo_desc="desc 1",
        date_created="2020-07-05",
        last_push_date="2021-03-01",
        language="rust",
        no_of_forks=6,
        no_of_stars=24,
        no_of_watches=22,
        no_of_contributors=7,
        no_of_commits=14,
        issues=5,
        pull_requests=13,
        asa_id="YieldlyFinance",
    )
    Github(
        repo_name="repo2",
        repo_desc="desc 2",
        date_created="2021-02-01",
        last_push_date="2022-04-01",
        language="ruby",
        no_of_forks=3,
        no_of_stars=50,
        no_of_watches=12,
        no_of_contributors=4,
        no_of_commits=20,
        issues=11,
        pull_requests=41,
        asa_id="YieldlyFinance",
    )
    Github(
        repo_name="repo3",
        repo_desc="desc 3",
        date_created="2022-01-31",
        last_push_date="2022-04-31",
        language="scala",
        no_of_forks=3,
        no_of_stars=50,
        no_of_watches=18,
        no_of_contributors=20,
        no_of_commits=20,
        issues=5,
        pull_requests=17,
        asa_id="YieldlyFinance",
    )


## strawberry schema\
@pytest.fixture
def schema():
    schema = strawberry.Schema(query=Query)
    return schema
