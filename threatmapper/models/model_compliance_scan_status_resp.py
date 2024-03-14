from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_compliance_scan_info import ModelComplianceScanInfo


T = TypeVar("T", bound="ModelComplianceScanStatusResp")


@_attrs_define
class ModelComplianceScanStatusResp:
    """
    Attributes:
        statuses (Union[List['ModelComplianceScanInfo'], None]):
    """

    statuses: Union[List["ModelComplianceScanInfo"], None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        statuses: Union[List[Dict[str, Any]], None]
        if isinstance(self.statuses, list):
            statuses = []
            for statuses_type_0_item_data in self.statuses:
                statuses_type_0_item = statuses_type_0_item_data.to_dict()
                statuses.append(statuses_type_0_item)

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
        from ..models.model_compliance_scan_info import ModelComplianceScanInfo

        d = src_dict.copy()

        def _parse_statuses(data: object) -> Union[List["ModelComplianceScanInfo"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                statuses_type_0 = []
                _statuses_type_0 = data
                for statuses_type_0_item_data in _statuses_type_0:
                    statuses_type_0_item = ModelComplianceScanInfo.from_dict(statuses_type_0_item_data)

                    statuses_type_0.append(statuses_type_0_item)

                return statuses_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelComplianceScanInfo"], None], data)

        statuses = _parse_statuses(d.pop("statuses"))

        model_compliance_scan_status_resp = cls(
            statuses=statuses,
        )

        model_compliance_scan_status_resp.additional_properties = d
        return model_compliance_scan_status_resp

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
