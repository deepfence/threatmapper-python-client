from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelScanStatusReq")


@_attrs_define
class ModelScanStatusReq:
    """
    Example:
        {'bulk_scan_id': 'bulk_scan_id', 'scan_ids': ['scan_ids', 'scan_ids']}

    Attributes:
        bulk_scan_id (str):
        scan_ids (Optional[List[str]]):
    """

    bulk_scan_id: str
    scan_ids: Optional[List[str]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bulk_scan_id = self.bulk_scan_id
        if self.scan_ids is None:
            scan_ids = None
        else:
            scan_ids = self.scan_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bulk_scan_id": bulk_scan_id,
                "scan_ids": scan_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bulk_scan_id = d.pop("bulk_scan_id")

        scan_ids = cast(List[str], d.pop("scan_ids"))

        model_scan_status_req = cls(
            bulk_scan_id=bulk_scan_id,
            scan_ids=scan_ids,
        )

        model_scan_status_req.additional_properties = d
        return model_scan_status_req

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
