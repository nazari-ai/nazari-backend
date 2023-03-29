import pytest
from datetime import datetime, timedelta
from api.definitions.twitter import Engagement, TweetStats
from models import Twitter
from api.resolvers.twitter_resolver import (
    get_tweet_lt,
    calculate_tweet_stats,
    get_tweets_stats,
    get_engagement_stats,
)


@pytest.fixture
def tweets():
    return [
        Twitter(
            asa_id="ASA_001",
            tweet_id=1,
            likes=10,
            retweets=20,
            posted_at=datetime(2022, 1, 1),
        ),
        Twitter(
            asa_id="ASA_001",
            tweet_id=2,
            likes=15,
            retweets=25,
            posted_at=datetime(2022, 1, 2),
        ),
        Twitter(
            asa_id="ASA_002",
            tweet_id=3,
            likes=5,
            retweets=15,
            posted_at=datetime(2022, 1, 1),
        ),
        Twitter(
            asa_id="ASA_002",
            tweet_id=4,
            likes=20,
            retweets=30,
            posted_at=datetime(2022, 1, 2),
        ),
        Twitter(
            asa_id="ASA_002",
            tweet_id=5,
            likes=30,
            retweets=40,
            posted_at=datetime(2022, 1, 3),
        ),
    ]


@pytest.mark.asyncio
async def test_get_tweet_lt(tweets):
    tweet_lt = await get_tweet_lt("ASA_001", "2022-01-01", "2022-01-02")
    assert tweet_lt == {"total_likes": 25, "total_retweets": 45}

    tweet_lt = await get_tweet_lt("ASA_001", "2022-01-03", "2022-01-04")
    assert tweet_lt == {}


# @pytest.mark.asyncio
# async def test_calculate_tweet_stats(tweets):
#     tweet = tweets[0]
#     tweet_lt = {"total_likes": 25, "total_retweets}
