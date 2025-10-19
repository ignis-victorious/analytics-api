#
#  Import LIBRARIES
from fastapi import APIRouter

#  Import FILES
from .schemas import EventCreateSchema, EventListSchema, EventSchema, EventUpdateSchema

#

router: APIRouter = APIRouter()


# /api/events/ß
@router.get(path="/")
def read_events() -> EventListSchema:
    # a bunch of items in a
    return {"results": [{"id": 1}, {"id": 2}, {"id": 3}], "count": 3}


# create view
# POST(SEND DATA) /api/events/
@router.post(path="/")
def create_event(payload: EventCreateSchema) -> EventSchema:
    # a bunch of items in a table
    print("_________")
    print(type(payload))
    print(payload.page)
    data = payload.model_dump()
    return {"id": 123, **data}


@router.get(path="/{event_id}")
def get_event(event_id: int) -> EventSchema:
    # a single row
    return {"id": event_id}


# Update this data
# PUT /api/events/12
@router.put(path="/{event_id}")
def update_event(event_id: int, payload: EventUpdateSchema) -> EventSchema:
    print(type(payload))
    print(payload.description)
    data = payload.model_dump()
    # a single row
    return {"id": event_id, **data}
    # return {"id": event_id, "description": payload.description}


# @router.get(path="/{event_id}")
# def get_event(event_id: int) -> dict[str, int]:
#     # a single row
#     return {"id": event_id}


# #  api/events/
# @router.get(path="/")
# def read_events() -> dict[str, list[int]]:
#     return {"items": [1, 2, 3]}
