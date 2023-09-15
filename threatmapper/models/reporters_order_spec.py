from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportersOrderSpec")


@_attrs_define
class ReportersOrderSpec:
    """
    Example:
        {'size': 0, 'descending': True, 'field_name': 'field_name'}

    Attributes:
        descending (bool):
        field_name (str):
        size (Union[Unset, int]):
    """

    descending: bool
    field_name: str
    size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        descending = self.descending
        field_name = self.field_name
        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "descending": descending,
                "field_name": field_name,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        descending = d.pop("descending")

        field_name = d.pop("field_name")

        size = d.pop("size", UNSET)

        reporters_order_spec = cls(
            descending=descending,
            field_name=field_name,
            size=size,
        )

        reporters_order_spec.additional_properties = d
        return reporters_order_spec

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
