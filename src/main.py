#
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from api.events import router as event_router

# from api.events.routing import router as event_router

#


app: FastAPI = FastAPI()
app.include_router(event_router, prefix="/api/events")


# Root routes
@app.get(path="/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get(path="/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> dict[str, int | str | None]:
    return {"item_id": item_id, "q": q}


@app.get(path="/healthz")
def read_api_health() -> dict[str, str]:
    return {"status": "ok"}
