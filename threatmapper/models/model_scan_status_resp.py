from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_scan_status_resp_statuses_type_0 import ModelScanStatusRespStatusesType0


T = TypeVar("T", bound="ModelScanStatusResp")


@_attrs_define
class ModelScanStatusResp:
    """
    Attributes:
        statuses (Union['ModelScanStatusRespStatusesType0', None]):
    """

    statuses: Union["ModelScanStatusRespStatusesType0", None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.model_scan_status_resp_statuses_type_0 import ModelScanStatusRespStatusesType0

        statuses: Union[Dict[str, Any], None]
        if isinstance(self.statuses, ModelScanStatusRespStatusesType0):
            statuses = self.statuses.to_dict()
        else:
            statuses = self.statuses

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
        from ..models.model_scan_status_resp_statuses_type_0 import ModelScanStatusRespStatusesType0

        d = src_dict.copy()

        def _parse_statuses(data: object) -> Union["ModelScanStatusRespStatusesType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                statuses_type_0 = ModelScanStatusRespStatusesType0.from_dict(data)

                return statuses_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelScanStatusRespStatusesType0", None], data)

        statuses = _parse_statuses(d.pop("statuses"))

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
