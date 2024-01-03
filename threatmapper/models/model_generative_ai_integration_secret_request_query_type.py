from enum import Enum


class ModelGenerativeAiIntegrationSecretRequestQueryType(str, Enum):
    REMEDIATION = "remediation"

    def __str__(self) -> str:
        return str(self.value)
