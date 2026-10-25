from dataclasses import dataclass
from enum import Enum
from uuid import UUID
from datetime import datetime

@dataclass(frozen=True)
class User:
    user_id: UserId
    user_mail:UserEmail
    user_status: UserStatus
    creation_time: AccountCreation
    last_connection: ConnectionData | None


@dataclass(frozen=True)
class UserId:
    value: UUID

@dataclass(frozen=True)
class UserEmail:
    value: str


class UserStatus(Enum):
    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    DISABLED = "DISABLED"
    BLOCKED = "BLOCKED"

@dataclass(frozen=True)
class AccountCreation:
    time: datetime

@dataclass(frozen=True)
class ConnectionData:
    time: datetime

