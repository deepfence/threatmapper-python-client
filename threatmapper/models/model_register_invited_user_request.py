from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelRegisterInvitedUserRequest")


@_attrs_define
class ModelRegisterInvitedUserRequest:
    """
    Example:
        {'password': 'password', 'code': 'code', 'namespace': 'namespace', 'last_name': 'last_name', 'first_name':
            'first_name', 'is_temporary_password': True}

    Attributes:
        code (str):
        first_name (str):
        last_name (str):
        namespace (str):
        password (str):
        is_temporary_password (Union[Unset, bool]):
    """

    code: str
    first_name: str
    last_name: str
    namespace: str
    password: str
    is_temporary_password: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        first_name = self.first_name
        last_name = self.last_name
        namespace = self.namespace
        password = self.password
        is_temporary_password = self.is_temporary_password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "first_name": first_name,
                "last_name": last_name,
                "namespace": namespace,
                "password": password,
            }
        )
        if is_temporary_password is not UNSET:
            field_dict["is_temporary_password"] = is_temporary_password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        namespace = d.pop("namespace")

        password = d.pop("password")

        is_temporary_password = d.pop("is_temporary_password", UNSET)

        model_register_invited_user_request = cls(
            code=code,
            first_name=first_name,
            last_name=last_name,
            namespace=namespace,
            password=password,
            is_temporary_password=is_temporary_password,
        )

        model_register_invited_user_request.additional_properties = d
        return model_register_invited_user_request

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
