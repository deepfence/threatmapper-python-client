from enum import Enum


class ModelCloudNodeControlReqCloudProvider(str, Enum):
    AWS = "aws"
    AZURE = "azure"
    GCP = "gcp"
    KUBERNETES = "kubernetes"
    LINUX = "linux"

    def __str__(self) -> str:
        return str(self.value)
