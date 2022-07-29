from tortoise.models import Model
from tortoise import fields


class ASA(Model):
    """
    ASA List & Descriptions
    """
    asset_id= fields.CharField(pk=True, max_length= 255)
    name= fields.CharField(max_length= 255)
    logo= name= fields.CharField(max_length= 255)
    unitname_1= fields.CharField(max_length= 255)
    unitname_2= fields.CharField(max_length= 255)
    reputation__pera= fields.CharField(max_length= 255)
    reputation__algoexplorer= fields.CharField(max_length= 255)
    score__algoexplorer= fields.IntField()
    description= fields.TextField()
    URL= name= fields.CharField(max_length= 255)
    usd_value= fields.FloatField()
    fraction_decimals= fields.IntField()
    total_supply= fields.CharField(max_length= 255)
    circ_supply=fields.CharField(max_length= 255)
    creator= fields.CharField(max_length= 255)
    category= fields.CharField(max_length= 255)
    twitter= fields.CharField(max_length= 255)
    telegram= fields.CharField(max_length= 255)
    discord= fields.CharField(max_length= 255)
    medium= fields.CharField(max_length= 255)
    reddit= fields.CharField(max_length= 255)
    github= fields.CharField(max_length= 255)

    class Meta:
        table= "asaTable"
    

class Twitter(Model):
    """
    Twitter model
    """

    tweet_id = fields.BigIntField(pk=True)
    tweet = fields.TextField()
    posted_at = fields.DatetimeField(auto_now_add=False)
    day_of_week = fields.IntField()
    day = fields.IntField()
    month = fields.IntField()
    year = fields.IntField()
    hour = fields.IntField()
    mins = fields.IntField()
    likes = fields.IntField()
    retweets = fields.IntField()
    sentiment_score = fields.FloatField()
    asa_id = fields.TextField()

    class Meta:
        table = "twitterTable"

    class PydanticMeta:
        exclude = ["asa_id"]


class RedditPostTable(Model):
    post_id = fields.CharField(pk=True, max_length=255)
    title = fields.TextField()
    text = fields.TextField()
    score = fields.IntField()
    num_of_comments = fields.IntField()
    time_created = fields.DatetimeField(auto_now_add=False)
    day_of_week = fields.IntField()
    day = fields.IntField()
    month = fields.IntField()
    year = fields.IntField()
    hr = fields.IntField()
    mins = fields.IntField()
    url = fields.TextField()
    sentiment_score = fields.FloatField()
    asa_id = fields.TextField()

    class Meta:
        table = "redditPostTable"

    class PydanticMeta:
        exclude = ["asa_id"]


class RedditCommentTable(Model):
    comment_id = fields.CharField(pk=True, max_length=255)
    body = fields.TextField()
    score = fields.IntField()
    time_created = fields.DatetimeField(auto_now_add=False)
    day_of_week = fields.IntField()
    day = fields.IntField()
    month = fields.IntField()
    year = fields.IntField()
    hr = fields.IntField()
    mins = fields.IntField()
    sentiment_score = fields.FloatField()
    post = fields.ForeignKeyField("models.RedditPostTable", related_name="parent_id")

    class Meta:
        table = "redditCommentTable"


class Github(Model):
    repo_name = fields.CharField(pk=True, max_length=255)
    repo_desc = fields.TextField()
    date_created = fields.DatetimeField(auto_now_add=False)
    dc_day_of_week = fields.IntField()
    dc_day = fields.IntField()
    dc_month = fields.IntField()
    dc_year = fields.IntField()
    dc_hr = fields.IntField()
    dc_mins = fields.IntField()
    last_push_date = fields.DatetimeField(auto_now_add=False)
    lp_day_of_week = fields.CharField(max_length=255)
    lp_day = fields.IntField()
    lp_month = fields.IntField()
    lp_year = fields.IntField()
    lp_hr = fields.IntField()
    lp_mins = fields.IntField()
    language = fields.CharField(max_length=100)
    no_of_forks = fields.IntField()
    no_of_stars = fields.IntField()
    no_of_watches = fields.IntField()
    no_of_contributors = fields.IntField()
    no_of_commits = fields.IntField()
    issues = fields.IntField()
    pull_requests = fields.IntField()
    asa_id = fields.TextField()

    class Meta:
        table = "githubTable"

    class PydanticMeta:
        exclude = ["asa_id"]
