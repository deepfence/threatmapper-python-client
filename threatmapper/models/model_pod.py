from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_container import ModelContainer
    from ..models.model_pod_kubernetes_labels import ModelPodKubernetesLabels
    from ..models.model_process import ModelProcess


T = TypeVar("T", bound="ModelPod")


@_attrs_define
class ModelPod:
    """
    Example:
        {'kubernetes_ip': 'kubernetes_ip', 'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline',
            'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1,
            'pid': 4, 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}], 'secret_scan_status':
            'secret_scan_status', 'kubernetes_cluster_id': 'kubernetes_cluster_id', 'kubernetes_cluster_name':
            'kubernetes_cluster_name', 'kubernetes_state': 'kubernetes_state', 'node_name': 'node_name',
            'kubernetes_created': 'kubernetes_created', 'pod_name': 'pod_name', 'kubernetes_namespace':
            'kubernetes_namespace', 'kubernetes_is_in_host_network': True, 'malware_scan_status': 'malware_scan_status',
            'kubernetes_labels': {'key': ''}, 'containers': [{'vulnerabilities_count': 6, 'secrets_count': 1,
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
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}

    Attributes:
        host_name (str):
        kubernetes_cluster_id (str):
        kubernetes_cluster_name (str):
        kubernetes_created (str):
        kubernetes_ip (str):
        kubernetes_is_in_host_network (bool):
        kubernetes_namespace (str):
        kubernetes_state (str):
        malware_scan_status (str):
        node_id (str):
        node_name (str):
        pod_name (str):
        secret_scan_status (str):
        vulnerability_scan_status (str):
        containers (Optional[List['ModelContainer']]):
        kubernetes_labels (Optional[ModelPodKubernetesLabels]):
        processes (Optional[List['ModelProcess']]):
    """

    host_name: str
    kubernetes_cluster_id: str
    kubernetes_cluster_name: str
    kubernetes_created: str
    kubernetes_ip: str
    kubernetes_is_in_host_network: bool
    kubernetes_namespace: str
    kubernetes_state: str
    malware_scan_status: str
    node_id: str
    node_name: str
    pod_name: str
    secret_scan_status: str
    vulnerability_scan_status: str
    containers: Optional[List["ModelContainer"]]
    kubernetes_labels: Optional["ModelPodKubernetesLabels"]
    processes: Optional[List["ModelProcess"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host_name = self.host_name
        kubernetes_cluster_id = self.kubernetes_cluster_id
        kubernetes_cluster_name = self.kubernetes_cluster_name
        kubernetes_created = self.kubernetes_created
        kubernetes_ip = self.kubernetes_ip
        kubernetes_is_in_host_network = self.kubernetes_is_in_host_network
        kubernetes_namespace = self.kubernetes_namespace
        kubernetes_state = self.kubernetes_state
        malware_scan_status = self.malware_scan_status
        node_id = self.node_id
        node_name = self.node_name
        pod_name = self.pod_name
        secret_scan_status = self.secret_scan_status
        vulnerability_scan_status = self.vulnerability_scan_status
        if self.containers is None:
            containers = None
        else:
            containers = []
            for containers_item_data in self.containers:
                containers_item = containers_item_data.to_dict()

                containers.append(containers_item)

        kubernetes_labels = self.kubernetes_labels.to_dict() if self.kubernetes_labels else None

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
                "host_name": host_name,
                "kubernetes_cluster_id": kubernetes_cluster_id,
                "kubernetes_cluster_name": kubernetes_cluster_name,
                "kubernetes_created": kubernetes_created,
                "kubernetes_ip": kubernetes_ip,
                "kubernetes_is_in_host_network": kubernetes_is_in_host_network,
                "kubernetes_namespace": kubernetes_namespace,
                "kubernetes_state": kubernetes_state,
                "malware_scan_status": malware_scan_status,
                "node_id": node_id,
                "node_name": node_name,
                "pod_name": pod_name,
                "secret_scan_status": secret_scan_status,
                "vulnerability_scan_status": vulnerability_scan_status,
                "containers": containers,
                "kubernetes_labels": kubernetes_labels,
                "processes": processes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_container import ModelContainer
        from ..models.model_pod_kubernetes_labels import ModelPodKubernetesLabels
        from ..models.model_process import ModelProcess

        d = src_dict.copy()
        host_name = d.pop("host_name")

        kubernetes_cluster_id = d.pop("kubernetes_cluster_id")

        kubernetes_cluster_name = d.pop("kubernetes_cluster_name")

        kubernetes_created = d.pop("kubernetes_created")

        kubernetes_ip = d.pop("kubernetes_ip")

        kubernetes_is_in_host_network = d.pop("kubernetes_is_in_host_network")

        kubernetes_namespace = d.pop("kubernetes_namespace")

        kubernetes_state = d.pop("kubernetes_state")

        malware_scan_status = d.pop("malware_scan_status")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        pod_name = d.pop("pod_name")

        secret_scan_status = d.pop("secret_scan_status")

        vulnerability_scan_status = d.pop("vulnerability_scan_status")

        containers = []
        _containers = d.pop("containers")
        for containers_item_data in _containers or []:
            containers_item = ModelContainer.from_dict(containers_item_data)

            containers.append(containers_item)

        _kubernetes_labels = d.pop("kubernetes_labels")
        kubernetes_labels: Optional[ModelPodKubernetesLabels]
        if _kubernetes_labels is None:
            kubernetes_labels = None
        else:
            kubernetes_labels = ModelPodKubernetesLabels.from_dict(_kubernetes_labels)

        processes = []
        _processes = d.pop("processes")
        for processes_item_data in _processes or []:
            processes_item = ModelProcess.from_dict(processes_item_data)

            processes.append(processes_item)

        model_pod = cls(
            host_name=host_name,
            kubernetes_cluster_id=kubernetes_cluster_id,
            kubernetes_cluster_name=kubernetes_cluster_name,
            kubernetes_created=kubernetes_created,
            kubernetes_ip=kubernetes_ip,
            kubernetes_is_in_host_network=kubernetes_is_in_host_network,
            kubernetes_namespace=kubernetes_namespace,
            kubernetes_state=kubernetes_state,
            malware_scan_status=malware_scan_status,
            node_id=node_id,
            node_name=node_name,
            pod_name=pod_name,
            secret_scan_status=secret_scan_status,
            vulnerability_scan_status=vulnerability_scan_status,
            containers=containers,
            kubernetes_labels=kubernetes_labels,
            processes=processes,
        )

        model_pod.additional_properties = d
        return model_pod

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
