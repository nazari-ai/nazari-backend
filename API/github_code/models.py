from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

class github(Model):
    repo_name = fields.CharField(pk=True, max_length=255)
    repo_desc = fields.TextField()
    date_created = fields.DatetimeField(auto_now_add=False)
    dc_day_of_week = fields.IntField()
    dc_day = fields.IntField()
    dc_month = fields.IntField()
    dc_year = fields.IntField()
    dc_hr = fields.IntField()
    dc_mins = fields.IntField()
    last_push_date = fields.DatetimeField(auto_now_add=False)
    lp_day_of_week = fields.CharField(max_length=255)
    lp_day = fields.IntField()
    lp_month = fields.IntField()
    lp_year = fields.IntField()
    lp_hr = fields.IntField()
    lp_mins = fields.IntField()
    language = fields.CharField(max_length=100)
    no_of_forks = fields.IntField()
    no_of_stars = fields.IntField()
    no_of_watches = fields.IntField()
    no_of_contributors = fields.IntField()
    no_of_commits = fields.IntField()
    issues = fields.IntField()
    pull_requests = fields.IntField()
    asa_id = fields.TextField()

    class Meta:
        table = "githubTable"

    class PydanticMeta:
        exclude = ["asa_id"]
        
Github_Pydantic = pydantic_model_creator(github, name="githubPydantic",)


#class github(Model):
#    repo_name = fields.CharField(pk=True, max_length=255)
#    repo_desc = fields.TextField()
#    date_created = fields.DatetimeField(auto_now_add=False)
#    last_push_date = fields.DatetimeField(auto_now_add=False)
#    language = fields.CharField(max_length=100)
#    no_of_forks = fields.IntField()
#    no_of_stars = fields.IntField()
#    no_of_watches = fields.IntField()
#    no_of_contributors = fields.IntField()
#    no_of_commits = fields.IntField()
#    issues = fields.IntField()
#    pull_requests = fields.IntField()
#    asa_id = fields.TextField()
#    weekday= fields.CharField(max_length=100)
#    dow= fields.IntField()

#    class Meta:
#        table= "githubTable"

#    class PydanticMeta:
#        exclude = ['asa_id']

#Github_Pydantic = pydantic_model_creator(github, name= "githubPydantic", )