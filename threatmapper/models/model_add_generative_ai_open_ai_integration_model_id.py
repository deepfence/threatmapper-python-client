from enum import Enum


class ModelAddGenerativeAiOpenAIIntegrationModelId(str, Enum):
    GPT_4 = "gpt-4"

    def __str__(self) -> str:
        return str(self.value)
