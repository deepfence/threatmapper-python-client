from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_container_image import ModelContainerImage


T = TypeVar("T", bound="ModelRegistryAccount")


@_attrs_define
class ModelRegistryAccount:
    """
    Example:
        {'syncing': True, 'container_images': [{'is_deepfence_system': True, 'metadata': {'key': ''},
            'secret_scan_status': 'secret_scan_status', 'vulnerabilities_count': 4, 'secrets_count': 1,
            'malware_latest_scan_id': 'malware_latest_scan_id', 'malwares_count': 7, 'node_name': 'node_name',
            'secret_latest_scan_id': 'secret_latest_scan_id', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'docker_image_created_at': 'docker_image_created_at', 'docker_image_tag':
            'docker_image_tag', 'malware_scan_status': 'malware_scan_status', 'docker_image_size': 'docker_image_size',
            'image_node_id': 'image_node_id', 'docker_image_virtual_size': 'docker_image_virtual_size', 'containers':
            [{'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'docker_image_id': 'docker_image_id', 'vulnerability_scan_status': 'vulnerability_scan_status',
            'docker_image_name': 'docker_image_name', 'docker_image_tag_list': ['docker_image_tag_list',
            'docker_image_tag_list'], 'node_id': 'node_id'}, {'is_deepfence_system': True, 'metadata': {'key': ''},
            'secret_scan_status': 'secret_scan_status', 'vulnerabilities_count': 4, 'secrets_count': 1,
            'malware_latest_scan_id': 'malware_latest_scan_id', 'malwares_count': 7, 'node_name': 'node_name',
            'secret_latest_scan_id': 'secret_latest_scan_id', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'docker_image_created_at': 'docker_image_created_at', 'docker_image_tag':
            'docker_image_tag', 'malware_scan_status': 'malware_scan_status', 'docker_image_size': 'docker_image_size',
            'image_node_id': 'image_node_id', 'docker_image_virtual_size': 'docker_image_virtual_size', 'containers':
            [{'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'docker_image_id': 'docker_image_id', 'vulnerability_scan_status': 'vulnerability_scan_status',
            'docker_image_name': 'docker_image_name', 'docker_image_tag_list': ['docker_image_tag_list',
            'docker_image_tag_list'], 'node_id': 'node_id'}], 'registry_type': 'registry_type', 'name': 'name', 'node_id':
            'node_id'}

    Attributes:
        container_images (Union[List['ModelContainerImage'], None]):
        name (str):
        node_id (str):
        registry_type (str):
        syncing (bool):
    """

    container_images: Union[List["ModelContainerImage"], None]
    name: str
    node_id: str
    registry_type: str
    syncing: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        container_images: Union[List[Dict[str, Any]], None]
        if isinstance(self.container_images, list):
            container_images = []
            for container_images_type_0_item_data in self.container_images:
                container_images_type_0_item = container_images_type_0_item_data.to_dict()
                container_images.append(container_images_type_0_item)

        else:
            container_images = self.container_images

        name = self.name

        node_id = self.node_id

        registry_type = self.registry_type

        syncing = self.syncing

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "container_images": container_images,
                "name": name,
                "node_id": node_id,
                "registry_type": registry_type,
                "syncing": syncing,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_container_image import ModelContainerImage

        d = src_dict.copy()

        def _parse_container_images(data: object) -> Union[List["ModelContainerImage"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                container_images_type_0 = []
                _container_images_type_0 = data
                for container_images_type_0_item_data in _container_images_type_0:
                    container_images_type_0_item = ModelContainerImage.from_dict(container_images_type_0_item_data)

                    container_images_type_0.append(container_images_type_0_item)

                return container_images_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelContainerImage"], None], data)

        container_images = _parse_container_images(d.pop("container_images"))

        name = d.pop("name")

        node_id = d.pop("node_id")

        registry_type = d.pop("registry_type")

        syncing = d.pop("syncing")

        model_registry_account = cls(
            container_images=container_images,
            name=name,
            node_id=node_id,
            registry_type=registry_type,
            syncing=syncing,
        )

        model_registry_account.additional_properties = d
        return model_registry_account

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
