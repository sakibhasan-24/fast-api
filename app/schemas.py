# 

from enum import Enum
from pydantic import BaseModel,Field
from typing import Optional

class IssueStatus(str,Enum):
    open = "Open"
    closed = "Closed"
    in_progress = "In Progress"


class issuePriority(str, Enum):
    low = "Low"
    medium = "Medium"
    high = "High"


class issueCreate(BaseModel):
    title:str=Field(min_length=3,max_length=50)
    description:str=Field(min_length=15,max_length=200)
    priority:issuePriority=issuePriority.medium

class issueUpdate(BaseModel):
    title:Optional[str]=Field(default=None, min_length=3,max_length=50)
    description:Optional[str]=Field(default=None,min_length=15,max_length=200)
    priority:Optional[issuePriority]=None
    status:Optional[IssueStatus]=None


class issueOut(BaseModel):
    id:int
    title:str
    description:str
    priority:issuePriority
    status:IssueStatus
    