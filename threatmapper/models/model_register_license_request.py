from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelRegisterLicenseRequest")


@_attrs_define
class ModelRegisterLicenseRequest:
    """
    Example:
        {'email': 'email', 'license_key': 'license_key'}

    Attributes:
        license_key (str):
        email (Union[Unset, str]):
    """

    license_key: str
    email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        license_key = self.license_key

        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "license_key": license_key,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        license_key = d.pop("license_key")

        email = d.pop("email", UNSET)

        model_register_license_request = cls(
            license_key=license_key,
            email=email,
        )

        model_register_license_request.additional_properties = d
        return model_register_license_request

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
