from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelLoginResponse")


@_attrs_define
class ModelLoginResponse:
    """
    Attributes:
        access_token (str):
        onboarding_required (bool):
        password_invalidated (bool):
        refresh_token (str):
    """

    access_token: str
    onboarding_required: bool
    password_invalidated: bool
    refresh_token: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_token = self.access_token

        onboarding_required = self.onboarding_required

        password_invalidated = self.password_invalidated

        refresh_token = self.refresh_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_token": access_token,
                "onboarding_required": onboarding_required,
                "password_invalidated": password_invalidated,
                "refresh_token": refresh_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_token = d.pop("access_token")

        onboarding_required = d.pop("onboarding_required")

        password_invalidated = d.pop("password_invalidated")

        refresh_token = d.pop("refresh_token")

        model_login_response = cls(
            access_token=access_token,
            onboarding_required=onboarding_required,
            password_invalidated=password_invalidated,
            refresh_token=refresh_token,
        )

        model_login_response.additional_properties = d
        return model_login_response

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
