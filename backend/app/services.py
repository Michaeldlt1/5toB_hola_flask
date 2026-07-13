from typing import Dict, List


class UserService:
    def __init__(self, users: List[Dict[str, str]] | None = None):
        self.users = users or []

    def create_user(self, name: str, email: str, password: str) -> Dict[str, str]:
        user = {"name": name, "email": email, "password": password}
        self.users.append(user)
        return user

    def list_users(self) -> List[Dict[str, str]]:
        return self.users
