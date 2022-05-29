##########---------Twitter-----------############
@pytest.mark.asyncio
async def test_twitter(schema,):

    query = """
    query TestQuery($asaID: String!, $startDate: Date, $endDate: Date) {
        twitter(asaID: $asaID, startDate: $startDate, endDate: $endDate){
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
            "created_time": [
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
    query TestQuery($asaID: String!, $startDate: Date, $endDate: Date) {
        reddit(asaID: $asaID, startDate: $startDate, endDate: $endDate){
            postID{
                text
                postUrl
                sentimentScores
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
                "sentimentScores": 0.8,
                "timeCreated": "2021-02-28",
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
    query TestQuery($asaID: String!) {
        github(asaID: $asaID){
            dateCreated
            language
            commits
            forks
            stars
            watchers
            contributors
            pullRequests
            issues
            repos{
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
            }
        }
    """

    result = await schema.execute(query, variable_values={"asaID": "YieldlyFinance"},)

    assert result.errors is None
    assert result.data["github"] == [
        {
            "dateCreated": "2020-07-01",
            "language": ["python"],
            "commits": 54,
            "forks": 12,
            "stars": 124,
            "watchers": 52,
            "contributors": 31,
            "pullRequests": 71,
            "issues": 21,
            "repos": {
                "repoName": ["repo1", "repo2", "repo3"],
                "dateCreated": ["2020-07-05", "2021-02-01", "2022-01-31"],
                "lastPushDate": ["2021-03-01", "2022-04-01", "2022-04-31"],
                "language": ["rust", "ruby", "scala"],
                "commits": [14, 20, 20],
                "forks": [6, 3, 3],
                "stars": [24, 50, 50],
                "watchers": [22, 12, 18],
                "contributors": [7, 4, 20],
                "pullRequests": [13, 41, 17],
                "issues": [5, 11, 5],
            },
        }
    ]
