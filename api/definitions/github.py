import strawberry
from typing import List, Union, Set
import datetime


@strawberry.type
class GithubOverview:
    languages: List[Union[str, None]]
    commits: int
    forks: int
    stars: int
    watches: int
    contributors: int
    pull_requests: int
    issues: int


@strawberry.type
class GithubAnalyticsPerTime:
    commits: int
    forks: int
    stars: int
    pull_requests: int
    issues: int
    watches: int
    last_push_date_weekday: Union[str, None]
    last_push_date_day: Union[int, None]
    last_push_date: Union[datetime.datetime, None]


@strawberry.type
class GithubAnalyticsPerRepo:
    commits: int
    forks: int
    stars: int
    contributors: int
    pull_requests: int
    issues: int
    watches: int
    repo_name: str


@strawberry.type
class PerRepo:
    repo: List[GithubAnalyticsPerRepo]


@strawberry.type
class PerTime:
    repo: List[GithubAnalyticsPerTime]


@strawberry.type
class RepoRank:
    repo_id: str
    repo_rank: float


@strawberry.type
class AssetRank:
    asset_id: str
    asset_rank: float


@strawberry.type
class GitHubPageRank:
    repos_ranks: List[RepoRank]
    assets_ranks: List[AssetRank]
