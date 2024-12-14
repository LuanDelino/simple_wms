from uuid import uuid4
from sqlmodel import Field, SQLModel


class UserModel(SQLModel, table=True):
    __tablename__: str = 'wms_users'

    id: uuid4 = Field(default=uuid4(), primary_key=True)
    name: str
    password: str
    email: str
