from enum import Enum


class ModelAddGenerativeAiBedrockIntegrationModelId(str, Enum):
    AI21_J2_MID_V1 = "ai21.j2-mid-v1"
    AI21_J2_ULTRA_V1 = "ai21.j2-ultra-v1"
    AMAZON_TITAN_TEXT_EXPRESS_V1 = "amazon.titan-text-express-v1"
    AMAZON_TITAN_TEXT_LITE_V1 = "amazon.titan-text-lite-v1"
    ANTHROPIC_CLAUDE_INSTANT_V1 = "anthropic.claude-instant-v1"
    ANTHROPIC_CLAUDE_V2 = "anthropic.claude-v2"
    COHERE_COMMAND_LIGHT_TEXT_V14 = "cohere.command-light-text-v14"
    COHERE_COMMAND_TEXT_V14 = "cohere.command-text-v14"
    META_LLAMA2_13B_CHAT_V1 = "meta.llama2-13b-chat-v1"

    def __str__(self) -> str:
        return str(self.value)
