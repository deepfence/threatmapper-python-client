from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_setting_update_request_key import ModelSettingUpdateRequestKey

T = TypeVar("T", bound="ModelSettingUpdateRequest")


@_attrs_define
class ModelSettingUpdateRequest:
    """
    Attributes:
        key (ModelSettingUpdateRequestKey):
        value (str):
    """

    key: ModelSettingUpdateRequestKey
    value: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key.value

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = ModelSettingUpdateRequestKey(d.pop("key"))

        value = d.pop("value")

        model_setting_update_request = cls(
            key=key,
            value=value,
        )

        model_setting_update_request.additional_properties = d
        return model_setting_update_request

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
