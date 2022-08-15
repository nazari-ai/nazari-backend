import strawberry
from typing import List, Optional


@strawberry.type
class AsaData:
    asset_id: str
    name: str
    logo: Optional[str]
    unitname_1: Optional[str]
    unitname_2: Optional[str]
    reputation__pera: str
    reputation__algoexplorer: str
    score__algoexplorer: int
    description: Optional[str]
    URL: Optional[str]
    usd_value: Optional[str]
    fraction_decimals: Optional[int]
    total_supply: Optional[str]
    circ_supply: Optional[str]
    category: Optional[str]
    creator: Optional[str]
    twitter: Optional[str]
    telegram: Optional[str]
    discord: Optional[str]
    medium: Optional[str]
    reddit: Optional[str]
    github: Optional[str]
    available: bool


@strawberry.type
class AsaResponse:
    result: List[AsaData]



@strawberry.type
class AsaList:
    result: List[AsaData]
