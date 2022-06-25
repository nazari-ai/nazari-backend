from typing import List, Dict, Any
from fastapi import status, HTTPException
import strawberry
from models import RedditPostTable, RedditCommentTable
from reddit import RedditPostSchema, RedditCommentSchema


@strawberry.type
class Query:
    @strawberry.field
    async def redditAnalytics(
        self,
        asaID: str,
        startDate: str = "2022-04-28",  # to be modified into datetime.now() in production
        endDate: str = "2021-02-22",  # to be modified using timedelta of 7 days
    ) -> List[RedditPostSchema]:
        """Resolver to generate a list of reddit posts with each post's comments nested in the schema.
        params
            asaID
            startDate   default = datetime.datetime.now
            endDate     default = datetime.datetime.now - datetime.timedelta(7)
        returns
            List[RedditPostSchema]
        """

        post_table = (
            await RedditPostTable.filter(asa_id=asaID)
            .filter(time_created__range=[startDate, endDate])
            .values()
        )

        async def reddit_table_to_json(post_data: RedditPostTable) -> RedditPostSchema:
            """Function to retrieve the JSON representation of each reddit post and its comments.
            params
                post_data   raw data of each reddit post from the redditPostTable
            returns
                RedditPostSchema    the JSON representation of each reddit post as needed by the client.
            """
            comment_table = await RedditCommentTable.filter(
                post_id=post_data["post_id"]
            ).values()
            comment_data = [
                RedditCommentSchema(
                    comment_id=comment["comment_id"],
                    comment_score=comment["score"],
                    comment_sentiment_score=comment["sentiment_score"],
                    post_id=comment["post_id"],
                )
                for comment in comment_table
            ]

            post_json = RedditPostSchema(
                asaID=post_data["asa_id"],
                post_id=post_data["post_id"],
                post_title=post_data["title"],
                post_text=post_data["text"],
                score=post_data["score"],
                sentimentScore=post_data["sentiment_score"],
                more=comment_data,
            )
            return post_json

        return [reddit_table_to_json(post_data) for post_data in post_table]


schema = strawberry.Schema(query=Query)
