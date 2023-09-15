from enum import Enum


class ModelUserRole(str, Enum):
    ADMIN = "admin"
    READ_ONLY_USER = "read-only-user"
    STANDARD_USER = "standard-user"

    def __str__(self) -> str:
        return str(self.value)
