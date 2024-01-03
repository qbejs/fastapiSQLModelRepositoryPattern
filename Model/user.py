from typing import Optional

from pydantic.schema import datetime
from sqlmodel import Field
from sqlmodel_repository import SQLModelEntity


class User(SQLModelEntity, table=True):
    """User model"""

    __tablename__ = "users"

    id: int = Field(index=True, default=None, primary_key=True)
    username: str
    password: str
    email: str
    is_active: bool = False
    is_superuser: bool = False
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)
