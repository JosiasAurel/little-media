from lib import create_user, view_post, like_post
from fastapi import Request, FastAPI

app = FastAPI()


@app.get("/")
async def _handle_root(req: Request):
    return {"msg": "It works super good..."}


@app.post("/make-user")
async def handler_make_user(req: Request):
    body = await req.json()
    user_name = body.get("name", "anonymous")
    result = create_user(user_name)
    return result
