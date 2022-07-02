##########---------Twitter-----------############
@pytest.mark.asyncio
async def test_twitter(schema,):

    query = """
    query TestQuery($asaID: String!, $startDate: Date, $endDate: Date, $weekDay: str, $hour: int) {
        twitter(asaID: $asaID, startDate: $startDate, endDate: $endDate, weekDay: $weekDay, hour: $hour){
            likes
            retweets
            createdTime
            sentimentScores

        }
    }
    """

    result = await schema.execute(
        query,
        variable_values={
            "asaID": "ChoiceCoin",
            "startDate": "2021-03-01",
            "endDate": "2021-03-21",
        },
    )

    assert result.errors is None
    assert result.data["twitter"] == [
        {
            "createdTime": [
                "2021-03-01",
                "2021-03-06",
                "2021-03-08",
                "2021-03-15",
                "2021-03-21",
            ],
            "retweets": [32, 12, 45, 2, 4],
            "likes": [50, 3, 5, 0, 0],
            "sentimentScores": [0.7, 0.4, 0.6, 0.3, 0.3],
        }
    ]


##########---------Reddit-----------############


@pytest.mark.asyncio
async def test_reddit(schema):

    query = """
    query TestQuery($asaID: String!, $startDate: Date, $endDate: Date, $weekDay: str, $hour: int) {
        reddit(asaID: $asaID, startDate: $startDate, endDate: $endDate, weekDay: $weekDay, hour: $hour){
            postID{
                text
                postUrl
                sentimentScore
                timeCreated
                comments{
                    SentimentScoreComments
                    upvotesComments
                    timeCreatedComments
                }
            }
        }
    }
    """

    result = await schema.execute(
        query,
        variable_values={
            "asaID": "YieldlyFinance",
            "startDate": "2021-03-01",
            "endDate": "2021-03-21",
        },
    )

    assert result.errors is None
    assert result.data["reddit"] == [
        {
            "jdnckosl": {
                "text": "Heyy! Yo! This coin is to the moon !!",
                "postUrl": "getpost.com",
                "sentimentScore": 0.8,
                "timeCreated": "2021-02-28",
                "score": 41,
                "comments": {
                    "SentimentScoreComments": [0.7, 0.4, 0.6, 0.3, 0.3],
                    "upvotesComments": [50, 3, 5, 0, 0],
                    "timeCreatedComments": [
                        "2021-03-01",
                        "2021-03-06",
                        "2021-03-08",
                        "2021-03-15",
                        "2021-03-21",
                    ],
                },
            }
        }
    ]


##########---------Github-----------############
@pytest.mark.asyncio
async def test_gtihub(schema):

    query = """
    query TestQuery($asaID: String!, $startDate: Date, $endDate: Date, $weekDay: str, $hour: int) {
        github(asaID: $asaID, startDate: $startDate, endDate: $endDate, weekDay: $weekDay, hour: $hour){
            dateCreated
            language
            commits
            forks
            stars
            watchers
            contributors
            pullRequests
            issues
            repos[
                repoName
                dateCreated
                lastPushDate
                language
                commits
                forks
                stars
                watchers
                contributors
                pullRequests
                issues
            ]
        }
    """

    result = await schema.execute(query, variable_values={"asaID": "YieldlyFinance"},)

    assert result.errors is None
    assert result.data["github"] == [
        {
            "dateCreated": "2020-07-01",
            "languages": ["rust", "ruby", "scala"],
            "commits": 54,
            "forks": 12,
            "stars": 124,
            "watchers": 52,
            "contributors": 31,
            "pullRequests": 71,
            "issues": 21,
            "repos": [
                {
                    "repoName": "repo1",
                    "dateCreated": "2020-07-05",
                    "lastPushDate": "2021-03-01",
                    "language": "rust",
                    "commits": 14,
                    "forks": 6,
                    "stars": 24,
                    "watchers": 22,
                    "contributors": 7,
                    "pullRequests": 13,
                    "issues": 5,
                },
                {
                    "repoName": "repo2",
                    "dateCreated": "2021-02-01",
                    "lastPushDate": "2022-04-01",
                    "language": "ruby",
                    "commits": 20,
                    "forks": 3,
                    "stars": 50,
                    "watchers": 12,
                    "contributors": 4,
                    "pullRequests": 41,
                    "issues": 11,
                },
                {
                    "repoName": "repo3",
                    "dateCreated": "2022-01-31",
                    "lastPushDate": "2022-04-31",
                    "language": "scala",
                    "commits": 20,
                    "forks": 3,
                    "stars": 50,
                    "watchers": 18,
                    "contributors": 20,
                    "pullRequests": 17,
                    "issues": 5,
                },
            ],
        }
    ]
