from uuid import uuid4
from dataclasses import dataclass


@dataclass
class UserEntity:
    id: uuid4
    name: str
    password: str
    email: str
