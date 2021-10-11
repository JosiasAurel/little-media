
from fastapi import Request, FastAPI

app = FastAPI()


@app.get("/")
async def _handle_root(req: Request):
    return {"msg": "It works super good..."}
