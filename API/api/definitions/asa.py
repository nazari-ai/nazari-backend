from unittest import result
import strawberry
from typing import List, Union
import datetime
from strawberry.scalars import JSON



    

@strawberry.type
class AsaData:
    asset_id:str
    name:Union[str, None]
    logo:Union[str, None]
    unitname_1:Union[str, None]
    unitname_2:Union[str, None]
    reputation__pera:Union[str, None]
    reputation__algoexplorer:Union[str, None]
    score__algoexplorer:Union[int, None]
    description:Union[str, None]
    URL:Union[str, None]
    usd_value: Union[str, None]
    fraction_decimals:Union[int, None]
    total_supply:Union[str, None]
    circ_supply: Union[str, None]
    category:Union[str, None]
    creator:Union[str, None]
    twitter:Union[str, None]
    telegram:Union[str, None]
    discord:Union[str, None]
    medium:Union[str, None]
    reddit:Union[str, None]
    github:Union[str, None]
    available: bool

@strawberry.type
class asa_response:
    result: List[AsaData]

@strawberry.type
class AsaList:
    result: List[AsaData]
    # data: List["AsaData"]









