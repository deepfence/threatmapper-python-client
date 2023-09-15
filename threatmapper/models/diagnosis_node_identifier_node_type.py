from enum import Enum


class DiagnosisNodeIdentifierNodeType(str, Enum):
    CLUSTER = "cluster"
    HOST = "host"

    def __str__(self) -> str:
        return str(self.value)
