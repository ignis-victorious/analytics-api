#
#  Import LIBRARIES
from fastapi import APIRouter

#  Import FILES
from .schemas import EventSchema

#

router: APIRouter = APIRouter()


# /api/events/
@router.get(path="/")
def read_events() -> dict[str, list[int]]:
    # a bunch of items in a
    return {"results": [1, 2, 3]}


@router.get(path="/{event_id}")
def get_event(event_id: EventSchema) -> EventSchema:
    # a single row
    return event_id


# @router.get(path="/{event_id}")
# def get_event(event_id: int) -> dict[str, int]:
#     # a single row
#     return {"id": event_id}


# #  api/events/
# @router.get(path="/")
# def read_events() -> dict[str, list[int]]:
#     return {"items": [1, 2, 3]}
