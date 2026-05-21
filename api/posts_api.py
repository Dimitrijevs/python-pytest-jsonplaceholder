from api.base_client import BaseClient

class PostsAPI(BaseClient):

    def get_all_posts(self):
        return self.get("/posts")

    def get_post(self, post_id: int):
        return self.get(f"/posts/{post_id}")

    def create_post(self, data: dict):
        return self.post("/posts", data=data)

    def put_post(self, post_id: int, data: dict):
        return self.put(f"/posts/{post_id}", data=data)

    def patch_post(self, post_id: int, data: dict):
        # data might be a title, I am using title
        # might be a body
        return self.patch(f"/posts/{post_id}", data=data)

    def delete_post(self, post_id: int):
        return self.delete(f"/posts/{post_id}")

    def get_post_comments(self, post_id: int):
        return self.get(f"/posts/{post_id}/comments")