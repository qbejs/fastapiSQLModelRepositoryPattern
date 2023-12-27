from Model.user import User
from Repository.abstract_repository import AbstractRepository


class UserRepository(AbstractRepository[User]):
    """User repository"""