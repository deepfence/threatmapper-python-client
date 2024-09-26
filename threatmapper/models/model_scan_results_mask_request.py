from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_scan_results_mask_request_mask_action import ModelScanResultsMaskRequestMaskAction
from ..models.model_scan_results_mask_request_scan_type import ModelScanResultsMaskRequestScanType

T = TypeVar("T", bound="ModelScanResultsMaskRequest")


@_attrs_define
class ModelScanResultsMaskRequest:
    """
    Attributes:
        mask_action (ModelScanResultsMaskRequestMaskAction):
        result_ids (Union[List[str], None]):
        scan_id (str):
        scan_type (ModelScanResultsMaskRequestScanType):
    """

    mask_action: ModelScanResultsMaskRequestMaskAction
    result_ids: Union[List[str], None]
    scan_id: str
    scan_type: ModelScanResultsMaskRequestScanType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mask_action = self.mask_action.value

        result_ids: Union[List[str], None]
        if isinstance(self.result_ids, list):
            result_ids = self.result_ids

        else:
            result_ids = self.result_ids

        scan_id = self.scan_id

        scan_type = self.scan_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mask_action": mask_action,
                "result_ids": result_ids,
                "scan_id": scan_id,
                "scan_type": scan_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mask_action = ModelScanResultsMaskRequestMaskAction(d.pop("mask_action"))

        def _parse_result_ids(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                result_ids_type_0 = cast(List[str], data)

                return result_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        result_ids = _parse_result_ids(d.pop("result_ids"))

        scan_id = d.pop("scan_id")

        scan_type = ModelScanResultsMaskRequestScanType(d.pop("scan_type"))

        model_scan_results_mask_request = cls(
            mask_action=mask_action,
            result_ids=result_ids,
            scan_id=scan_id,
            scan_type=scan_type,
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
