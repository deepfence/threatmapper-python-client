from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_secret import ModelSecret
    from ..models.model_secret_scan_result_severity_counts import ModelSecretScanResultSeverityCounts


T = TypeVar("T", bound="ModelSecretScanResult")


@_attrs_define
class ModelSecretScanResult:
    """
    Example:
        {'severity_counts': {'key': 6}, 'node_type': 'node_type', 'docker_container_name': 'docker_container_name',
            'updated_at': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name', 'node_name': 'node_name', 'created_at':
            0, 'scan_id': 'scan_id', 'secrets': [{'full_filename': 'full_filename', 'level': 'level', 'masked': True,
            'part': 'part', 'relative_ending_index': 0, 'starting_index': 5, 'resources': ['resources', 'resources'],
            'signature_to_match': 'signature_to_match', 'rule_id': 1, 'score': 5.962133916683182, 'matched_content':
            'matched_content', 'updated_at': 2, 'name': 'name', 'relative_starting_index': 6, 'node_id': 'node_id'},
            {'full_filename': 'full_filename', 'level': 'level', 'masked': True, 'part': 'part', 'relative_ending_index': 0,
            'starting_index': 5, 'resources': ['resources', 'resources'], 'signature_to_match': 'signature_to_match',
            'rule_id': 1, 'score': 5.962133916683182, 'matched_content': 'matched_content', 'updated_at': 2, 'name': 'name',
            'relative_starting_index': 6, 'node_id': 'node_id'}], 'docker_image_name': 'docker_image_name', 'host_name':
            'host_name', 'node_id': 'node_id'}

    Attributes:
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
        secrets (Optional[List['ModelSecret']]):
        severity_counts (Optional[ModelSecretScanResultSeverityCounts]):
    """

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
    secrets: Optional[List["ModelSecret"]]
    severity_counts: Optional["ModelSecretScanResultSeverityCounts"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        if self.secrets is None:
            secrets = None
        else:
            secrets = []
            for secrets_item_data in self.secrets:
                secrets_item = secrets_item_data.to_dict()

                secrets.append(secrets_item)

        severity_counts = self.severity_counts.to_dict() if self.severity_counts else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
                "secrets": secrets,
                "severity_counts": severity_counts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_secret import ModelSecret
        from ..models.model_secret_scan_result_severity_counts import ModelSecretScanResultSeverityCounts

        d = src_dict.copy()
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

        secrets = []
        _secrets = d.pop("secrets")
        for secrets_item_data in _secrets or []:
            secrets_item = ModelSecret.from_dict(secrets_item_data)

            secrets.append(secrets_item)

        _severity_counts = d.pop("severity_counts")
        severity_counts: Optional[ModelSecretScanResultSeverityCounts]
        if _severity_counts is None:
            severity_counts = None
        else:
            severity_counts = ModelSecretScanResultSeverityCounts.from_dict(_severity_counts)

        model_secret_scan_result = cls(
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
            secrets=secrets,
            severity_counts=severity_counts,
        )

        model_secret_scan_result.additional_properties = d
        return model_secret_scan_result

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
