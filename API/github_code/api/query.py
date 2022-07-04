from pandas import timedelta_range
import strawberry
import datetime
from tortoise.functions import Sum
from dacite import from_dict #to simply creation of dataclasses from dictionaries.
from models import Github_Pydantic, github
from api.github import PerRepo, PerTime, GithubAnalyticsPerTime, GithubOverview, GithubAnalyticsPerRepo

endDate= datetime.datetime.utcnow()  #contains the current local date and time 
startDate= endDate - datetime.timedelta(days=7) #contains 7 days from the current date and time


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


@strawberry.type
class Query:
    @strawberry.field
    async def github_overview(self, asaID: str) -> GithubOverview:
        """
        This resolver function generates the sum of each github activity data in relation
        to the typehints shown in the `GitHub Overview` schema.

        params : asaID
        returns : GithubOverview Schema
        """
        result = await github.filter(asa_id= asaID).values()
        result= AttrDict({key: [i[key] for i in result] for key in result[0]})

        return GithubOverview(
            commits=sum(result.no_of_commits),
            forks= sum(result.no_of_forks),
            stars=sum(result.no_of_stars),
            contributors=sum(result.no_of_contributors),
            pull_requests=sum(result.pull_requests),
            issues=sum(result.issues),
            watches= sum(result.no_of_watches),
            languages= result.language
            )



    @strawberry.field
    async def github_analytics_perepo(self, asaID:str, sortBy:str) -> PerRepo:
        """
        This function generates each github activity data per repository in relation
        to the typehints shown in the `PerRepo` schema.

        params:      asaID
                     sortBy: order the data by the specified activity(e.g forks, stars, pull_requests.)
        aggregations: To aggregate data from the DB site.
                      - Annotation of the QuerySet (sum of a total of 6 github activities).
                      - Grouping which applies on the entire columns by "Repository Name".
                      - Ordering by the specified `sortBy` params value.
        returns:      PerRepo Schema - the JSON representation of each github activity as needed by the client.
        """
        result= await github.filter(asa_id= asaID).\
            annotate(stars=Sum("no_of_stars"), forks=Sum("no_of_forks"),
            contributors= Sum("no_of_contributors"), commits= Sum("no_of_commits"),
            issues= Sum("issues"), pull_requests= Sum("pull_requests")).\
            group_by("repo_name").order_by("-" + str(sortBy)).\
            values("repo_name", "stars", "forks", "contributors", "commits", "issues", "pull_requests")

        result= [from_dict(data_class= GithubAnalyticsPerRepo, data=x)for x in result]
        return PerRepo(
            repo= result
        )


    @strawberry.field
    async def github_analytics_pertime(self, asaID:str, endDate:str = endDate, startDate:str =startDate, day:bool = False, weekDay:bool = False) -> PerTime:
        """
        This resolver function generates each github activity data per time (e.g weekday, day of the week) in relation
        to the typehints shown in the "PerTime" schema.

        params: asaID
                startDate: default = datetime.datetime.now
                endDate: default = datetime.datetime.now - datetime.timedelta(7)
                day: default = boolean-False
                weekday: default = boolean-False

        aggregations: To aggregate data from the DB site.
                      - Annotation of the QuerySet (sum of a total of 6 github activities).
                      - Grouping which applies on the entire columns by "weekday/day_of_week/last_push_date".
        
        returns: PerTime Schema
        """
        if weekDay and day:
            raise Exception("Error! Analyze Weekday or Day")
            
        elif weekDay:
            result = await github.filter(asa_id= asaID).\
            filter(last_push_date__range= [startDate, endDate]).\
            annotate(stars= Sum("no_of_stars"), forks= Sum("no_of_forks"), watches= Sum("no_of_watches"),
            commits= Sum("no_of_commits"), issues= Sum("issues"), pull_requests= Sum("pull_requests")).\
            group_by("lp_day_of_week").\
            values("lp_day_of_week", "stars", "forks", "commits", "issues", "pull_requests", "watches") 

        elif day:
            result = await github.filter(asa_id= asaID).\
            filter(last_push_date__range= [startDate, endDate]).\
            annotate(stars= Sum("no_of_stars"), forks= Sum("no_of_forks"), watches= Sum("no_of_watches"),
            commits= Sum("no_of_commits"), issues= Sum("issues"), pull_requests= Sum("pull_requests")).\
            group_by("lp_day").\
            values("lp_day", "stars", "forks", "commits", "issues", "pull_requests", "watches") 
        
        else:
            result = await github.filter(asa_id= asaID).filter(last_push_date__range= [startDate, endDate]).\
            annotate(stars= Sum("no_of_stars"), forks= Sum("no_of_forks"), watches= Sum("no_of_watches"),
            commits= Sum("no_of_commits"), issues= Sum("issues"), pull_requests= Sum("pull_requests")).\
            group_by("last_push_date").\
            values("last_push_date", "stars", "forks", "commits", "issues", "pull_requests", "watches") 

        print(result)
        result= [from_dict(data_class= GithubAnalyticsPerTime, data=x)for x in result]
        return PerTime(
            repo= result
            )
        

schema= strawberry.Schema(query= Query)




