from datetime import datetime
from typing import Optional

from pydantic import Field

from Model.user import User


class UserFactory:
    """User factory"""

    @staticmethod
    def create(
        username: str,
        password: str,
        email: str,
        is_superuser: bool = False,
        id: int = None,
        is_active: bool = False,
        created_at: Optional[datetime] = Field(default=None),
        updated_at: Optional[datetime] = Field(default=None),
    ) -> User:
        """Creates a user"""
        return User(
            username=username,
            password=password,
            email=email,
            is_active=is_active,
            is_superuser=is_superuser,
            id=id,
            created_at=created_at,
            updated_at=updated_at,
        )
