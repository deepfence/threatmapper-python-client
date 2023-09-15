from enum import Enum


class UtilsReportFiltersNodeType(str, Enum):
    AWS = "aws"
    AZURE = "azure"
    CLUSTER = "cluster"
    CONTAINER = "container"
    CONTAINER_IMAGE = "container_image"
    GCP = "gcp"
    HOST = "host"
    LINUX = "linux"

    def __str__(self) -> str:
        return str(self.value)
