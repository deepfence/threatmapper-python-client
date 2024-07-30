from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelScanResultsCommon")


@_attrs_define
class ModelScanResultsCommon:
    """
    Example:
        {'cloud_account_id': 'cloud_account_id', 'node_type': 'node_type', 'docker_container_name':
            'docker_container_name', 'updated_at': 6, 'kubernetes_cluster_name': 'kubernetes_cluster_name', 'node_name':
            'node_name', 'created_at': 0, 'scan_id': 'scan_id', 'docker_image_name': 'docker_image_name', 'host_name':
            'host_name', 'node_id': 'node_id'}

    Attributes:
        cloud_account_id (str):
        created_at (int):
        docker_container_name (str):
        docker_image_name (str):
        host_name (str):
        kubernetes_cluster_name (str):
        node_id (str):
        node_name (str):
        node_type (str):
        scan_id (str):
        updated_at (int):
    """

    cloud_account_id: str
    created_at: int
    docker_container_name: str
    docker_image_name: str
    host_name: str
    kubernetes_cluster_name: str
    node_id: str
    node_name: str
    node_type: str
    scan_id: str
    updated_at: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloud_account_id = self.cloud_account_id

        created_at = self.created_at

        docker_container_name = self.docker_container_name

        docker_image_name = self.docker_image_name

        host_name = self.host_name

        kubernetes_cluster_name = self.kubernetes_cluster_name

        node_id = self.node_id

        node_name = self.node_name

        node_type = self.node_type

        scan_id = self.scan_id

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_account_id": cloud_account_id,
                "created_at": created_at,
                "docker_container_name": docker_container_name,
                "docker_image_name": docker_image_name,
                "host_name": host_name,
                "kubernetes_cluster_name": kubernetes_cluster_name,
                "node_id": node_id,
                "node_name": node_name,
                "node_type": node_type,
                "scan_id": scan_id,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cloud_account_id = d.pop("cloud_account_id")

        created_at = d.pop("created_at")

        docker_container_name = d.pop("docker_container_name")

        docker_image_name = d.pop("docker_image_name")

        host_name = d.pop("host_name")

        kubernetes_cluster_name = d.pop("kubernetes_cluster_name")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        node_type = d.pop("node_type")

        scan_id = d.pop("scan_id")

        updated_at = d.pop("updated_at")

        model_scan_results_common = cls(
            cloud_account_id=cloud_account_id,
            created_at=created_at,
            docker_container_name=docker_container_name,
            docker_image_name=docker_image_name,
            host_name=host_name,
            kubernetes_cluster_name=kubernetes_cluster_name,
            node_id=node_id,
            node_name=node_name,
            node_type=node_type,
            scan_id=scan_id,
            updated_at=updated_at,
        )

        model_scan_results_common.additional_properties = d
        return model_scan_results_common

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
