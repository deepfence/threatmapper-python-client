from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_scan_results_mask_request_scan_type import ModelScanResultsMaskRequestScanType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelScanResultsMaskRequest")


@_attrs_define
class ModelScanResultsMaskRequest:
    """
    Example:
        {'mask_across_hosts_and_images': True, 'result_ids': ['result_ids', 'result_ids'], 'scan_type': 'SecretScan',
            'scan_id': 'scan_id'}

    Attributes:
        scan_id (str):
        scan_type (ModelScanResultsMaskRequestScanType):
        mask_across_hosts_and_images (Union[Unset, bool]):
        result_ids (Optional[List[str]]):
    """

    scan_id: str
    scan_type: ModelScanResultsMaskRequestScanType
    result_ids: Optional[List[str]]
    mask_across_hosts_and_images: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scan_id = self.scan_id
        scan_type = self.scan_type.value

        mask_across_hosts_and_images = self.mask_across_hosts_and_images
        if self.result_ids is None:
            result_ids = None
        else:
            result_ids = self.result_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scan_id": scan_id,
                "scan_type": scan_type,
                "result_ids": result_ids,
            }
        )
        if mask_across_hosts_and_images is not UNSET:
            field_dict["mask_across_hosts_and_images"] = mask_across_hosts_and_images

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scan_id = d.pop("scan_id")

        scan_type = ModelScanResultsMaskRequestScanType(d.pop("scan_type"))

        mask_across_hosts_and_images = d.pop("mask_across_hosts_and_images", UNSET)

        result_ids = cast(List[str], d.pop("result_ids"))

        model_scan_results_mask_request = cls(
            scan_id=scan_id,
            scan_type=scan_type,
            mask_across_hosts_and_images=mask_across_hosts_and_images,
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
