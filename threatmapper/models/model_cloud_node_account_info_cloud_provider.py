from enum import Enum


class ModelCloudNodeAccountInfoCloudProvider(str, Enum):
    AWS = "aws"
    AWS_ORG = "aws_org"
    AZURE = "azure"
    AZURE_ORG = "azure_org"
    GCP = "gcp"
    GCP_ORG = "gcp_org"

    def __str__(self) -> str:
        return str(self.value)
