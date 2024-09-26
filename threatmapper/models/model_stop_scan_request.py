from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_stop_scan_request_scan_type import ModelStopScanRequestScanType

T = TypeVar("T", bound="ModelStopScanRequest")


@_attrs_define
class ModelStopScanRequest:
    """
    Attributes:
        scan_ids (Union[List[str], None]):
        scan_type (ModelStopScanRequestScanType):
    """

    scan_ids: Union[List[str], None]
    scan_type: ModelStopScanRequestScanType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scan_ids: Union[List[str], None]
        if isinstance(self.scan_ids, list):
            scan_ids = self.scan_ids

        else:
            scan_ids = self.scan_ids

        scan_type = self.scan_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scan_ids": scan_ids,
                "scan_type": scan_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_scan_ids(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scan_ids_type_0 = cast(List[str], data)

                return scan_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        scan_ids = _parse_scan_ids(d.pop("scan_ids"))

        scan_type = ModelStopScanRequestScanType(d.pop("scan_type"))

        model_stop_scan_request = cls(
            scan_ids=scan_ids,
            scan_type=scan_type,
        )

        model_stop_scan_request.additional_properties = d
        return model_stop_scan_request

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
