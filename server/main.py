from lib import create_user, view_post, like_post
from fastapi import Request, FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def _handle_root(req: Request):
    return {"msg": "It works super good..."}


@app.post("/make-user")
async def handler_make_user(req: Request):
    body = await req.json()
    user_name = body.get("name", "anonymous")
    result = create_user(user_name)
    return {"msg": result}


@app.post("/view-post")
async def _handle_view_post(req: Request):
    body = await req.json()
    user = body.get("user")
    post = body.get("post")
    time_spent = body.get("time")
    result = view_post(user, post, time_spent)
    return {"msg": result}


@app.post("/like-post")
async def _handle_like_post(req: Request):
    body = await req.json()
    user = body.get("user")
    post = body.get("post")
    result = like_post(user, post)
    return {"msg": result}
