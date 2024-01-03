from enum import Enum


class ModelGenerativeAiIntegrationCloudPostureRequestRemediationFormat(str, Enum):
    ALL = "all"
    CLI = "cli"
    PULUMI = "pulumi"
    TERRAFORM = "terraform"

    def __str__(self) -> str:
        return str(self.value)
