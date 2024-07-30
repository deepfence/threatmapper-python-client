from enum import Enum


class ModelComplianceStatus(str, Enum):
    INFO = "info"
    NOTE = "note"
    PASS = "pass"
    WARN = "warn"

    def __str__(self) -> str:
        return str(self.value)
