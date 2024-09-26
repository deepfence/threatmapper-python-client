from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_secret import ModelSecret
    from ..models.model_secret_scan_result_severity_counts_type_0 import ModelSecretScanResultSeverityCountsType0


T = TypeVar("T", bound="ModelSecretScanResult")


@_attrs_define
class ModelSecretScanResult:
    """
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
        secrets (Union[List['ModelSecret'], None]):
        severity_counts (Union['ModelSecretScanResultSeverityCountsType0', None]):
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
    secrets: Union[List["ModelSecret"], None]
    severity_counts: Union["ModelSecretScanResultSeverityCountsType0", None]
    updated_at: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.model_secret_scan_result_severity_counts_type_0 import ModelSecretScanResultSeverityCountsType0

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

        secrets: Union[List[Dict[str, Any]], None]
        if isinstance(self.secrets, list):
            secrets = []
            for secrets_type_0_item_data in self.secrets:
                secrets_type_0_item = secrets_type_0_item_data.to_dict()
                secrets.append(secrets_type_0_item)

        else:
            secrets = self.secrets

        severity_counts: Union[Dict[str, Any], None]
        if isinstance(self.severity_counts, ModelSecretScanResultSeverityCountsType0):
            severity_counts = self.severity_counts.to_dict()
        else:
            severity_counts = self.severity_counts

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
                "secrets": secrets,
                "severity_counts": severity_counts,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_secret import ModelSecret
        from ..models.model_secret_scan_result_severity_counts_type_0 import ModelSecretScanResultSeverityCountsType0

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

        def _parse_secrets(data: object) -> Union[List["ModelSecret"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                secrets_type_0 = []
                _secrets_type_0 = data
                for secrets_type_0_item_data in _secrets_type_0:
                    secrets_type_0_item = ModelSecret.from_dict(secrets_type_0_item_data)

                    secrets_type_0.append(secrets_type_0_item)

                return secrets_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelSecret"], None], data)

        secrets = _parse_secrets(d.pop("secrets"))

        def _parse_severity_counts(data: object) -> Union["ModelSecretScanResultSeverityCountsType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                severity_counts_type_0 = ModelSecretScanResultSeverityCountsType0.from_dict(data)

                return severity_counts_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelSecretScanResultSeverityCountsType0", None], data)

        severity_counts = _parse_severity_counts(d.pop("severity_counts"))

        updated_at = d.pop("updated_at")

        model_secret_scan_result = cls(
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
            secrets=secrets,
            severity_counts=severity_counts,
            updated_at=updated_at,
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
