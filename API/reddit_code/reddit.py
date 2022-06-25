from typing import List, Dict, Any
import strawberry


@strawberry.type
class RedditPostSchema:
    asaID: str
    post_id: str
    post_title: str
    post_text: str
    score: int
    sentimentScore: float
    more: List["RedditCommentSchema"]


@strawberry.type
class RedditCommentSchema:
    comment_id: str
    comment_score: int
    comment_sentiment_score: float
    post_id: str
