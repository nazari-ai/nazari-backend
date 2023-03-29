import datetime
import math
from typing import List, Optional

from tortoise.functions import Sum
from tortoise.expressions import Subquery

from api.definitions.twitter import Engagement, TweetStats
from models import AssetTable, Twitter


async def get_tweet_lt(asaID: str, startDate: str, endDate: str) -> dict:
    tweet_lt = (
        await Twitter.filter(asa_id=asaID, posted_at__range=[startDate, endDate])
        .annotate(total_likes=Sum("likes"), total_retweets=Sum("retweets"))
        .values("total_likes", "total_retweets")
    )

    return tweet_lt[0] or {}


async def calculate_tweet_stats(tweet, tweet_lt) -> dict:
    prf = (
        tweet.retweets / tweet_lt["total_retweets"]
        if tweet_lt.get("total_retweets", 0) > 0
        else 0
    )
    plf = (
        tweet.likes / tweet_lt["total_likes"]
        if tweet_lt.get("total_likes", 0) > 0
        else 0
    )
    pr = (math.log2(1 + plf) * prf) * 100
    return {
        "tweet_id": tweet.tweet_id,
        "prf": prf,
        "plf": plf,
        "pr": pr,
        "total_retweets": tweet.retweets,
        "total_likes": tweet.likes,
    }


async def get_tweets_stats(
    asaID: str,
    startDate: str = None,
    endDate: str = None,
    filter_by: str = "pr",
) -> TweetStats:
    if startDate is None:
        endDate = datetime.datetime.utcnow()
        startDate = endDate - datetime.timedelta(days=7)

    # Query the database for all tweets and their corresponding likes and retweets
    tweets = await Twitter.filter(asa_id=asaID, posted_at__range=[startDate, endDate])

    # Get the total number of likes and retweets for all tweets
    tweet_lt = await get_tweet_lt(asaID, startDate, endDate)

    if not tweets:
        return None, None

    tweet_stats = [await calculate_tweet_stats(tweet, tweet_lt) for tweet in tweets]

    if filter_by == "plf":
        sorted_tweet_stats = sorted(tweet_stats, key=lambda x: x["plf"], reverse=True)
    elif filter_by == "prf":
        sorted_tweet_stats = sorted(tweet_stats, key=lambda x: x["prf"], reverse=True)
    else:
        sorted_tweet_stats = sorted(tweet_stats, key=lambda x: x["pr"], reverse=True)

    most_engaged_tweet = sorted_tweet_stats[0]

    return (
        TweetStats(
            tweet_id=most_engaged_tweet["tweet_id"],
            prf=most_engaged_tweet["prf"],
            plf=most_engaged_tweet["plf"],
            pr=most_engaged_tweet["pr"],
            total_retweets=most_engaged_tweet["total_retweets"],
            total_likes=most_engaged_tweet["total_likes"],
            total_tweets=len(tweets),
        ),
        tweet_lt,
    )


async def get_engagement_stats(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    filter_by: str = "pr",
) -> List[Engagement]:
    assets = await AssetTable.all().values(
        "asset_id", "name", "logo", "total_supply", "circ_supply", "available"
    )
    engagement_stats = []
    for asset in assets:
        tweet_stats, tweet_lt = await get_tweets_stats(
            asset["asset_id"], start_date, end_date, filter_by
        )

        if tweet_stats is None:
            continue

        engagement_stats.append(
            Engagement(
                name=asset["name"],
                logo=asset["logo"],
                total_supply=asset["total_supply"],
                available=asset["available"],
                circ_supply=asset["circ_supply"],
                top_tweet_id=tweet_stats.tweet_id,
                top_tweet_likes=tweet_stats.total_likes,
                top_tweet_retweets=tweet_stats.total_retweets,
                asa_total_likes=tweet_lt["total_likes"],
                asa_total_retweets=tweet_lt["total_retweets"],
                total_tweets=tweet_stats.total_tweets,
                total_followers=0,  # dummy value i.e not from database
                total_mentions=0,  # dummy value i.e not from database
                plf=tweet_stats.plf,
                prf=tweet_stats.prf,
                pr=tweet_stats.pr,
            )
        )

    if filter_by == "plf":
        sorted_engagement_stats = sorted(
            engagement_stats, key=lambda x: x.plf, reverse=True
        )
    elif filter_by == "prf":
        sorted_engagement_stats = sorted(
            engagement_stats, key=lambda x: x.prf, reverse=True
        )
    else:
        sorted_engagement_stats = sorted(
            engagement_stats, key=lambda x: x.pr, reverse=True
        )

    return sorted_engagement_stats
