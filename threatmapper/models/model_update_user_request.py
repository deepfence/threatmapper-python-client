from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_update_user_request_role import ModelUpdateUserRequestRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelUpdateUserRequest")


@_attrs_define
class ModelUpdateUserRequest:
    """
    Attributes:
        first_name (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        last_name (Union[Unset, str]):
        role (Union[Unset, ModelUpdateUserRequestRole]):
    """

    first_name: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    last_name: Union[Unset, str] = UNSET
    role: Union[Unset, ModelUpdateUserRequestRole] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name

        is_active = self.is_active

        last_name = self.last_name

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first_name = d.pop("first_name", UNSET)

        is_active = d.pop("is_active", UNSET)

        last_name = d.pop("last_name", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, ModelUpdateUserRequestRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = ModelUpdateUserRequestRole(_role)

        model_update_user_request = cls(
            first_name=first_name,
            is_active=is_active,
            last_name=last_name,
            role=role,
        )

        model_update_user_request.additional_properties = d
        return model_update_user_request

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
