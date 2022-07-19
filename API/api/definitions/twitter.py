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


@strawberry.type
class TwitterAnalytics:
    # asaID: Union[str, None]
    posted_at: Union[datetime, None]
    day_of_week: Union[int, None]
    hour: Union[int, None]
    likes: int
    retweets: int
    sentiment: float


@strawberry.type
class Response:
    asaID: Union[str, None]
    results: List[TwitterAnalytics]
