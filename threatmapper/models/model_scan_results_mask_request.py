from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_scan_results_mask_request_mask_action import ModelScanResultsMaskRequestMaskAction
from ..models.model_scan_results_mask_request_scan_type import ModelScanResultsMaskRequestScanType

T = TypeVar("T", bound="ModelScanResultsMaskRequest")


@_attrs_define
class ModelScanResultsMaskRequest:
    """
    Example:
        {'mask_action': 'mask_global', 'result_ids': ['result_ids', 'result_ids'], 'scan_type': 'SecretScan', 'scan_id':
            'scan_id'}

    Attributes:
        mask_action (ModelScanResultsMaskRequestMaskAction):
        scan_id (str):
        scan_type (ModelScanResultsMaskRequestScanType):
        result_ids (Optional[List[str]]):
    """

    mask_action: ModelScanResultsMaskRequestMaskAction
    scan_id: str
    scan_type: ModelScanResultsMaskRequestScanType
    result_ids: Optional[List[str]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mask_action = self.mask_action.value

        scan_id = self.scan_id
        scan_type = self.scan_type.value

        if self.result_ids is None:
            result_ids = None
        else:
            result_ids = self.result_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mask_action": mask_action,
                "scan_id": scan_id,
                "scan_type": scan_type,
                "result_ids": result_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mask_action = ModelScanResultsMaskRequestMaskAction(d.pop("mask_action"))

        scan_id = d.pop("scan_id")

        scan_type = ModelScanResultsMaskRequestScanType(d.pop("scan_type"))

        result_ids = cast(List[str], d.pop("result_ids"))

        model_scan_results_mask_request = cls(
            mask_action=mask_action,
            scan_id=scan_id,
            scan_type=scan_type,
            result_ids=result_ids,
        )

        model_scan_results_mask_request.additional_properties = d
        return model_scan_results_mask_request

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
