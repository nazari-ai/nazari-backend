from datetime import datetime
from typing import List, Optional, Union

import strawberry


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
    sentimentPos: float
    sentimentNeg: float
    sentimentNeu: float
    sentimentScore: Optional[float]


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
    logo: Optional[str]
    total_supply: Optional[str]
    available: Optional[str]
    circ_supply: Optional[str]
    plf: str
    prf: str
    pr: str
    top_tweet_id: str
    top_tweet_retweets: Optional[int]
    top_tweet_likes: Optional[int]
    asa_total_retweets: Optional[int]
    asa_total_likes: Optional[int]
    total_tweets: Optional[int]
    total_followers: Optional[int]
    total_mentions: Optional[int]


@strawberry.type
class EngagementResponse:
    results: List[Engagement]
