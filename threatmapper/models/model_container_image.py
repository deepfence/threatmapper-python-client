from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_container import ModelContainer
    from ..models.model_container_image_metadata_type_0 import ModelContainerImageMetadataType0


T = TypeVar("T", bound="ModelContainerImage")


@_attrs_define
class ModelContainerImage:
    """
    Attributes:
        containers (Union[List['ModelContainer'], None]):
        docker_image_created_at (str):
        docker_image_id (str):
        docker_image_name (str):
        docker_image_size (str):
        docker_image_tag (str):
        docker_image_tag_list (Union[List[str], None]):
        docker_image_virtual_size (str):
        image_node_id (str):
        is_deepfence_system (bool):
        malware_latest_scan_id (str):
        malware_scan_status (str):
        malwares_count (int):
        node_id (str):
        node_name (str):
        secret_latest_scan_id (str):
        secret_scan_status (str):
        secrets_count (int):
        vulnerabilities_count (int):
        vulnerability_latest_scan_id (str):
        vulnerability_scan_status (str):
        metadata (Union['ModelContainerImageMetadataType0', None, Unset]):
    """

    containers: Union[List["ModelContainer"], None]
    docker_image_created_at: str
    docker_image_id: str
    docker_image_name: str
    docker_image_size: str
    docker_image_tag: str
    docker_image_tag_list: Union[List[str], None]
    docker_image_virtual_size: str
    image_node_id: str
    is_deepfence_system: bool
    malware_latest_scan_id: str
    malware_scan_status: str
    malwares_count: int
    node_id: str
    node_name: str
    secret_latest_scan_id: str
    secret_scan_status: str
    secrets_count: int
    vulnerabilities_count: int
    vulnerability_latest_scan_id: str
    vulnerability_scan_status: str
    metadata: Union["ModelContainerImageMetadataType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.model_container_image_metadata_type_0 import ModelContainerImageMetadataType0

        containers: Union[List[Dict[str, Any]], None]
        if isinstance(self.containers, list):
            containers = []
            for containers_type_0_item_data in self.containers:
                containers_type_0_item = containers_type_0_item_data.to_dict()
                containers.append(containers_type_0_item)

        else:
            containers = self.containers

        docker_image_created_at = self.docker_image_created_at

        docker_image_id = self.docker_image_id

        docker_image_name = self.docker_image_name

        docker_image_size = self.docker_image_size

        docker_image_tag = self.docker_image_tag

        docker_image_tag_list: Union[List[str], None]
        if isinstance(self.docker_image_tag_list, list):
            docker_image_tag_list = self.docker_image_tag_list

        else:
            docker_image_tag_list = self.docker_image_tag_list

        docker_image_virtual_size = self.docker_image_virtual_size

        image_node_id = self.image_node_id

        is_deepfence_system = self.is_deepfence_system

        malware_latest_scan_id = self.malware_latest_scan_id

        malware_scan_status = self.malware_scan_status

        malwares_count = self.malwares_count

        node_id = self.node_id

        node_name = self.node_name

        secret_latest_scan_id = self.secret_latest_scan_id

        secret_scan_status = self.secret_scan_status

        secrets_count = self.secrets_count

        vulnerabilities_count = self.vulnerabilities_count

        vulnerability_latest_scan_id = self.vulnerability_latest_scan_id

        vulnerability_scan_status = self.vulnerability_scan_status

        metadata: Union[Dict[str, Any], None, Unset]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, ModelContainerImageMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "containers": containers,
                "docker_image_created_at": docker_image_created_at,
                "docker_image_id": docker_image_id,
                "docker_image_name": docker_image_name,
                "docker_image_size": docker_image_size,
                "docker_image_tag": docker_image_tag,
                "docker_image_tag_list": docker_image_tag_list,
                "docker_image_virtual_size": docker_image_virtual_size,
                "image_node_id": image_node_id,
                "is_deepfence_system": is_deepfence_system,
                "malware_latest_scan_id": malware_latest_scan_id,
                "malware_scan_status": malware_scan_status,
                "malwares_count": malwares_count,
                "node_id": node_id,
                "node_name": node_name,
                "secret_latest_scan_id": secret_latest_scan_id,
                "secret_scan_status": secret_scan_status,
                "secrets_count": secrets_count,
                "vulnerabilities_count": vulnerabilities_count,
                "vulnerability_latest_scan_id": vulnerability_latest_scan_id,
                "vulnerability_scan_status": vulnerability_scan_status,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_container import ModelContainer
        from ..models.model_container_image_metadata_type_0 import ModelContainerImageMetadataType0

        d = src_dict.copy()

        def _parse_containers(data: object) -> Union[List["ModelContainer"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                containers_type_0 = []
                _containers_type_0 = data
                for containers_type_0_item_data in _containers_type_0:
                    containers_type_0_item = ModelContainer.from_dict(containers_type_0_item_data)

                    containers_type_0.append(containers_type_0_item)

                return containers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelContainer"], None], data)

        containers = _parse_containers(d.pop("containers"))

        docker_image_created_at = d.pop("docker_image_created_at")

        docker_image_id = d.pop("docker_image_id")

        docker_image_name = d.pop("docker_image_name")

        docker_image_size = d.pop("docker_image_size")

        docker_image_tag = d.pop("docker_image_tag")

        def _parse_docker_image_tag_list(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                docker_image_tag_list_type_0 = cast(List[str], data)

                return docker_image_tag_list_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        docker_image_tag_list = _parse_docker_image_tag_list(d.pop("docker_image_tag_list"))

        docker_image_virtual_size = d.pop("docker_image_virtual_size")

        image_node_id = d.pop("image_node_id")

        is_deepfence_system = d.pop("is_deepfence_system")

        malware_latest_scan_id = d.pop("malware_latest_scan_id")

        malware_scan_status = d.pop("malware_scan_status")

        malwares_count = d.pop("malwares_count")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        secret_latest_scan_id = d.pop("secret_latest_scan_id")

        secret_scan_status = d.pop("secret_scan_status")

        secrets_count = d.pop("secrets_count")

        vulnerabilities_count = d.pop("vulnerabilities_count")

        vulnerability_latest_scan_id = d.pop("vulnerability_latest_scan_id")

        vulnerability_scan_status = d.pop("vulnerability_scan_status")

        def _parse_metadata(data: object) -> Union["ModelContainerImageMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = ModelContainerImageMetadataType0.from_dict(data)

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelContainerImageMetadataType0", None, Unset], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        model_container_image = cls(
            containers=containers,
            docker_image_created_at=docker_image_created_at,
            docker_image_id=docker_image_id,
            docker_image_name=docker_image_name,
            docker_image_size=docker_image_size,
            docker_image_tag=docker_image_tag,
            docker_image_tag_list=docker_image_tag_list,
            docker_image_virtual_size=docker_image_virtual_size,
            image_node_id=image_node_id,
            is_deepfence_system=is_deepfence_system,
            malware_latest_scan_id=malware_latest_scan_id,
            malware_scan_status=malware_scan_status,
            malwares_count=malwares_count,
            node_id=node_id,
            node_name=node_name,
            secret_latest_scan_id=secret_latest_scan_id,
            secret_scan_status=secret_scan_status,
            secrets_count=secrets_count,
            vulnerabilities_count=vulnerabilities_count,
            vulnerability_latest_scan_id=vulnerability_latest_scan_id,
            vulnerability_scan_status=vulnerability_scan_status,
            metadata=metadata,
        )

        model_container_image.additional_properties = d
        return model_container_image

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
