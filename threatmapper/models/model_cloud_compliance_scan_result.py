from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_cloud_compliance import ModelCloudCompliance
    from ..models.model_cloud_compliance_scan_result_status_counts_type_0 import (
        ModelCloudComplianceScanResultStatusCountsType0,
    )


T = TypeVar("T", bound="ModelCloudComplianceScanResult")


@_attrs_define
class ModelCloudComplianceScanResult:
    """
    Attributes:
        benchmark_type (Union[List[str], None]):
        cloud_account_id (str):
        compliance_percentage (float):
        compliances (Union[List['ModelCloudCompliance'], None]):
        created_at (int):
        docker_container_name (str):
        docker_image_name (str):
        host_name (str):
        kubernetes_cluster_name (str):
        node_id (str):
        node_name (str):
        node_type (str):
        scan_id (str):
        status_counts (Union['ModelCloudComplianceScanResultStatusCountsType0', None]):
        updated_at (int):
    """

    benchmark_type: Union[List[str], None]
    cloud_account_id: str
    compliance_percentage: float
    compliances: Union[List["ModelCloudCompliance"], None]
    created_at: int
    docker_container_name: str
    docker_image_name: str
    host_name: str
    kubernetes_cluster_name: str
    node_id: str
    node_name: str
    node_type: str
    scan_id: str
    status_counts: Union["ModelCloudComplianceScanResultStatusCountsType0", None]
    updated_at: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.model_cloud_compliance_scan_result_status_counts_type_0 import (
            ModelCloudComplianceScanResultStatusCountsType0,
        )

        benchmark_type: Union[List[str], None]
        if isinstance(self.benchmark_type, list):
            benchmark_type = self.benchmark_type

        else:
            benchmark_type = self.benchmark_type

        cloud_account_id = self.cloud_account_id

        compliance_percentage = self.compliance_percentage

        compliances: Union[List[Dict[str, Any]], None]
        if isinstance(self.compliances, list):
            compliances = []
            for compliances_type_0_item_data in self.compliances:
                compliances_type_0_item = compliances_type_0_item_data.to_dict()
                compliances.append(compliances_type_0_item)

        else:
            compliances = self.compliances

        created_at = self.created_at

        docker_container_name = self.docker_container_name

        docker_image_name = self.docker_image_name

        host_name = self.host_name

        kubernetes_cluster_name = self.kubernetes_cluster_name

        node_id = self.node_id

        node_name = self.node_name

        node_type = self.node_type

        scan_id = self.scan_id

        status_counts: Union[Dict[str, Any], None]
        if isinstance(self.status_counts, ModelCloudComplianceScanResultStatusCountsType0):
            status_counts = self.status_counts.to_dict()
        else:
            status_counts = self.status_counts

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "benchmark_type": benchmark_type,
                "cloud_account_id": cloud_account_id,
                "compliance_percentage": compliance_percentage,
                "compliances": compliances,
                "created_at": created_at,
                "docker_container_name": docker_container_name,
                "docker_image_name": docker_image_name,
                "host_name": host_name,
                "kubernetes_cluster_name": kubernetes_cluster_name,
                "node_id": node_id,
                "node_name": node_name,
                "node_type": node_type,
                "scan_id": scan_id,
                "status_counts": status_counts,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_cloud_compliance import ModelCloudCompliance
        from ..models.model_cloud_compliance_scan_result_status_counts_type_0 import (
            ModelCloudComplianceScanResultStatusCountsType0,
        )

        d = src_dict.copy()

        def _parse_benchmark_type(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                benchmark_type_type_0 = cast(List[str], data)

                return benchmark_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        benchmark_type = _parse_benchmark_type(d.pop("benchmark_type"))

        cloud_account_id = d.pop("cloud_account_id")

        compliance_percentage = d.pop("compliance_percentage")

        def _parse_compliances(data: object) -> Union[List["ModelCloudCompliance"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                compliances_type_0 = []
                _compliances_type_0 = data
                for compliances_type_0_item_data in _compliances_type_0:
                    compliances_type_0_item = ModelCloudCompliance.from_dict(compliances_type_0_item_data)

                    compliances_type_0.append(compliances_type_0_item)

                return compliances_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelCloudCompliance"], None], data)

        compliances = _parse_compliances(d.pop("compliances"))

        created_at = d.pop("created_at")

        docker_container_name = d.pop("docker_container_name")

        docker_image_name = d.pop("docker_image_name")

        host_name = d.pop("host_name")

        kubernetes_cluster_name = d.pop("kubernetes_cluster_name")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        node_type = d.pop("node_type")

        scan_id = d.pop("scan_id")

        def _parse_status_counts(data: object) -> Union["ModelCloudComplianceScanResultStatusCountsType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_counts_type_0 = ModelCloudComplianceScanResultStatusCountsType0.from_dict(data)

                return status_counts_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelCloudComplianceScanResultStatusCountsType0", None], data)

        status_counts = _parse_status_counts(d.pop("status_counts"))

        updated_at = d.pop("updated_at")

        model_cloud_compliance_scan_result = cls(
            benchmark_type=benchmark_type,
            cloud_account_id=cloud_account_id,
            compliance_percentage=compliance_percentage,
            compliances=compliances,
            created_at=created_at,
            docker_container_name=docker_container_name,
            docker_image_name=docker_image_name,
            host_name=host_name,
            kubernetes_cluster_name=kubernetes_cluster_name,
            node_id=node_id,
            node_name=node_name,
            node_type=node_type,
            scan_id=scan_id,
            status_counts=status_counts,
            updated_at=updated_at,
        )

        model_cloud_compliance_scan_result.additional_properties = d
        return model_cloud_compliance_scan_result

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
