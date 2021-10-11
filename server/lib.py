
from deta import Deta

deta = Deta()

posts = deta.Base("posts")
users = deta.Base("users")


def create_user(name: str = "anonymous"):
    try:
        result = users.put({"name": name})
        return result
    except:
        return "Failed"


def create_post(text: str, image_link: str):
    try:
        posts.put({"text": text, "image": image_link})
        return "Success"
    except:
        return "Failed"
