import datetime
import math
from typing import List, Optional

from tortoise.functions import Sum

from api.definitions.reddit import RedditEngagement, RedditStats
from models import AssetTable, RedditPostTable


async def get_posts_cu(asaID: str, startDate: str, endDate: str) -> dict:
    posts_cu = (
        await RedditPostTable.filter(
            asa_id=asaID, time_created__range=[startDate, endDate]
        )
        .annotate(total_comments=Sum("total_comments"), total_upvotes=Sum("score"))
        .values("total_comments", "total_upvotes")
    )

    return posts_cu[0] or {}


async def calculate_post_stats(post, posts_cu) -> dict:
    pcf = post.total_comments / posts_cu["total_comments"]
    puf = post.score / posts_cu["total_upvotes"]
    pr = (math.log2(1 + pcf) * puf) * 100
    return {
        "post_id": post.post_id,
        "puf": puf,
        "pcf": pcf,
        "pr": pr,
    }


async def get_posts_stats(
    asaID: str,
    startDate: str = None,
    endDate: str = None,
    filter_by: str = "pr",
) -> RedditStats:
    if startDate is None:
        endDate = datetime.datetime.utcnow()
        startDate = endDate - datetime.timedelta(days=360)

    # Query the database for all posts and their corresponding likes and reposts
    posts = await RedditPostTable.filter(
        asa_id=asaID, time_created__range=[startDate, endDate]
    )

    if not posts:
        return None

    # Get the total number of likes and reposts for all posts
    posts_cu = await get_posts_cu(asaID, startDate, endDate)

    post_stats = [await calculate_post_stats(post, posts_cu) for post in posts]

    if filter_by == "pcf":
        sorted_post_stats = sorted(post_stats, key=lambda x: x["pcf"], reverse=True)
    elif filter_by == "puf":
        sorted_post_stats = sorted(post_stats, key=lambda x: x["puf"], reverse=True)
    else:
        sorted_post_stats = sorted(post_stats, key=lambda x: x["pr"], reverse=True)

    most_engaged_post = sorted_post_stats[0]

    return RedditStats(
        post_id=most_engaged_post["post_id"],
        puf=most_engaged_post["puf"],
        pcf=most_engaged_post["pcf"],
        pr=most_engaged_post["pr"],
        total_comments=posts_cu["total_comments"],
        total_upvotes=posts_cu["total_upvotes"],
        total_posts=len(posts),
    )


async def get_reddit_engagement_stats(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    filter_by: str = "pr",
) -> List[RedditEngagement]:
    assets = await AssetTable.all().values(
        "asset_id", "name", "logo", "total_supply", "circ_supply", "available"
    )

    engagement_stats = []
    for asset in assets:
        post_stats = await get_posts_stats(
            asset["asset_id"], start_date, end_date, filter_by
        )

        if not post_stats:
            continue

        engagement_stats.append(
            RedditEngagement(
                asa_id=asset["asset_id"],
                name=asset["name"],
                logo=asset["logo"],
                total_supply=asset["total_supply"],
                available=asset["available"],
                circ_supply=asset["circ_supply"],
                most_engaged_post=post_stats.post_id,
                total_comments=post_stats.total_comments,
                total_upvotes=post_stats.total_upvotes,
                total_posts=post_stats.total_posts,
            )
        )
    return engagement_stats
