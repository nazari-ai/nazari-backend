from . import schema


def test_analytics(client):
    async def get_analytics():
        query = """
        query MyQuery {
            redditAnalytics(asaID: "ChoiceCoin", startDate: "2020-01-01") {
                asaID
                numOfComments
                postId
                postText
                postTitle
                score
                sentimentScore
                more {
                    commentId
                    commentScore
                    commentSentimentScore
                    postId
                }
            }
        }
        """
        result = await schema.execute(
            query,
            variable_values={"asaID": "ChoiceCoin", "startDate": "2020-01-01"},
        )

        return result

    result = client.portal.call(get_analytics)

    assert result.errors is None
    assert result.data["redditAnalytics"] == [
        {
            "asaID": "ChoiceCoin",
            "numOfComments": 3,
            "postId": "3752125",
            "postText": "text for post 1",
            "postTitle": "post 1",
            "score": 35,
            "sentimentScore": 0.7,
            "more": [
                {
                    "commentId": "1005114",
                    "commentScore": 21,
                    "commentSentimentScore": 0.7,
                    "postId": "3752125",
                },
                {
                    "commentId": "1805475",
                    "commentScore": 11,
                    "commentSentimentScore": 0.65,
                    "postId": "3752125",
                },
                {
                    "commentId": "120024",
                    "commentScore": 21,
                    "commentSentimentScore": 0.65,
                    "postId": "3752125",
                },
            ],
        },
        {
            "asaID": "ChoiceCoin",
            "numOfComments": 2,
            "postId": "2569278",
            "postText": "text for post 2",
            "postTitle": "post 2",
            "score": 13,
            "sentimentScore": 0.3,
            "more": [
                {
                    "commentId": "8753656",
                    "commentScore": 11,
                    "commentSentimentScore": 0.7,
                    "postId": "2569278",
                },
                {
                    "commentId": "7189372",
                    "commentScore": 1,
                    "commentSentimentScore": 0.7,
                    "postId": "2569278",
                },
            ],
        },
    ]
