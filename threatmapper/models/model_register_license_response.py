from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelRegisterLicenseResponse")


@_attrs_define
class ModelRegisterLicenseResponse:
    """
    Attributes:
        email_domain (str):
        license_key (str):
    """

    email_domain: str
    license_key: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email_domain = self.email_domain

        license_key = self.license_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email_domain": email_domain,
                "license_key": license_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email_domain = d.pop("email_domain")

        license_key = d.pop("license_key")

        model_register_license_response = cls(
            email_domain=email_domain,
            license_key=license_key,
        )

        model_register_license_response.additional_properties = d
        return model_register_license_response

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
