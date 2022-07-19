from . import schema


def test_analytics_per_repo(client):
    async def get_analytics():
        query = """
    query MyQuery {
      githubAnalyticsPerepo(asaID: "ChoiceCoin", sortBy: "stars") {
        repo {
          commits
          contributors
          forks
          issues
          pullRequests
          repoName
          stars
          }
        }
      }
      """
        result = await schema.execute(
            query,
            variable_values={"asaID": "ChoiceCoin", "sortBy": "stars"},
        )
        return result

    result = client.portal.call(get_analytics)
    assert result.errors is None
    assert result.data["githubAnalyticsPerepo"] == {
        "repo": [
            {
                "commits": 234,
                "contributors": 34,
                "forks": 12,
                "issues": 123,
                "pullRequests": 12,
                "repoName": "repo1",
                "stars": 34,
            },
            {
                "commits": 234,
                "contributors": 34,
                "forks": 12,
                "issues": 123,
                "pullRequests": 12,
                "repoName": "repo2",
                "stars": 34,
            },
            {
                "commits": 234,
                "contributors": 34,
                "forks": 12,
                "issues": 123,
                "pullRequests": 12,
                "repoName": "repo3",
                "stars": 34,
            },
        ]
    }


def test_analytics_per_day(client):
    async def analytics_day():
        query = """
    query MyQuery {
      githubAnalyticsPertime(asaID: "ChoiceCoin", day: true, startDate: "2020-01-01") {
        repo {
          commits
          forks
          issues
          lpDay
          pullRequests
          watches
          stars
        }
      }
    }

    
    """
        result = await schema.execute(
            query,
            variable_values={
                "asaID": "ChoiceCoin",
                "day": True,
                "startDate": "2020-01-01",
            },
        )
        return result

    result = client.portal.call(analytics_day)
    assert result.errors is None
    assert result.data["githubAnalyticsPertime"] == {
        "repo": [
            {
                "commits": 234,
                "forks": 12,
                "issues": 123,
                "lpDay": 1,
                "pullRequests": 12,
                "watches": 45,
                "stars": 34,
            },
            {
                "commits": 234,
                "forks": 12,
                "issues": 123,
                "lpDay": 24,
                "pullRequests": 12,
                "watches": 45,
                "stars": 34,
            },
            {
                "commits": 234,
                "forks": 12,
                "issues": 123,
                "lpDay": 28,
                "pullRequests": 12,
                "watches": 45,
                "stars": 34,
            },
        ]
    }


def test_analytics_per_weekday(client):
    async def analytics_wkday():
        query = """
    query MyQuery {
       githubAnalyticsPertime(asaID: "ChoiceCoin", startDate: "2020-01-01", weekDay: true) {
          repo {
            commits
            forks
            issues
            lpDayOfWeek
            pullRequests
            watches
            stars
          }
        }
      }


    
    """
        result = await schema.execute(
            query,
            variable_values={
                "asaID": "ChoiceCoin",
                "weekDay": True,
                "startDate": "2020-01-01",
            },
        )
        return result

    result = client.portal.call(analytics_wkday)
    assert result.errors is None
    assert result.data["githubAnalyticsPertime"] == {
        "repo": [
            {
                "commits": 234,
                "forks": 12,
                "issues": 123,
                "lpDayOfWeek": "1",
                "pullRequests": 12,
                "watches": 45,
                "stars": 34,
            },
            {
                "commits": 468,
                "forks": 24,
                "issues": 246,
                "lpDayOfWeek": "4",
                "pullRequests": 24,
                "watches": 90,
                "stars": 68,
            },
        ]
    }


def test_overview(client):
    async def get_overview():
        query = """
    query MyQuery {
      githubOverview(asaID: "ChoiceCoin") {
        commits
        contributors
        forks
        languages
        pullRequests
        issues
        stars
        watches
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
    assert result.data["githubOverview"] == {
        "commits": 702,
        "contributors": 102,
        "forks": 36,
        "languages": ["python", "python", "python"],
        "pullRequests": 36,
        "issues": 369,
        "stars": 102,
        "watches": 135,
    }
