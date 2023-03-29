import numpy as np

from api.definitions.github import AssetRank, GitHubPageRank, RepoRank
from models import Github


def mult_matrix(a, b):
    # Dot products
    if len(a[0]) != len(b):
        return None

    return np.dot(a, b)


async def get_github_page_rank() -> GitHubPageRank:
    repos = await Github.all()

    a = np.array([[0.1] * 6])

    repo_ids = []
    repo_activities = []

    for repo in repos:
        repo_ids.append(f"{repo.asa_id}/{repo.repo_name}")
        repo_activities.append(
            [
                repo.no_of_forks,
                repo.no_of_stars,
                repo.no_of_contributors,
                repo.pull_requests,
                repo.issues,
                repo.no_of_commits,
            ]
        )
    repo_activities = np.array(repo_activities).T / 100

    repo_rank = mult_matrix(a, repo_activities)[0]

    repo_ids_rank_mapping = [
        RepoRank(repo_id=k, repo_rank=v) for k, v in zip(repo_ids, repo_rank)
    ]

    sorted_repo_ids_rank_mapping = sorted(
        repo_ids_rank_mapping, key=lambda x: x.repo_rank, reverse=True
    )

    asset_rank = {}
    for i in repo_ids_rank_mapping:
        repo_id, rank = i.repo_id, i.repo_rank
        repo_name = repo_id.split("/")[0]

        asset_rank[repo_name] = asset_rank.get(repo_name, 0) + rank

    asset_ranks = [AssetRank(asset_id=k, asset_rank=v) for k, v in asset_rank.items()]

    sorted_asset_ranks = sorted(asset_ranks, key=lambda x: x.asset_rank, reverse=True)

    return GitHubPageRank(
        repos_ranks=sorted_repo_ids_rank_mapping, assets_ranks=sorted_asset_ranks
    )
