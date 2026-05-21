from pydantic import BaseModel

class PostComment(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str