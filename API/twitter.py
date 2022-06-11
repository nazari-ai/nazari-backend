from typing import List
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
    asaID: str 
    likesCount: List[int]
    retweetsCount: List[int]
    sentimentScore: List[float]
    weekday: List[str]
    hour: List[int]

    

