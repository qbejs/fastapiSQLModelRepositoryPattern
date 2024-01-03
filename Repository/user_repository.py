from datetime import datetime

from Model.user import User
from Repository.abstract_repository import AbstractRepository


class UserRepository(AbstractRepository[User]):
    """User repository"""

    def create(self, entity: User) -> User:
        with self.get_session() as session:
            entity.created_at = datetime.now()
            session.add(entity)
            session.commit()
            session.refresh(entity)
            return entity

    def get_by_username(self, username: str) -> User:
        with self.get_session() as session:
            return session.query(User).filter(User.username == username).first()
