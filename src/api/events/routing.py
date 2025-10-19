#
#  Import LIBRARIES
from fastapi import APIRouter

#  Import FILES
from .schemas import EventListSchema, EventSchema

#

router: APIRouter = APIRouter()


# /api/events/
@router.get(path="/")
def read_events() -> EventListSchema:
    # a bunch of items in a
    return {"results": [{"id": 1}, {"id": 2}, {"id": 3}], "count": 3}


# L to chat, &K to generate

# @router.get(path="/")
# def read_events() -> dict[str, list[int]]:
#     # a bunch of items in a
#     return {"results": [1, 2, 3]}


@router.get(path="/{event_id}")
def get_event(event_id: int) -> EventSchema:
    # a single row
    return {"id": event_id}


# @router.get(path="/{event_id}")
# def get_event(event_id: int) -> dict[str, int]:
#     # a single row
#     return {"id": event_id}


# #  api/events/
# @router.get(path="/")
# def read_events() -> dict[str, list[int]]:
#     return {"items": [1, 2, 3]}
