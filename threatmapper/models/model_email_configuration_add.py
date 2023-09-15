from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelEmailConfigurationAdd")


@_attrs_define
class ModelEmailConfigurationAdd:
    """
    Example:
        {'email_id': 'email_id', 'password': 'password', 'smtp': 'smtp', 'port': 'port', 'email_provider':
            'email_provider', 'amazon_secret_key': 'amazon_secret_key', 'amazon_access_key': 'amazon_access_key',
            'created_by_user_id': 0, 'ses_region': 'ses_region'}

    Attributes:
        amazon_access_key (Union[Unset, str]):
        amazon_secret_key (Union[Unset, str]):
        created_by_user_id (Union[Unset, int]):
        email_id (Union[Unset, str]):
        email_provider (Union[Unset, str]):
        password (Union[Unset, str]):
        port (Union[Unset, str]):
        ses_region (Union[Unset, str]):
        smtp (Union[Unset, str]):
    """

    amazon_access_key: Union[Unset, str] = UNSET
    amazon_secret_key: Union[Unset, str] = UNSET
    created_by_user_id: Union[Unset, int] = UNSET
    email_id: Union[Unset, str] = UNSET
    email_provider: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    port: Union[Unset, str] = UNSET
    ses_region: Union[Unset, str] = UNSET
    smtp: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon_access_key = self.amazon_access_key
        amazon_secret_key = self.amazon_secret_key
        created_by_user_id = self.created_by_user_id
        email_id = self.email_id
        email_provider = self.email_provider
        password = self.password
        port = self.port
        ses_region = self.ses_region
        smtp = self.smtp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amazon_access_key is not UNSET:
            field_dict["amazon_access_key"] = amazon_access_key
        if amazon_secret_key is not UNSET:
            field_dict["amazon_secret_key"] = amazon_secret_key
        if created_by_user_id is not UNSET:
            field_dict["created_by_user_id"] = created_by_user_id
        if email_id is not UNSET:
            field_dict["email_id"] = email_id
        if email_provider is not UNSET:
            field_dict["email_provider"] = email_provider
        if password is not UNSET:
            field_dict["password"] = password
        if port is not UNSET:
            field_dict["port"] = port
        if ses_region is not UNSET:
            field_dict["ses_region"] = ses_region
        if smtp is not UNSET:
            field_dict["smtp"] = smtp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amazon_access_key = d.pop("amazon_access_key", UNSET)

        amazon_secret_key = d.pop("amazon_secret_key", UNSET)

        created_by_user_id = d.pop("created_by_user_id", UNSET)

        email_id = d.pop("email_id", UNSET)

        email_provider = d.pop("email_provider", UNSET)

        password = d.pop("password", UNSET)

        port = d.pop("port", UNSET)

        ses_region = d.pop("ses_region", UNSET)

        smtp = d.pop("smtp", UNSET)

        model_email_configuration_add = cls(
            amazon_access_key=amazon_access_key,
            amazon_secret_key=amazon_secret_key,
            created_by_user_id=created_by_user_id,
            email_id=email_id,
            email_provider=email_provider,
            password=password,
            port=port,
            ses_region=ses_region,
            smtp=smtp,
        )

        model_email_configuration_add.additional_properties = d
        return model_email_configuration_add

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
