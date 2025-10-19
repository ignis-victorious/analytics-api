#
#  Import LIBRARIES
from fastapi import APIRouter

#  Import FILES


router: APIRouter = APIRouter()


#  api/events/
@router.get(path="/")
def read_events() -> dict[str, list[int]]:
    return {"items": [1, 2, 3]}
