from enum import Enum


class ModelNodeIdentifierNodeType(str, Enum):
    CLOUD_ACCOUNT = "cloud_account"
    CLUSTER = "cluster"
    CONTAINER = "container"
    HOST = "host"
    IMAGE = "image"
    POD = "pod"
    REGISTRY = "registry"

    def __str__(self) -> str:
        return str(self.value)
