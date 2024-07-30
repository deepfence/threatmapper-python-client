from enum import Enum


class ModelCloudResourceCloudProvider(str, Enum):
    AWS = "aws"
    AZURE = "azure"
    GCP = "gcp"

    def __str__(self) -> str:
        return str(self.value)
