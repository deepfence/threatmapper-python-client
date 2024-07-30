from enum import Enum


class ModelSecretLevel(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    LOW = "low"
    MEDIUM = "medium"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
