#
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
#

app: FastAPI = FastAPI()


@app.get(path="/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get(path="/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> dict[str, int | str | None]:
    return {"item_id": item_id, "q": q}
