from datetime import datetime

from Model.user import User
from Repository.abstract_repository import AbstractRepository


class UserRepository(AbstractRepository[User]):
    """User repository"""

    def create(self, entity: User) -> User:
        """Creates a user"""
        with self.get_session() as session:
            entity.created_at = datetime.now()
            session.add(entity)
            session.commit()
            session.refresh(entity)
            return entity
