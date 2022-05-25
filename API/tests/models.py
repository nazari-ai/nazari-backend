from sqlalchemy import Column, DateTime, BigInteger, String, Integer, Float, ForeignKey
from conftest import Base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Twitter(Base):
    __tablename__ = "twitter"

    tweet_id = Column(BigInteger, primary_key=True)
    tweet = Column(String)
    posted_at = Column(DateTime)
    likes = Column(Integer)
    retweets = Column(Integer)
    sentiment_score = Column(Float)
    asa_id = Column(String)


class Reddit_Post_Table(Base):
    __tablename__ = "reddit_post_table"

    post_id = Column(String)
    title = Column(String)
    text = Column(String)
    score = Column(Integer)
    num_of_comments = Column(Integer)
    time_created = Column(DateTime)
    url = Column(String)
    sentiment_score = Column(Integer)

    comments = relationship("Reddit_Comment_Table")


class Reddit_Comment_Table(Base):
    __tablename__ = "reddit_comment_table"

    comment_id = Column(String)
    body = Column(String)
    score = Column(Integer)
    time_created = Column(DateTime)
    sentiment_score = Column(Float)
    post_id = Column(String, ForeignKey("reddit_post_table.post_id"))


class Github(Base):
    __tablename__ = "github"

    repo_name = Column(String, primary_key=True)
    repo_desc = Column(String)
    date_created = Column(DateTime)
    last_date = Column(DateTime)
    language = Column(String)
    no_of_forks = Column(Integer)
    no_of_stars = Column(Integer)
    no_of_watches = Column(Integer)
    no_of_contributors = Column(Integer)
    no_of_commits = Column(Integer)
    issues = Column(Integer)
    pull_requests = Column(Integer)
