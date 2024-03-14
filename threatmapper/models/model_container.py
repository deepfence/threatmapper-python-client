from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_container_docker_labels_type_0 import ModelContainerDockerLabelsType0
    from ..models.model_container_image import ModelContainerImage
    from ..models.model_process import ModelProcess


T = TypeVar("T", bound="ModelContainer")


@_attrs_define
class ModelContainer:
    """
    Attributes:
        cpu_max (float):
        cpu_usage (float):
        docker_container_command (str):
        docker_container_created (str):
        docker_container_ips (Union[List[Any], None]):
        docker_container_name (str):
        docker_container_network_mode (str):
        docker_container_networks (str):
        docker_container_ports (str):
        docker_container_state (str):
        docker_container_state_human (str):
        docker_labels (Union['ModelContainerDockerLabelsType0', None]):
        host_name (str):
        image (ModelContainerImage):
        malware_latest_scan_id (str):
        malware_scan_status (str):
        malwares_count (int):
        memory_max (int):
        memory_usage (int):
        node_id (str):
        node_name (str):
        processes (Union[List['ModelProcess'], None]):
        secret_latest_scan_id (str):
        secret_scan_status (str):
        secrets_count (int):
        uptime (int):
        vulnerabilities_count (int):
        vulnerability_latest_scan_id (str):
        vulnerability_scan_status (str):
    """

    cpu_max: float
    cpu_usage: float
    docker_container_command: str
    docker_container_created: str
    docker_container_ips: Union[List[Any], None]
    docker_container_name: str
    docker_container_network_mode: str
    docker_container_networks: str
    docker_container_ports: str
    docker_container_state: str
    docker_container_state_human: str
    docker_labels: Union["ModelContainerDockerLabelsType0", None]
    host_name: str
    image: "ModelContainerImage"
    malware_latest_scan_id: str
    malware_scan_status: str
    malwares_count: int
    memory_max: int
    memory_usage: int
    node_id: str
    node_name: str
    processes: Union[List["ModelProcess"], None]
    secret_latest_scan_id: str
    secret_scan_status: str
    secrets_count: int
    uptime: int
    vulnerabilities_count: int
    vulnerability_latest_scan_id: str
    vulnerability_scan_status: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.model_container_docker_labels_type_0 import ModelContainerDockerLabelsType0

        cpu_max = self.cpu_max

        cpu_usage = self.cpu_usage

        docker_container_command = self.docker_container_command

        docker_container_created = self.docker_container_created

        docker_container_ips: Union[List[Any], None]
        if isinstance(self.docker_container_ips, list):
            docker_container_ips = self.docker_container_ips

        else:
            docker_container_ips = self.docker_container_ips

        docker_container_name = self.docker_container_name

        docker_container_network_mode = self.docker_container_network_mode

        docker_container_networks = self.docker_container_networks

        docker_container_ports = self.docker_container_ports

        docker_container_state = self.docker_container_state

        docker_container_state_human = self.docker_container_state_human

        docker_labels: Union[Dict[str, Any], None]
        if isinstance(self.docker_labels, ModelContainerDockerLabelsType0):
            docker_labels = self.docker_labels.to_dict()
        else:
            docker_labels = self.docker_labels

        host_name = self.host_name

        image = self.image.to_dict()

        malware_latest_scan_id = self.malware_latest_scan_id

        malware_scan_status = self.malware_scan_status

        malwares_count = self.malwares_count

        memory_max = self.memory_max

        memory_usage = self.memory_usage

        node_id = self.node_id

        node_name = self.node_name

        processes: Union[List[Dict[str, Any]], None]
        if isinstance(self.processes, list):
            processes = []
            for processes_type_0_item_data in self.processes:
                processes_type_0_item = processes_type_0_item_data.to_dict()
                processes.append(processes_type_0_item)

        else:
            processes = self.processes

        secret_latest_scan_id = self.secret_latest_scan_id

        secret_scan_status = self.secret_scan_status

        secrets_count = self.secrets_count

        uptime = self.uptime

        vulnerabilities_count = self.vulnerabilities_count

        vulnerability_latest_scan_id = self.vulnerability_latest_scan_id

        vulnerability_scan_status = self.vulnerability_scan_status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cpu_max": cpu_max,
                "cpu_usage": cpu_usage,
                "docker_container_command": docker_container_command,
                "docker_container_created": docker_container_created,
                "docker_container_ips": docker_container_ips,
                "docker_container_name": docker_container_name,
                "docker_container_network_mode": docker_container_network_mode,
                "docker_container_networks": docker_container_networks,
                "docker_container_ports": docker_container_ports,
                "docker_container_state": docker_container_state,
                "docker_container_state_human": docker_container_state_human,
                "docker_labels": docker_labels,
                "host_name": host_name,
                "image": image,
                "malware_latest_scan_id": malware_latest_scan_id,
                "malware_scan_status": malware_scan_status,
                "malwares_count": malwares_count,
                "memory_max": memory_max,
                "memory_usage": memory_usage,
                "node_id": node_id,
                "node_name": node_name,
                "processes": processes,
                "secret_latest_scan_id": secret_latest_scan_id,
                "secret_scan_status": secret_scan_status,
                "secrets_count": secrets_count,
                "uptime": uptime,
                "vulnerabilities_count": vulnerabilities_count,
                "vulnerability_latest_scan_id": vulnerability_latest_scan_id,
                "vulnerability_scan_status": vulnerability_scan_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_container_docker_labels_type_0 import ModelContainerDockerLabelsType0
        from ..models.model_container_image import ModelContainerImage
        from ..models.model_process import ModelProcess

        d = src_dict.copy()
        cpu_max = d.pop("cpu_max")

        cpu_usage = d.pop("cpu_usage")

        docker_container_command = d.pop("docker_container_command")

        docker_container_created = d.pop("docker_container_created")

        def _parse_docker_container_ips(data: object) -> Union[List[Any], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                docker_container_ips_type_0 = cast(List[Any], data)

                return docker_container_ips_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[Any], None], data)

        docker_container_ips = _parse_docker_container_ips(d.pop("docker_container_ips"))

        docker_container_name = d.pop("docker_container_name")

        docker_container_network_mode = d.pop("docker_container_network_mode")

        docker_container_networks = d.pop("docker_container_networks")

        docker_container_ports = d.pop("docker_container_ports")

        docker_container_state = d.pop("docker_container_state")

        docker_container_state_human = d.pop("docker_container_state_human")

        def _parse_docker_labels(data: object) -> Union["ModelContainerDockerLabelsType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                docker_labels_type_0 = ModelContainerDockerLabelsType0.from_dict(data)

                return docker_labels_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelContainerDockerLabelsType0", None], data)

        docker_labels = _parse_docker_labels(d.pop("docker_labels"))

        host_name = d.pop("host_name")

        image = ModelContainerImage.from_dict(d.pop("image"))

        malware_latest_scan_id = d.pop("malware_latest_scan_id")

        malware_scan_status = d.pop("malware_scan_status")

        malwares_count = d.pop("malwares_count")

        memory_max = d.pop("memory_max")

        memory_usage = d.pop("memory_usage")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        def _parse_processes(data: object) -> Union[List["ModelProcess"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                processes_type_0 = []
                _processes_type_0 = data
                for processes_type_0_item_data in _processes_type_0:
                    processes_type_0_item = ModelProcess.from_dict(processes_type_0_item_data)

                    processes_type_0.append(processes_type_0_item)

                return processes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelProcess"], None], data)

        processes = _parse_processes(d.pop("processes"))

        secret_latest_scan_id = d.pop("secret_latest_scan_id")

        secret_scan_status = d.pop("secret_scan_status")

        secrets_count = d.pop("secrets_count")

        uptime = d.pop("uptime")

        vulnerabilities_count = d.pop("vulnerabilities_count")

        vulnerability_latest_scan_id = d.pop("vulnerability_latest_scan_id")

        vulnerability_scan_status = d.pop("vulnerability_scan_status")

        model_container = cls(
            cpu_max=cpu_max,
            cpu_usage=cpu_usage,
            docker_container_command=docker_container_command,
            docker_container_created=docker_container_created,
            docker_container_ips=docker_container_ips,
            docker_container_name=docker_container_name,
            docker_container_network_mode=docker_container_network_mode,
            docker_container_networks=docker_container_networks,
            docker_container_ports=docker_container_ports,
            docker_container_state=docker_container_state,
            docker_container_state_human=docker_container_state_human,
            docker_labels=docker_labels,
            host_name=host_name,
            image=image,
            malware_latest_scan_id=malware_latest_scan_id,
            malware_scan_status=malware_scan_status,
            malwares_count=malwares_count,
            memory_max=memory_max,
            memory_usage=memory_usage,
            node_id=node_id,
            node_name=node_name,
            processes=processes,
            secret_latest_scan_id=secret_latest_scan_id,
            secret_scan_status=secret_scan_status,
            secrets_count=secrets_count,
            uptime=uptime,
            vulnerabilities_count=vulnerabilities_count,
            vulnerability_latest_scan_id=vulnerability_latest_scan_id,
            vulnerability_scan_status=vulnerability_scan_status,
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
