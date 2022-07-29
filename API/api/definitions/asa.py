import strawberry
from typing import List, Union
import datetime

@strawberry.type
class ASAData:
    asset_id:str
    name:str
    logo:str
    unitname_1:str
    unitname_2:str
    reputation_pera:str
    reputation_algoexplorer:str
    score__algoexplorer:int
    description:str
    URL:str
    usd_value: float
    fraction_decimals:str
    total_supply:int
    circ_supply: int
    category:List[str]
    creator:str
    twitter:str
    telegram:str
    discord:str
    medium:str
    reddit:str
    github:str








