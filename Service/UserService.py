from Model.Factory.user_factory import UserFactory
from Model.user import User
from Repository.user_repository import UserRepository
from Utils.auth.utils import get_hashed_password


def create_user() -> User:
    """Creates a user"""
    usr = UserFactory.create("username", get_hashed_password("password"), "email")
    user: User = UserRepository().create(usr)

    return user