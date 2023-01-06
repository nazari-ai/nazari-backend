from typing import List, Union
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
    sentimentPos: float
    sentimentNeg: float
    sentimentNeu: float


@strawberry.type
class Response:
    asaID: Union[str, None]
    results: List[TwitterAnalytics]
