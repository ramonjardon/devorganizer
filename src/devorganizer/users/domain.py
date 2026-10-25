from dataclasses import dataclass
from uuid import UUID
from datetime import datetime

@dataclass
class User:
    id: UUID
    mail:str
    active: bool
    creation_time: datetime
    last_connection: datetime


class Role: