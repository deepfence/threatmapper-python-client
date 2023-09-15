from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelEmailConfigurationResp")


@_attrs_define
class ModelEmailConfigurationResp:
    """
    Example:
        {'email_id': 'email_id', 'smtp': 'smtp', 'port': 'port', 'email_provider': 'email_provider', 'id': 6,
            'created_by_user_id': 0, 'ses_region': 'ses_region'}

    Attributes:
        created_by_user_id (Union[Unset, int]):
        email_id (Union[Unset, str]):
        email_provider (Union[Unset, str]):
        id (Union[Unset, int]):
        port (Union[Unset, str]):
        ses_region (Union[Unset, str]):
        smtp (Union[Unset, str]):
    """

    created_by_user_id: Union[Unset, int] = UNSET
    email_id: Union[Unset, str] = UNSET
    email_provider: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    port: Union[Unset, str] = UNSET
    ses_region: Union[Unset, str] = UNSET
    smtp: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_by_user_id = self.created_by_user_id
        email_id = self.email_id
        email_provider = self.email_provider
        id = self.id
        port = self.port
        ses_region = self.ses_region
        smtp = self.smtp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_by_user_id is not UNSET:
            field_dict["created_by_user_id"] = created_by_user_id
        if email_id is not UNSET:
            field_dict["email_id"] = email_id
        if email_provider is not UNSET:
            field_dict["email_provider"] = email_provider
        if id is not UNSET:
            field_dict["id"] = id
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
        created_by_user_id = d.pop("created_by_user_id", UNSET)

        email_id = d.pop("email_id", UNSET)

        email_provider = d.pop("email_provider", UNSET)

        id = d.pop("id", UNSET)

        port = d.pop("port", UNSET)

        ses_region = d.pop("ses_region", UNSET)

        smtp = d.pop("smtp", UNSET)

        model_email_configuration_resp = cls(
            created_by_user_id=created_by_user_id,
            email_id=email_id,
            email_provider=email_provider,
            id=id,
            port=port,
            ses_region=ses_region,
            smtp=smtp,
        )

        model_email_configuration_resp.additional_properties = d
        return model_email_configuration_resp

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
