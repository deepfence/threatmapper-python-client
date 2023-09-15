from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_compliance import ModelCompliance
    from ..models.model_compliance_scan_result_status_counts import ModelComplianceScanResultStatusCounts


T = TypeVar("T", bound="ModelComplianceScanResult")


@_attrs_define
class ModelComplianceScanResult:
    """
    Example:
        {'benchmark_type': ['benchmark_type', 'benchmark_type'], 'docker_container_name': 'docker_container_name',
            'kubernetes_cluster_name': 'kubernetes_cluster_name', 'node_name': 'node_name', 'created_at': 6, 'compliances':
            [{'resource': 'resource', 'masked': True, 'description': 'description', 'resources': ['resources', 'resources'],
            'test_category': 'test_category', 'remediation_ansible': 'remediation_ansible', 'compliance_check_type':
            'compliance_check_type', 'test_rationale': 'test_rationale', 'test_severity': 'test_severity', 'node_type':
            'node_type', 'updated_at': 0, 'remediation_puppet': 'remediation_puppet', 'remediation_script':
            'remediation_script', 'node_id': 'node_id', 'status': 'status', 'test_desc': 'test_desc', 'test_number':
            'test_number'}, {'resource': 'resource', 'masked': True, 'description': 'description', 'resources':
            ['resources', 'resources'], 'test_category': 'test_category', 'remediation_ansible': 'remediation_ansible',
            'compliance_check_type': 'compliance_check_type', 'test_rationale': 'test_rationale', 'test_severity':
            'test_severity', 'node_type': 'node_type', 'updated_at': 0, 'remediation_puppet': 'remediation_puppet',
            'remediation_script': 'remediation_script', 'node_id': 'node_id', 'status': 'status', 'test_desc': 'test_desc',
            'test_number': 'test_number'}], 'compliance_percentage': 0.8008281904610115, 'node_type': 'node_type',
            'updated_at': 5, 'scan_id': 'scan_id', 'status_counts': {'key': 1}, 'docker_image_name': 'docker_image_name',
            'host_name': 'host_name', 'node_id': 'node_id'}

    Attributes:
        compliance_percentage (float):
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
        benchmark_type (Optional[List[str]]):
        compliances (Optional[List['ModelCompliance']]):
        status_counts (Optional[ModelComplianceScanResultStatusCounts]):
    """

    compliance_percentage: float
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
    benchmark_type: Optional[List[str]]
    compliances: Optional[List["ModelCompliance"]]
    status_counts: Optional["ModelComplianceScanResultStatusCounts"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compliance_percentage = self.compliance_percentage
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
        if self.benchmark_type is None:
            benchmark_type = None
        else:
            benchmark_type = self.benchmark_type

        if self.compliances is None:
            compliances = None
        else:
            compliances = []
            for compliances_item_data in self.compliances:
                compliances_item = compliances_item_data.to_dict()

                compliances.append(compliances_item)

        status_counts = self.status_counts.to_dict() if self.status_counts else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "compliance_percentage": compliance_percentage,
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
                "benchmark_type": benchmark_type,
                "compliances": compliances,
                "status_counts": status_counts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_compliance import ModelCompliance
        from ..models.model_compliance_scan_result_status_counts import ModelComplianceScanResultStatusCounts

        d = src_dict.copy()
        compliance_percentage = d.pop("compliance_percentage")

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

        benchmark_type = cast(List[str], d.pop("benchmark_type"))

        compliances = []
        _compliances = d.pop("compliances")
        for compliances_item_data in _compliances or []:
            compliances_item = ModelCompliance.from_dict(compliances_item_data)

            compliances.append(compliances_item)

        _status_counts = d.pop("status_counts")
        status_counts: Optional[ModelComplianceScanResultStatusCounts]
        if _status_counts is None:
            status_counts = None
        else:
            status_counts = ModelComplianceScanResultStatusCounts.from_dict(_status_counts)

        model_compliance_scan_result = cls(
            compliance_percentage=compliance_percentage,
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
            benchmark_type=benchmark_type,
            compliances=compliances,
            status_counts=status_counts,
        )

        model_compliance_scan_result.additional_properties = d
        return model_compliance_scan_result

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
