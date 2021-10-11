
from deta import Deta

deta = Deta()

posts = deta.Base("posts")
users = deta.Base("users")


def create_user(name: str = "anonymous"):
    try:
        result = users.put({"name": name, "posts": []})
        return result
    except:
        return "Failed"


def create_post(text: str, image_link: str):
    try:
        posts.put({"text": text, "image": image_link, "likes": 0})
        return "Success"
    except:
        return "Failed"


def view_post(user_id: str, post_id: str, time_spent: int):
    try:
        users.update({"posts": users.util.append(
            {"post": post_id, "time": time_spent})}, user_id)
        return "Success"
    except:
        return "Failed"
