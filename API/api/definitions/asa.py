import strawberry
from typing import List, Union
import datetime

@strawberry.type
class AsaData:
    asset_id:str
    name:Union[List[str], None]
    logo:str
    unitname_1:str
    unitname_2:str
    reputation_pera:str
    reputation_algoexplorer:str
    score_algoexplorer:int
    description:str
    URL:List[str]
    usd_value: float
    fraction_decimals:str
    total_supply:int
    circ_supply: int
    category:List[str]
    creator:str
    twitter:Union[List[str], None]
    telegram:Union[List[str], None]
    discord:Union[List[str], None]
    medium:str
    reddit:str
    github:str








