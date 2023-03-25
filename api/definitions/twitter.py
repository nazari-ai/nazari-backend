from typing import List, Optional, Union
import strawberry
from datetime import datetime


@strawberry.type
class TwitterOverview:
    asaID: str
    tweetTotal: int
    likeTotal: int
    retweetTotal: int
    sentimentTotal: float
    sentimentTotalPos: float
    sentimentTotalNeg: float
    sentimentTotalNeu: float


@strawberry.type
class TwitterAnalytics:
    posted_at: Union[datetime, None]
    weekday: Union[str, None]
    hour: Union[int, None]
    likes: int
    retweets: int
    sentiment_score: float
    sentimentPos: float
    sentimentNeg: float
    sentimentNeu: float


@strawberry.type
class Response:
    asaID: Union[str, None]
    results: List[TwitterAnalytics]


@strawberry.type
class TweetStats:
    tweet_id: str
    prf: Optional[float]
    plf: Optional[float]
    pr: Optional[float]
    total_retweets: Optional[int]
    total_likes: Optional[int]
    total_tweets: Optional[int]


@strawberry.type
class Engagement:
    name: str
    logo: str
    total_supply: str
    available: str
    circ_supply: str
    most_engaged_tweet: Optional[str]
    total_retweets: Optional[int]
    total_likes: Optional[int]
    total_tweets: Optional[int]
    total_followers: Optional[int]
    total_mentions: Optional[int]


@strawberry.type
class EngagementResponse:
    results: List[Engagement]
