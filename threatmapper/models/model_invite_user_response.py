from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelInviteUserResponse")


@_attrs_define
class ModelInviteUserResponse:
    """
    Example:
        {'invite_expiry_hours': 0, 'invite_url': 'invite_url', 'message': 'message'}

    Attributes:
        invite_expiry_hours (Union[Unset, int]):
        invite_url (Union[Unset, str]):
        message (Union[Unset, str]):
    """

    invite_expiry_hours: Union[Unset, int] = UNSET
    invite_url: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invite_expiry_hours = self.invite_expiry_hours

        invite_url = self.invite_url

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invite_expiry_hours is not UNSET:
            field_dict["invite_expiry_hours"] = invite_expiry_hours
        if invite_url is not UNSET:
            field_dict["invite_url"] = invite_url
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invite_expiry_hours = d.pop("invite_expiry_hours", UNSET)

        invite_url = d.pop("invite_url", UNSET)

        message = d.pop("message", UNSET)

        model_invite_user_response = cls(
            invite_expiry_hours=invite_expiry_hours,
            invite_url=invite_url,
            message=message,
        )

        model_invite_user_response.additional_properties = d
        return model_invite_user_response

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
