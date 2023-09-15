from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_nodes_in_scan_result_request_scan_type import ModelNodesInScanResultRequestScanType

T = TypeVar("T", bound="ModelNodesInScanResultRequest")


@_attrs_define
class ModelNodesInScanResultRequest:
    """
    Example:
        {'result_ids': ['result_ids', 'result_ids'], 'scan_type': 'SecretScan'}

    Attributes:
        scan_type (ModelNodesInScanResultRequestScanType):
        result_ids (Optional[List[str]]):
    """

    scan_type: ModelNodesInScanResultRequestScanType
    result_ids: Optional[List[str]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scan_type = self.scan_type.value

        if self.result_ids is None:
            result_ids = None
        else:
            result_ids = self.result_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scan_type": scan_type,
                "result_ids": result_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scan_type = ModelNodesInScanResultRequestScanType(d.pop("scan_type"))

        result_ids = cast(List[str], d.pop("result_ids"))

        model_nodes_in_scan_result_request = cls(
            scan_type=scan_type,
            result_ids=result_ids,
        )

        model_nodes_in_scan_result_request.additional_properties = d
        return model_nodes_in_scan_result_request

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
