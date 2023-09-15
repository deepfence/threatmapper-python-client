from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_container_docker_labels import ModelContainerDockerLabels
    from ..models.model_container_image import ModelContainerImage
    from ..models.model_process import ModelProcess


T = TypeVar("T", bound="ModelContainer")


@_attrs_define
class ModelContainer:
    """
    Example:
        {'vulnerabilities_count': 6, 'secrets_count': 1, 'docker_container_state': 'docker_container_state', 'cpu_max':
            0.8008281904610115, 'memory_usage': 5, 'secret_latest_scan_id': 'secret_latest_scan_id',
            'docker_container_network_mode': 'docker_container_network_mode', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'malware_scan_status': 'malware_scan_status', 'docker_container_ips': ['', ''],
            'docker_labels': {'key': ''}, 'image': None, 'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline',
            'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1,
            'pid': 4, 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}], 'secret_scan_status':
            'secret_scan_status', 'docker_container_name': 'docker_container_name', 'docker_container_created':
            'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id', 'malwares_count': 1,
            'node_name': 'node_name', 'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}

    Attributes:
        cpu_max (float):
        cpu_usage (float):
        docker_container_command (str):
        docker_container_created (str):
        docker_container_name (str):
        docker_container_network_mode (str):
        docker_container_networks (str):
        docker_container_ports (str):
        docker_container_state (str):
        docker_container_state_human (str):
        host_name (str):
        image (ModelContainerImage):  Example: {'metadata': {'key': ''}, 'secret_scan_status': 'secret_scan_status',
            'vulnerabilities_count': 4, 'secrets_count': 1, 'malware_latest_scan_id': 'malware_latest_scan_id',
            'malwares_count': 7, 'node_name': 'node_name', 'secret_latest_scan_id': 'secret_latest_scan_id',
            'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id', 'docker_image_created_at':
            'docker_image_created_at', 'docker_image_tag': 'docker_image_tag', 'malware_scan_status': 'malware_scan_status',
            'docker_image_size': 'docker_image_size', 'image_node_id': 'image_node_id', 'docker_image_virtual_size':
            'docker_image_virtual_size', 'containers': [{'vulnerabilities_count': 6, 'secrets_count': 1,
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'malware_scan_status': 'malware_scan_status', 'docker_container_ips': ['', ''], 'docker_labels': {'key': ''},
            'image': None, 'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name':
            'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'cpu_usage': 7.061401241503109,
            'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655,
            'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}], 'secret_scan_status': 'secret_scan_status',
            'docker_container_name': 'docker_container_name', 'docker_container_created': 'docker_container_created',
            'malware_latest_scan_id': 'malware_latest_scan_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'docker_container_state': 'docker_container_state', 'cpu_max':
            0.8008281904610115, 'memory_usage': 5, 'secret_latest_scan_id': 'secret_latest_scan_id',
            'docker_container_network_mode': 'docker_container_network_mode', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'malware_scan_status': 'malware_scan_status', 'docker_container_ips': ['', ''],
            'docker_labels': {'key': ''}, 'image': None, 'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline',
            'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1,
            'pid': 4, 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}], 'secret_scan_status':
            'secret_scan_status', 'docker_container_name': 'docker_container_name', 'docker_container_created':
            'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id', 'malwares_count': 1,
            'node_name': 'node_name', 'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'docker_image_id': 'docker_image_id', 'vulnerability_scan_status': 'vulnerability_scan_status',
            'docker_image_name': 'docker_image_name', 'docker_image_tag_list': ['docker_image_tag_list',
            'docker_image_tag_list'], 'node_id': 'node_id'}.
        malware_latest_scan_id (str):
        malware_scan_status (str):
        malwares_count (int):
        memory_max (int):
        memory_usage (int):
        node_id (str):
        node_name (str):
        secret_latest_scan_id (str):
        secret_scan_status (str):
        secrets_count (int):
        uptime (int):
        vulnerabilities_count (int):
        vulnerability_latest_scan_id (str):
        vulnerability_scan_status (str):
        docker_container_ips (Optional[List[Any]]):
        docker_labels (Optional[ModelContainerDockerLabels]):
        processes (Optional[List['ModelProcess']]):
    """

    cpu_max: float
    cpu_usage: float
    docker_container_command: str
    docker_container_created: str
    docker_container_name: str
    docker_container_network_mode: str
    docker_container_networks: str
    docker_container_ports: str
    docker_container_state: str
    docker_container_state_human: str
    host_name: str
    image: "ModelContainerImage"
    malware_latest_scan_id: str
    malware_scan_status: str
    malwares_count: int
    memory_max: int
    memory_usage: int
    node_id: str
    node_name: str
    secret_latest_scan_id: str
    secret_scan_status: str
    secrets_count: int
    uptime: int
    vulnerabilities_count: int
    vulnerability_latest_scan_id: str
    vulnerability_scan_status: str
    docker_container_ips: Optional[List[Any]]
    docker_labels: Optional["ModelContainerDockerLabels"]
    processes: Optional[List["ModelProcess"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cpu_max = self.cpu_max
        cpu_usage = self.cpu_usage
        docker_container_command = self.docker_container_command
        docker_container_created = self.docker_container_created
        docker_container_name = self.docker_container_name
        docker_container_network_mode = self.docker_container_network_mode
        docker_container_networks = self.docker_container_networks
        docker_container_ports = self.docker_container_ports
        docker_container_state = self.docker_container_state
        docker_container_state_human = self.docker_container_state_human
        host_name = self.host_name
        image = self.image.to_dict()

        malware_latest_scan_id = self.malware_latest_scan_id
        malware_scan_status = self.malware_scan_status
        malwares_count = self.malwares_count
        memory_max = self.memory_max
        memory_usage = self.memory_usage
        node_id = self.node_id
        node_name = self.node_name
        secret_latest_scan_id = self.secret_latest_scan_id
        secret_scan_status = self.secret_scan_status
        secrets_count = self.secrets_count
        uptime = self.uptime
        vulnerabilities_count = self.vulnerabilities_count
        vulnerability_latest_scan_id = self.vulnerability_latest_scan_id
        vulnerability_scan_status = self.vulnerability_scan_status
        if self.docker_container_ips is None:
            docker_container_ips = None
        else:
            docker_container_ips = self.docker_container_ips

        docker_labels = self.docker_labels.to_dict() if self.docker_labels else None

        if self.processes is None:
            processes = None
        else:
            processes = []
            for processes_item_data in self.processes:
                processes_item = processes_item_data.to_dict()

                processes.append(processes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cpu_max": cpu_max,
                "cpu_usage": cpu_usage,
                "docker_container_command": docker_container_command,
                "docker_container_created": docker_container_created,
                "docker_container_name": docker_container_name,
                "docker_container_network_mode": docker_container_network_mode,
                "docker_container_networks": docker_container_networks,
                "docker_container_ports": docker_container_ports,
                "docker_container_state": docker_container_state,
                "docker_container_state_human": docker_container_state_human,
                "host_name": host_name,
                "image": image,
                "malware_latest_scan_id": malware_latest_scan_id,
                "malware_scan_status": malware_scan_status,
                "malwares_count": malwares_count,
                "memory_max": memory_max,
                "memory_usage": memory_usage,
                "node_id": node_id,
                "node_name": node_name,
                "secret_latest_scan_id": secret_latest_scan_id,
                "secret_scan_status": secret_scan_status,
                "secrets_count": secrets_count,
                "uptime": uptime,
                "vulnerabilities_count": vulnerabilities_count,
                "vulnerability_latest_scan_id": vulnerability_latest_scan_id,
                "vulnerability_scan_status": vulnerability_scan_status,
                "docker_container_ips": docker_container_ips,
                "docker_labels": docker_labels,
                "processes": processes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_container_docker_labels import ModelContainerDockerLabels
        from ..models.model_container_image import ModelContainerImage
        from ..models.model_process import ModelProcess

        d = src_dict.copy()
        cpu_max = d.pop("cpu_max")

        cpu_usage = d.pop("cpu_usage")

        docker_container_command = d.pop("docker_container_command")

        docker_container_created = d.pop("docker_container_created")

        docker_container_name = d.pop("docker_container_name")

        docker_container_network_mode = d.pop("docker_container_network_mode")

        docker_container_networks = d.pop("docker_container_networks")

        docker_container_ports = d.pop("docker_container_ports")

        docker_container_state = d.pop("docker_container_state")

        docker_container_state_human = d.pop("docker_container_state_human")

        host_name = d.pop("host_name")

        image = ModelContainerImage.from_dict(d.pop("image"))

        malware_latest_scan_id = d.pop("malware_latest_scan_id")

        malware_scan_status = d.pop("malware_scan_status")

        malwares_count = d.pop("malwares_count")

        memory_max = d.pop("memory_max")

        memory_usage = d.pop("memory_usage")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        secret_latest_scan_id = d.pop("secret_latest_scan_id")

        secret_scan_status = d.pop("secret_scan_status")

        secrets_count = d.pop("secrets_count")

        uptime = d.pop("uptime")

        vulnerabilities_count = d.pop("vulnerabilities_count")

        vulnerability_latest_scan_id = d.pop("vulnerability_latest_scan_id")

        vulnerability_scan_status = d.pop("vulnerability_scan_status")

        docker_container_ips = cast(List[Any], d.pop("docker_container_ips"))

        _docker_labels = d.pop("docker_labels")
        docker_labels: Optional[ModelContainerDockerLabels]
        if _docker_labels is None:
            docker_labels = None
        else:
            docker_labels = ModelContainerDockerLabels.from_dict(_docker_labels)

        processes = []
        _processes = d.pop("processes")
        for processes_item_data in _processes or []:
            processes_item = ModelProcess.from_dict(processes_item_data)

            processes.append(processes_item)

        model_container = cls(
            cpu_max=cpu_max,
            cpu_usage=cpu_usage,
            docker_container_command=docker_container_command,
            docker_container_created=docker_container_created,
            docker_container_name=docker_container_name,
            docker_container_network_mode=docker_container_network_mode,
            docker_container_networks=docker_container_networks,
            docker_container_ports=docker_container_ports,
            docker_container_state=docker_container_state,
            docker_container_state_human=docker_container_state_human,
            host_name=host_name,
            image=image,
            malware_latest_scan_id=malware_latest_scan_id,
            malware_scan_status=malware_scan_status,
            malwares_count=malwares_count,
            memory_max=memory_max,
            memory_usage=memory_usage,
            node_id=node_id,
            node_name=node_name,
            secret_latest_scan_id=secret_latest_scan_id,
            secret_scan_status=secret_scan_status,
            secrets_count=secrets_count,
            uptime=uptime,
            vulnerabilities_count=vulnerabilities_count,
            vulnerability_latest_scan_id=vulnerability_latest_scan_id,
            vulnerability_scan_status=vulnerability_scan_status,
            docker_container_ips=docker_container_ips,
            docker_labels=docker_labels,
            processes=processes,
        )

        model_container.additional_properties = d
        return model_container

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
