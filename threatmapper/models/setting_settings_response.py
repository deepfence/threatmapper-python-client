from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SettingSettingsResponse")


@_attrs_define
class SettingSettingsResponse:
    """
    Example:
        {'description': 'description', 'id': 0, 'label': 'label', 'value': '', 'key': 'key'}

    Attributes:
        description (str):
        id (int):
        key (str):
        label (str):
        value (Any):
    """

    description: str
    id: int
    key: str
    label: str
    value: Any
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        id = self.id

        key = self.key

        label = self.label

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "id": id,
                "key": key,
                "label": label,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        id = d.pop("id")

        key = d.pop("key")

        label = d.pop("label")

        value = d.pop("value")

        setting_settings_response = cls(
            description=description,
            id=id,
            key=key,
            label=label,
            value=value,
        )

        setting_settings_response.additional_properties = d
        return setting_settings_response

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
