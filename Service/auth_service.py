from Repository.user_repository import UserRepository
from Utils.auth.utils import verify_password


class AuthService:
    user_repository: UserRepository

    def __init__(self):
        self.user_repository = UserRepository()

    def check_credentials(self, username: str, password: str) -> bool:
        user = self.user_repository.get_by_username(username)

        if not user:
            return False

        if not user.is_active:
            return False

        if not verify_password(password, user.password):
            return False

        return True
