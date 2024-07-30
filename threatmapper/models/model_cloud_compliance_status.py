from enum import Enum


class ModelCloudComplianceStatus(str, Enum):
    ALARM = "alarm"
    DELETE = "delete"
    INFO = "info"
    OK = "ok"
    SKIP = "skip"

    def __str__(self) -> str:
        return str(self.value)
