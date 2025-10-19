#
#  Import LIBRARIES
from pydantic import BaseModel

#  Import FILES
#

"""
id
path
description
"""


class EventCreateSchema(BaseModel):
    page: str


class EventUpdateSchema(BaseModel):
    description: str


class EventSchema(BaseModel):
    id: int
    page: str | None = None
    description: str | None = None


class EventListSchema(BaseModel):
    results: list[EventSchema]
    count: int
