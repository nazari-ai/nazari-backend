from . import schema


def test_overview(client):
    async def get_overview():
        query = """
        query MyQuery {
          twitterOverview(asaID: "ChoiceCoin") {
            asaID
            likeTotal
            retweetTotal
            sentimentTotal
            tweetTotal
            }
        }
        """
        result = await schema.execute(
            query,
            variable_values={
                "asaID": "ChoiceCoin",
            },
        )

        return result

    result = client.portal.call(get_overview)

    assert result.errors is None
    assert result.data["twitterOverview"] == {
        "asaID": "ChoiceCoin",
        "likeTotal": 69,
        "retweetTotal": 20,
        "sentimentTotal": 1.8000000000000003,
        "tweetTotal": 4,
    }


def test_analytics_weekday(client):
    async def get_analytics_wkday():
        query = """
        query MyQuery {
          twitterAnalytics(asaID: "ChoiceCoin", weekday: true, startDate: "2021-01-01") {
            asaID
            results {
              dayOfWeek
              likes
              retweets
              sentiment
              }
            }
          }
        """
        result = await schema.execute(
            query,
            variable_values={
                "asaID": "ChoiceCoin",
                "weekday": True,
                "startDate": "2021-01-01",
            },
        )

        return result

    result = client.portal.call(get_analytics_wkday)

    assert result.errors is None
    assert result.data["twitterAnalytics"] == {
        "asaID": "ChoiceCoin",
        "results": [
            {"dayOfWeek": 0, "likes": 22, "retweets": 3, "sentiment": 1},
            {"dayOfWeek": 4, "likes": 13, "retweets": 5, "sentiment": 0.1},
            {"dayOfWeek": 5, "likes": 34, "retweets": 12, "sentiment": 0.7},
        ],
    }


def test_analytics_hr(client):
    async def get_analytics_hr():
        query = """
        query MyQuery {
          twitterAnalytics(asaID: "ChoiceCoin", hour: true, startDate: "2021-01-01") {
            asaID
            results {
              hour
              likes
              retweets
              sentiment
              }
          }
        }
        """
        result = await schema.execute(
            query,
            variable_values={
                "asaID": "ChoiceCoin",
                "hour": True,
                "startDate": "2021-01-01",
            },
        )

        return result

    result = client.portal.call(get_analytics_hr)
    assert result.errors is None
    assert result.data["twitterAnalytics"] == {
        "asaID": "ChoiceCoin",
        "results": [
            {"hour": 8, "likes": 3, "retweets": 1, "sentiment": 0.35},
            {"hour": 10, "likes": 19, "retweets": 2, "sentiment": 0.65},
            {"hour": 14, "likes": 34, "retweets": 12, "sentiment": 0.7},
            {"hour": 17, "likes": 13, "retweets": 5, "sentiment": 0.1},
        ],
    }


def test_analytics(client):
    async def get_analytics():
        query = """
        query MyQuery {
          twitterAnalytics(asaID: "ChoiceCoin",  startDate: "2021-01-01") {
            asaID
            results {
              likes
              retweets
              sentiment
              postedAt
              }
            }
          }
        """
        result = await schema.execute(
            query,
            variable_values={"asaID": "ChoiceCoin", "startDate": "2021-01-01"},
        )

        return result

    result = client.portal.call(get_analytics)
    assert result.errors is None
    assert result.data["twitterAnalytics"] == {
        "asaID": "ChoiceCoin",
        "results": [
            {
                "likes": 34,
                "retweets": 12,
                "sentiment": 0.7,
                "postedAt": "2022-01-15T14:51:42+00:00",
            },
            {
                "likes": 19,
                "retweets": 2,
                "sentiment": 0.65,
                "postedAt": "2022-02-21T10:30:02+00:00",
            },
            {
                "likes": 3,
                "retweets": 1,
                "sentiment": 0.35,
                "postedAt": "2022-02-28T08:30:02+00:00",
            },
            {
                "likes": 13,
                "retweets": 5,
                "sentiment": 0.1,
                "postedAt": "2022-04-22T17:20:45+00:00",
            },
        ],
    }
