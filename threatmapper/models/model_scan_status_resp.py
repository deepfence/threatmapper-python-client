from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_scan_status_resp_statuses import ModelScanStatusRespStatuses


T = TypeVar("T", bound="ModelScanStatusResp")


@_attrs_define
class ModelScanStatusResp:
    """
    Example:
        {'statuses': {'key': {'severity_counts': {'key': 6}, 'status_message': 'status_message', 'node_type':
            'node_type', 'updated_at': 1, 'node_name': 'node_name', 'created_at': 0, 'scan_id': 'scan_id', 'node_id':
            'node_id', 'status': 'status'}}}

    Attributes:
        statuses (Optional[ModelScanStatusRespStatuses]):
    """

    statuses: Optional["ModelScanStatusRespStatuses"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        statuses = self.statuses.to_dict() if self.statuses else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "statuses": statuses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_scan_status_resp_statuses import ModelScanStatusRespStatuses

        d = src_dict.copy()
        _statuses = d.pop("statuses")
        statuses: Optional[ModelScanStatusRespStatuses]
        if _statuses is None:
            statuses = None
        else:
            statuses = ModelScanStatusRespStatuses.from_dict(_statuses)

        model_scan_status_resp = cls(
            statuses=statuses,
        )

        model_scan_status_resp.additional_properties = d
        return model_scan_status_resp

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
