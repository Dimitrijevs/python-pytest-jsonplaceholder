from api.base_client import BaseClient

class UsersAPI(BaseClient):

    def get_all_users(self):
        return self.get("/users")

    def get_user(self, user_id: int):
        return self.get(f"/users/{user_id}")

    def create_user(self, data: dict):
        return self.post("/users", data=data)

    def put_user(self, user_id: int, data: dict):
        return self.put(f"/users/{user_id}", data=data)

    def patch_user(self, user_id: int, data: dict):
        return self.patch(f"/users/{user_id}", data=data)

    def delete_user(self, user_id: int):
        return self.delete(f"/users/{user_id}")

    def get_user_albums(self, user_id: int):
        return self.get(f"/users/{user_id}/albums")

    def get_user_todos(self, user_id: int):
        return self.get(f"/users/{user_id}/todos")

    def get_user_posts(self, user_id: int):
        return self.get(f"/users/{user_id}/posts")