from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelUpdateUserPasswordRequest")


@_attrs_define
class ModelUpdateUserPasswordRequest:
    """
    Example:
        {'old_password': 'old_password', 'new_password': 'new_password'}

    Attributes:
        new_password (str):
        old_password (str):
    """

    new_password: str
    old_password: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        new_password = self.new_password
        old_password = self.old_password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "new_password": new_password,
                "old_password": old_password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        new_password = d.pop("new_password")

        old_password = d.pop("old_password")

        model_update_user_password_request = cls(
            new_password=new_password,
            old_password=old_password,
        )

        model_update_user_password_request.additional_properties = d
        return model_update_user_password_request

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
