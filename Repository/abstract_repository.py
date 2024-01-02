import os
from contextlib import contextmanager
from typing import TypeVar

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker
from sqlmodel_repository import SQLModelEntity, Repository

ExampleEntity = TypeVar("ExampleEntity", bound=SQLModelEntity)


class AbstractRepository(Repository[ExampleEntity]):
    """Example base class for all repositories"""

    @contextmanager
    def get_session(self) -> Session:
        """Provides a session to work with"""
        engine = create_engine(
            os.getenv("DATABASE_URL"))
        session = sessionmaker(bind=engine)
        try:
            yield session()
            session().commit()
        except:
            session().rollback()
            raise
        finally:
            session().close()
