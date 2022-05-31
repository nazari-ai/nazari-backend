from tortoise.models import Model
from tortoise import fields


class Twitter(Model):
    tweet_id = fields.BigIntField(pk=True)
    tweet = fields.TextField()
    posted_at = fields.DateTimeField(auto_now_add=False)
    likes = fields.IntegerField()
    retweets = fields.IntegerField()
    sentiment_score = fields.FloatField()
    asa_id = fields.TextField()

    class Meta:
        table = "twitterTable"


class RedditPostTable(Model):
    post_id = fields.CharField(pk=True)
    title = fields.TextField()
    text = fields.TextField()
    score = fields.IntegerField()
    num_of_comments = fields.IntegerField()
    time_created = fields.DateTimeField(auto_now_add=False)
    url = fields.TextField()
    sentiment_score = fields.FloatField()
    asa_id = fields.CharField()

    class Meta:
        table = "redditPostTable"


class RedditCommentTable(Model):
    comment_id = fields.CharField(pk=True)
    body = fields.TextField()
    score = fields.IntegerField()
    time_created = fields.DateTimeField(auto_now_add=False)
    sentiment_score = fields.FloatField()
    post_id = fields.ForeignKey("models.RedditPostTable", related_name="post_id")

    class Meta:
        table = "redditCommentTable"


class Github(Model):
    repo_name = fields.CharField(pk=True)
    repo_desc = fields.TextField()
    date_created = fields.DateTimeField(auto_now_add=False)
    last_date = fields.DateTimeField(auto_now_add=False)
    language = fields.CharField()
    no_of_forks = fields.IntegerField()
    no_of_stars = fields.IntegerField()
    no_of_watches = fields.IntegerField()
    no_of_contributors = fields.IntegerField()
    no_of_commits = fields.IntegerField()
    issues = fields.IntegerField()
    pull_requests = fields.IntegerField()

    class Meta:
        table = "githubTable"

