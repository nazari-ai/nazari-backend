import strawberry
from typing import List, Union
import datetime

@strawberry.type
class AsaData:
    asset_id:List[str]
    name:Union[List[str], None]
    logo:List[str]
    unitname_1:List[str]
    unitname_2:List[str]
    reputation_pera:List[str]
    reputation_algoexplorer:List[str]
    score_algoexplorer:List[int]
    description:List[str]
    URL:List[str]
    usd_value: List[float]
    fraction_decimals:List[int]
    total_supply:List[str]
    circ_supply: List[str]
    category:List[str]
    creator:List[str]
    twitter:Union[List[str], None]
    telegram:Union[List[str], None]
    discord:Union[List[str], None]
    medium:List[str]
    reddit:List[str]
    github:List[str]








