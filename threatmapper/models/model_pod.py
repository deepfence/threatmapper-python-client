from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_container import ModelContainer
    from ..models.model_pod_kubernetes_labels_type_0 import ModelPodKubernetesLabelsType0
    from ..models.model_process import ModelProcess


T = TypeVar("T", bound="ModelPod")


@_attrs_define
class ModelPod:
    """
    Attributes:
        containers (Union[List['ModelContainer'], None]):
        host_name (str):
        kubernetes_cluster_id (str):
        kubernetes_cluster_name (str):
        kubernetes_created (str):
        kubernetes_ip (str):
        kubernetes_is_in_host_network (bool):
        kubernetes_labels (Union['ModelPodKubernetesLabelsType0', None]):
        kubernetes_namespace (str):
        kubernetes_state (str):
        malware_scan_status (str):
        node_id (str):
        node_name (str):
        pod_name (str):
        processes (Union[List['ModelProcess'], None]):
        secret_scan_status (str):
        vulnerability_scan_status (str):
    """

    containers: Union[List["ModelContainer"], None]
    host_name: str
    kubernetes_cluster_id: str
    kubernetes_cluster_name: str
    kubernetes_created: str
    kubernetes_ip: str
    kubernetes_is_in_host_network: bool
    kubernetes_labels: Union["ModelPodKubernetesLabelsType0", None]
    kubernetes_namespace: str
    kubernetes_state: str
    malware_scan_status: str
    node_id: str
    node_name: str
    pod_name: str
    processes: Union[List["ModelProcess"], None]
    secret_scan_status: str
    vulnerability_scan_status: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.model_pod_kubernetes_labels_type_0 import ModelPodKubernetesLabelsType0

        containers: Union[List[Dict[str, Any]], None]
        if isinstance(self.containers, list):
            containers = []
            for containers_type_0_item_data in self.containers:
                containers_type_0_item = containers_type_0_item_data.to_dict()
                containers.append(containers_type_0_item)

        else:
            containers = self.containers

        host_name = self.host_name

        kubernetes_cluster_id = self.kubernetes_cluster_id

        kubernetes_cluster_name = self.kubernetes_cluster_name

        kubernetes_created = self.kubernetes_created

        kubernetes_ip = self.kubernetes_ip

        kubernetes_is_in_host_network = self.kubernetes_is_in_host_network

        kubernetes_labels: Union[Dict[str, Any], None]
        if isinstance(self.kubernetes_labels, ModelPodKubernetesLabelsType0):
            kubernetes_labels = self.kubernetes_labels.to_dict()
        else:
            kubernetes_labels = self.kubernetes_labels

        kubernetes_namespace = self.kubernetes_namespace

        kubernetes_state = self.kubernetes_state

        malware_scan_status = self.malware_scan_status

        node_id = self.node_id

        node_name = self.node_name

        pod_name = self.pod_name

        processes: Union[List[Dict[str, Any]], None]
        if isinstance(self.processes, list):
            processes = []
            for processes_type_0_item_data in self.processes:
                processes_type_0_item = processes_type_0_item_data.to_dict()
                processes.append(processes_type_0_item)

        else:
            processes = self.processes

        secret_scan_status = self.secret_scan_status

        vulnerability_scan_status = self.vulnerability_scan_status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "containers": containers,
                "host_name": host_name,
                "kubernetes_cluster_id": kubernetes_cluster_id,
                "kubernetes_cluster_name": kubernetes_cluster_name,
                "kubernetes_created": kubernetes_created,
                "kubernetes_ip": kubernetes_ip,
                "kubernetes_is_in_host_network": kubernetes_is_in_host_network,
                "kubernetes_labels": kubernetes_labels,
                "kubernetes_namespace": kubernetes_namespace,
                "kubernetes_state": kubernetes_state,
                "malware_scan_status": malware_scan_status,
                "node_id": node_id,
                "node_name": node_name,
                "pod_name": pod_name,
                "processes": processes,
                "secret_scan_status": secret_scan_status,
                "vulnerability_scan_status": vulnerability_scan_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_container import ModelContainer
        from ..models.model_pod_kubernetes_labels_type_0 import ModelPodKubernetesLabelsType0
        from ..models.model_process import ModelProcess

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

        host_name = d.pop("host_name")

        kubernetes_cluster_id = d.pop("kubernetes_cluster_id")

        kubernetes_cluster_name = d.pop("kubernetes_cluster_name")

        kubernetes_created = d.pop("kubernetes_created")

        kubernetes_ip = d.pop("kubernetes_ip")

        kubernetes_is_in_host_network = d.pop("kubernetes_is_in_host_network")

        def _parse_kubernetes_labels(data: object) -> Union["ModelPodKubernetesLabelsType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                kubernetes_labels_type_0 = ModelPodKubernetesLabelsType0.from_dict(data)

                return kubernetes_labels_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelPodKubernetesLabelsType0", None], data)

        kubernetes_labels = _parse_kubernetes_labels(d.pop("kubernetes_labels"))

        kubernetes_namespace = d.pop("kubernetes_namespace")

        kubernetes_state = d.pop("kubernetes_state")

        malware_scan_status = d.pop("malware_scan_status")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        pod_name = d.pop("pod_name")

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

        secret_scan_status = d.pop("secret_scan_status")

        vulnerability_scan_status = d.pop("vulnerability_scan_status")

        model_pod = cls(
            containers=containers,
            host_name=host_name,
            kubernetes_cluster_id=kubernetes_cluster_id,
            kubernetes_cluster_name=kubernetes_cluster_name,
            kubernetes_created=kubernetes_created,
            kubernetes_ip=kubernetes_ip,
            kubernetes_is_in_host_network=kubernetes_is_in_host_network,
            kubernetes_labels=kubernetes_labels,
            kubernetes_namespace=kubernetes_namespace,
            kubernetes_state=kubernetes_state,
            malware_scan_status=malware_scan_status,
            node_id=node_id,
            node_name=node_name,
            pod_name=pod_name,
            processes=processes,
            secret_scan_status=secret_scan_status,
            vulnerability_scan_status=vulnerability_scan_status,
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
