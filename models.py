from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class RedditPostTable(Model):
    """
    Post model
    """

    post_id = fields.CharField(pk=True, max_length=255)
    title = fields.TextField()
    post_text = fields.TextField(null=True)
    score = fields.IntField()
    total_comments = fields.IntField()
    post_url = fields.TextField()
    time_created = fields.DatetimeField(auto_now_add=False)
    asa_id = fields.CharField(max_length=255)
    time_created_day = fields.IntField()
    time_created_month = fields.IntField()
    time_created_year = fields.IntField()
    time_created_weekday = fields.CharField(max_length=255)
    time_created_weekday_int = fields.IntField()
    time_created_hour = fields.IntField()
    time_created_minute = fields.IntField()
    sentiment_score = fields.FloatField()

    class Meta:
        table = "redditPostTable"

    class PydanticMeta:
        exclude = ["asa_id"]


Post_Pydantic = pydantic_model_creator(
    RedditPostTable,
    name="postsPydantic",
)


class Twitter(Model):
    """
    Twitter model
    """

    tweet_id = fields.BigIntField(pk=True)
    user_id = fields.BigIntField()
    text = fields.TextField()
    posted_at = fields.DatetimeField(auto_now_add=False)
    asa_id = fields.TextField()
    weekday_int = fields.IntField()
    day = fields.IntField()
    month = fields.IntField()
    year = fields.IntField()
    hour = fields.IntField()
    mins = fields.IntField()
    weekday = fields.TextField()
    likes = fields.IntField()
    retweets = fields.IntField()
    sentiment_score = fields.FloatField()

    class Meta:
        table = "twitterTable"

    class PydanticMeta:
        exclude = ["asa_id"]


Twitter_Pydantic = pydantic_model_creator(
    Twitter,
    name="twitterPydantic",
)


class RedditCommentTable(Model):
    comment_id = fields.CharField(pk=True, max_length=255)
    body = fields.TextField()
    score = fields.IntField()
    post = fields.ForeignKeyField("models.RedditPostTable", related_name="parent_id")
    created_at = fields.DatetimeField(auto_now_add=False)
    asa_id = fields.IntField()
    created_at_day = fields.IntField()
    created_at_month = fields.IntField()
    created_at_year = fields.IntField()
    created_at_weekday = fields.CharField(max_length=255)
    created_at_weekday_int = fields.IntField()
    created_at_hour = fields.IntField()
    created_at_minute = fields.IntField()
    sentiment_score = fields.FloatField()

    class Meta:
        table = "redditCommentTable"


Comment_Pydantic = pydantic_model_creator(
    RedditCommentTable,
    name="commentsPydantic",
)


class Github(Model):

    repo_name = fields.CharField(pk=True, max_length=255)
    repo_desc = fields.TextField(null=True)
    date_created = fields.DatetimeField(auto_now_add=False)
    last_push_date = fields.DatetimeField(auto_now_add=False)
    language = fields.TextField(null=True)
    no_of_forks = fields.IntField()
    no_of_stars = fields.IntField()
    no_of_watchers = fields.IntField()
    no_of_contributors = fields.IntField()
    no_of_commits = fields.IntField()
    issues = fields.IntField()
    pull_requests = fields.IntField()
    asa_id = fields.CharField(max_length=255)
    last_push_date_day = fields.IntField()
    last_push_date_month = fields.IntField()
    last_push_date_year = fields.IntField()
    last_push_date_weekday = fields.CharField(max_length=255)
    last_push_date_weekday_int = fields.IntField()
    last_push_date_hour = fields.IntField()
    last_push_date_minute = fields.IntField()
    date_created_day = fields.IntField()
    date_created_month = fields.IntField()
    date_created_year = fields.IntField()
    date_created_weekday = fields.CharField(max_length=255)
    date_created_weekday_int = fields.IntField()
    date_created_hour = fields.IntField()
    date_created_minute = fields.IntField()

    class Meta:
        table = "githubTable"

    class PydanticMeta:
        exclude = ["asa_id"]


Github_Pydantic = pydantic_model_creator(
    Github,
    name="githubPydantic",
)
