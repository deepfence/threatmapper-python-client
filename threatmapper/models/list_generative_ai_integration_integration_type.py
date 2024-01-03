from enum import Enum


class ListGenerativeAiIntegrationIntegrationType(str, Enum):
    AMAZON_BEDROCK = "amazon-bedrock"
    OPENAI = "openai"

    def __str__(self) -> str:
        return str(self.value)
