from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelPasswordResetVerifyRequest")


@_attrs_define
class ModelPasswordResetVerifyRequest:
    """
    Example:
        {'password': 'password', 'code': 'code', 'namespace': 'namespace'}

    Attributes:
        code (str):
        namespace (str):
        password (str):
    """

    code: str
    namespace: str
    password: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        namespace = self.namespace

        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "namespace": namespace,
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code")

        namespace = d.pop("namespace")

        password = d.pop("password")

        model_password_reset_verify_request = cls(
            code=code,
            namespace=namespace,
            password=password,
        )

        model_password_reset_verify_request.additional_properties = d
        return model_password_reset_verify_request

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
