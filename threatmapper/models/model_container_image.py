from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_container import ModelContainer
    from ..models.model_container_image_metadata import ModelContainerImageMetadata


T = TypeVar("T", bound="ModelContainerImage")


@_attrs_define
class ModelContainerImage:
    """
    Example:
        {'metadata': {'key': ''}, 'secret_scan_status': 'secret_scan_status', 'vulnerabilities_count': 4,
            'secrets_count': 1, 'malware_latest_scan_id': 'malware_latest_scan_id', 'malwares_count': 7, 'node_name':
            'node_name', 'secret_latest_scan_id': 'secret_latest_scan_id', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'docker_image_created_at': 'docker_image_created_at', 'docker_image_tag':
            'docker_image_tag', 'malware_scan_status': 'malware_scan_status', 'docker_image_size': 'docker_image_size',
            'image_node_id': 'image_node_id', 'docker_image_virtual_size': 'docker_image_virtual_size', 'containers':
            [{'vulnerabilities_count': 6, 'secrets_count': 1, 'docker_container_state': 'docker_container_state', 'cpu_max':
            0.8008281904610115, 'memory_usage': 5, 'secret_latest_scan_id': 'secret_latest_scan_id',
            'docker_container_network_mode': 'docker_container_network_mode', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'malware_scan_status': 'malware_scan_status', 'docker_container_ips': ['', ''],
            'docker_labels': {'key': ''}, 'image': None, 'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9,
            'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3,
            'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109,
            'node_id': 'node_id', 'ppid': 7}], 'secret_scan_status': 'secret_scan_status', 'docker_container_name':
            'docker_container_name', 'docker_container_created': 'docker_container_created', 'malware_latest_scan_id':
            'malware_latest_scan_id', 'malwares_count': 1, 'node_name': 'node_name', 'docker_container_networks':
            'docker_container_networks', 'docker_container_command': 'docker_container_command', 'uptime': 1, 'memory_max':
            5, 'docker_container_ports': 'docker_container_ports', 'docker_container_state_human':
            'docker_container_state_human', 'cpu_usage': 6.027456183070403, 'vulnerability_scan_status':
            'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}, {'vulnerabilities_count': 6,
            'secrets_count': 1, 'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115,
            'memory_usage': 5, 'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'malware_scan_status': 'malware_scan_status', 'docker_container_ips': ['', ''], 'docker_labels': {'key': ''},
            'image': None, 'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name':
            'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name',
            'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline',
            'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1,
            'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'malwares_count': 1, 'node_name': 'node_name', 'docker_container_networks': 'docker_container_networks',
            'docker_container_command': 'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports':
            'docker_container_ports', 'docker_container_state_human': 'docker_container_state_human', 'cpu_usage':
            6.027456183070403, 'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name',
            'node_id': 'node_id'}], 'docker_image_id': 'docker_image_id', 'vulnerability_scan_status':
            'vulnerability_scan_status', 'docker_image_name': 'docker_image_name', 'docker_image_tag_list':
            ['docker_image_tag_list', 'docker_image_tag_list'], 'node_id': 'node_id'}

    Attributes:
        docker_image_created_at (str):
        docker_image_id (str):
        docker_image_name (str):
        docker_image_size (str):
        docker_image_tag (str):
        docker_image_virtual_size (str):
        image_node_id (str):
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
        containers (Optional[List['ModelContainer']]):
        docker_image_tag_list (Optional[List[str]]):
        metadata (Union[Unset, None, ModelContainerImageMetadata]):
    """

    docker_image_created_at: str
    docker_image_id: str
    docker_image_name: str
    docker_image_size: str
    docker_image_tag: str
    docker_image_virtual_size: str
    image_node_id: str
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
    containers: Optional[List["ModelContainer"]]
    docker_image_tag_list: Optional[List[str]]
    metadata: Union[Unset, None, "ModelContainerImageMetadata"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        docker_image_created_at = self.docker_image_created_at
        docker_image_id = self.docker_image_id
        docker_image_name = self.docker_image_name
        docker_image_size = self.docker_image_size
        docker_image_tag = self.docker_image_tag
        docker_image_virtual_size = self.docker_image_virtual_size
        image_node_id = self.image_node_id
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
        if self.containers is None:
            containers = None
        else:
            containers = []
            for containers_item_data in self.containers:
                containers_item = containers_item_data.to_dict()

                containers.append(containers_item)

        if self.docker_image_tag_list is None:
            docker_image_tag_list = None
        else:
            docker_image_tag_list = self.docker_image_tag_list

        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "docker_image_created_at": docker_image_created_at,
                "docker_image_id": docker_image_id,
                "docker_image_name": docker_image_name,
                "docker_image_size": docker_image_size,
                "docker_image_tag": docker_image_tag,
                "docker_image_virtual_size": docker_image_virtual_size,
                "image_node_id": image_node_id,
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
                "containers": containers,
                "docker_image_tag_list": docker_image_tag_list,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_container import ModelContainer
        from ..models.model_container_image_metadata import ModelContainerImageMetadata

        d = src_dict.copy()
        docker_image_created_at = d.pop("docker_image_created_at")

        docker_image_id = d.pop("docker_image_id")

        docker_image_name = d.pop("docker_image_name")

        docker_image_size = d.pop("docker_image_size")

        docker_image_tag = d.pop("docker_image_tag")

        docker_image_virtual_size = d.pop("docker_image_virtual_size")

        image_node_id = d.pop("image_node_id")

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

        containers = []
        _containers = d.pop("containers")
        for containers_item_data in _containers or []:
            containers_item = ModelContainer.from_dict(containers_item_data)

            containers.append(containers_item)

        docker_image_tag_list = cast(List[str], d.pop("docker_image_tag_list"))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, None, ModelContainerImageMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModelContainerImageMetadata.from_dict(_metadata)

        model_container_image = cls(
            docker_image_created_at=docker_image_created_at,
            docker_image_id=docker_image_id,
            docker_image_name=docker_image_name,
            docker_image_size=docker_image_size,
            docker_image_tag=docker_image_tag,
            docker_image_virtual_size=docker_image_virtual_size,
            image_node_id=image_node_id,
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
            containers=containers,
            docker_image_tag_list=docker_image_tag_list,
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
