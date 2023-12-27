import os
from typing import TypeVar

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker
from sqlmodel_repository import SQLModelEntity, Repository

ExampleEntity = TypeVar("ExampleEntity", bound=SQLModelEntity)


class AbstractRepository(Repository[ExampleEntity]):
    """Example base class for all repositories"""

    def get_session(self) -> Session:
        """Provides a session to work with"""
        engine = create_engine(os.getenv("DATABASE_URL"))
        factory = sessionmaker(bind=engine)
        with factory() as session:
            try:
                yield session
                session.commit()
            except SQLAlchemyError as e:
                session.rollback()
                raise