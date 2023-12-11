from enum import Enum


class DiagnosisNodeIdentifierNodeType(str, Enum):
    CLOUD_ACCOUNT = "cloud_account"
    CLUSTER = "cluster"
    HOST = "host"

    def __str__(self) -> str:
        return str(self.value)
