from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_compliance_scan_info_severity_counts import ModelComplianceScanInfoSeverityCounts


T = TypeVar("T", bound="ModelComplianceScanInfo")


@_attrs_define
class ModelComplianceScanInfo:
    """
    Example:
        {'severity_counts': {'key': 6}, 'status_message': 'status_message', 'node_type': 'node_type', 'benchmark_types':
            ['benchmark_types', 'benchmark_types'], 'updated_at': 1, 'node_name': 'node_name', 'created_at': 0, 'scan_id':
            'scan_id', 'node_id': 'node_id', 'status': 'status'}

    Attributes:
        created_at (int):
        node_id (str):
        node_name (str):
        node_type (str):
        scan_id (str):
        status (str):
        status_message (str):
        updated_at (int):
        benchmark_types (Optional[List[str]]):
        severity_counts (Optional[ModelComplianceScanInfoSeverityCounts]):
    """

    created_at: int
    node_id: str
    node_name: str
    node_type: str
    scan_id: str
    status: str
    status_message: str
    updated_at: int
    benchmark_types: Optional[List[str]]
    severity_counts: Optional["ModelComplianceScanInfoSeverityCounts"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at
        node_id = self.node_id
        node_name = self.node_name
        node_type = self.node_type
        scan_id = self.scan_id
        status = self.status
        status_message = self.status_message
        updated_at = self.updated_at
        if self.benchmark_types is None:
            benchmark_types = None
        else:
            benchmark_types = self.benchmark_types

        severity_counts = self.severity_counts.to_dict() if self.severity_counts else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "node_id": node_id,
                "node_name": node_name,
                "node_type": node_type,
                "scan_id": scan_id,
                "status": status,
                "status_message": status_message,
                "updated_at": updated_at,
                "benchmark_types": benchmark_types,
                "severity_counts": severity_counts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_compliance_scan_info_severity_counts import ModelComplianceScanInfoSeverityCounts

        d = src_dict.copy()
        created_at = d.pop("created_at")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        node_type = d.pop("node_type")

        scan_id = d.pop("scan_id")

        status = d.pop("status")

        status_message = d.pop("status_message")

        updated_at = d.pop("updated_at")

        benchmark_types = cast(List[str], d.pop("benchmark_types"))

        _severity_counts = d.pop("severity_counts")
        severity_counts: Optional[ModelComplianceScanInfoSeverityCounts]
        if _severity_counts is None:
            severity_counts = None
        else:
            severity_counts = ModelComplianceScanInfoSeverityCounts.from_dict(_severity_counts)

        model_compliance_scan_info = cls(
            created_at=created_at,
            node_id=node_id,
            node_name=node_name,
            node_type=node_type,
            scan_id=scan_id,
            status=status,
            status_message=status_message,
            updated_at=updated_at,
            benchmark_types=benchmark_types,
            severity_counts=severity_counts,
        )

        model_compliance_scan_info.additional_properties = d
        return model_compliance_scan_info

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
