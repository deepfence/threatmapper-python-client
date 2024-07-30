from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelGenerateLicenseResponse")


@_attrs_define
class ModelGenerateLicenseResponse:
    """
    Example:
        {'success': True, 'generate_license_link': 'generate_license_link', 'message': 'message'}

    Attributes:
        message (str):
        success (bool):
        generate_license_link (Union[Unset, str]):
    """

    message: str
    success: bool
    generate_license_link: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message

        success = self.success

        generate_license_link = self.generate_license_link

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "success": success,
            }
        )
        if generate_license_link is not UNSET:
            field_dict["generate_license_link"] = generate_license_link

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message")

        success = d.pop("success")

        generate_license_link = d.pop("generate_license_link", UNSET)

        model_generate_license_response = cls(
            message=message,
            success=success,
            generate_license_link=generate_license_link,
        )

        model_generate_license_response.additional_properties = d
        return model_generate_license_response

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
