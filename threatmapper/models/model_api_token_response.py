import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelAPITokenResponse")


@_attrs_define
class ModelAPITokenResponse:
    """
    Example:
        {'company_id': 0, 'api_token': 'api_token', 'name': 'name', 'created_at': datetime.datetime(2000, 1, 23, 4, 56,
            7, tzinfo=datetime.timezone.utc), 'id': 1, 'created_by_user_id': 6}

    Attributes:
        api_token (Union[Unset, str]):
        company_id (Union[Unset, int]):
        created_at (Union[Unset, datetime.datetime]):
        created_by_user_id (Union[Unset, int]):
        id (Union[Unset, int]):
        name (Union[Unset, str]):
    """

    api_token: Union[Unset, str] = UNSET
    company_id: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    created_by_user_id: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_token = self.api_token
        company_id = self.company_id
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by_user_id = self.created_by_user_id
        id = self.id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_token is not UNSET:
            field_dict["api_token"] = api_token
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_user_id is not UNSET:
            field_dict["created_by_user_id"] = created_by_user_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        api_token = d.pop("api_token", UNSET)

        company_id = d.pop("company_id", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        created_by_user_id = d.pop("created_by_user_id", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        model_api_token_response = cls(
            api_token=api_token,
            company_id=company_id,
            created_at=created_at,
            created_by_user_id=created_by_user_id,
            id=id,
            name=name,
        )

        model_api_token_response.additional_properties = d
        return model_api_token_response

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
