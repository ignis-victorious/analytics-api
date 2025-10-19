#
#  Import LIBRARIES
from pydantic import BaseModel

#  Import FILES
#


class EventSchema(BaseModel):
    id: int


class EventListSchema(BaseModel):
    results: list[EventSchema]
    count: int
