from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IngestersSecretRule")


@_attrs_define
class IngestersSecretRule:
    """
    Example:
        {'part': 'part', 'name': 'name', 'signature_to_match': 'signature_to_match', 'id': 5}

    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        part (Union[Unset, str]):
        signature_to_match (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    part: Union[Unset, str] = UNSET
    signature_to_match: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        part = self.part
        signature_to_match = self.signature_to_match

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if part is not UNSET:
            field_dict["part"] = part
        if signature_to_match is not UNSET:
            field_dict["signature_to_match"] = signature_to_match

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        part = d.pop("part", UNSET)

        signature_to_match = d.pop("signature_to_match", UNSET)

        ingesters_secret_rule = cls(
            id=id,
            name=name,
            part=part,
            signature_to_match=signature_to_match,
        )

        ingesters_secret_rule.additional_properties = d
        return ingesters_secret_rule

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
