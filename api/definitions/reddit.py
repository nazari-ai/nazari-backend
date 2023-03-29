from typing import List, Optional, Union
import strawberry


@strawberry.type
class RedditPostSchema:
    asaID: str
    post_id: str
    post_title: str
    post_text: Union[str, None]
    num_of_comments: int
    score: int
    sentimentScore: float
    sentimentScorePos: float
    sentimentScoreNeg: float
    sentimentScoreNeu: float
    rank: int
    more: List["RedditCommentSchema"]


@strawberry.type
class RedditCommentSchema:
    comment_id: str
    comment_score: int
    comment_sentiment_score: float
    comment_sentiment_score_pos: float
    comment_sentiment_score_neg: float
    comment_sentiment_score_neu: float
    post_id: str


@strawberry.type
class RedditStats:
    post_id: str
    pcf: Optional[float]
    puf: Optional[float]
    pr: Optional[float]
    total_upvotes: Optional[int]
    total_comments: Optional[int]
    total_posts: Optional[int]


@strawberry.type
class RedditEngagement:
    asa_id: str
    name: str
    logo: Optional[str]
    total_supply: Optional[str]
    available: Optional[str]
    circ_supply: Optional[str]
    top_post_id: Optional[str]
    top_post_upvotes: Optional[int]
    top_post_comments: Optional[int]
    asa_total_comments: Optional[int]
    asa_total_upvotes: Optional[int]
    total_posts: Optional[int]
    puf: Optional[float]
    pcf: Optional[float]
    pr: Optional[float]


@strawberry.type
class RedditEngagementResponse:
    results: List[RedditEngagement]
