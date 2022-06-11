from typing import List
from fastapi import status, HTTPException
import strawberry
from models import Twitter
from twitter import TwitterOverview, TwitterAnalytics 

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

# def customSum(element:list, mt:int)

@strawberry.type
class Query:
    @strawberry.field 
    async def twitterOverview(self, asaID:str) -> TwitterOverview:
        result = await Twitter.filter(asa_id=asaID).values()
        result = {key: [i[key] for i in result] for key in result[0]}
        result = AttrDict(result)

        return TwitterOverview(
            asaID = result['asa_id'][0],
            tweetTotal = len(result['tweet']),
            likeTotal = sum(result['likes']),
            retweetTotal = sum(result['retweets']),
            sentimentTotal = sum(result['sentiment_score'])
        )



    @strawberry.field
    async def twitterAnalytics(self, asaID:str, startDate:str = '2021-03-01', endDate:str = '2021-03-21', weekday: bool=False, hour: bool=False) -> TwitterAnalytics:
        
        
        result = await Twitter.filter(asa_id = asaID).filter(posted_at__range = [startDate, endDate]).values()
        result = {key: [i[key] for i in result] for key in result[0]}
        result = AttrDict(result)
        print(result.keys())
        print(result['hour'])
        return TwitterAnalytics(
            asaID = result['asa_id'][0],
            likesCount = result['likes'],
            retweetsCount = result['retweets'],
            sentimentScore = result['sentiment_score'],
            hour = result['hour'],
            weekday = result['dow']
            

        )

schema = strawberry.Schema(query = Query)



