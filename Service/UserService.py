from Model.Factory.user_factory import UserFactory
from Model.user import User
from Repository.user_repository import UserRepository
from Utils.auth.utils import get_hashed_password


def create_user(username: str, password: str, email: str) -> User:
    """Creates a user"""
    usr = UserFactory.create(
        username=username, password=get_hashed_password(password), email=email
    )
    user: User = UserRepository().create(usr)

    return user
