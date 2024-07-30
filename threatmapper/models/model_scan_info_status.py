from enum import Enum


class ModelScanInfoStatus(str, Enum):
    CANCELLED = "CANCELLED"
    CANCELLING = "CANCELLING"
    CANCEL_PENDING = "CANCEL_PENDING"
    COMPLETE = "COMPLETE"
    DELETE_PENDING = "DELETE_PENDING"
    ERROR = "ERROR"
    IN_PROGRESS = "IN_PROGRESS"
    STARTING = "STARTING"

    def __str__(self) -> str:
        return str(self.value)
