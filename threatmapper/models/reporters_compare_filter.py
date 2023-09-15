from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReportersCompareFilter")


@_attrs_define
class ReportersCompareFilter:
    """
    Example:
        {'greater_than': True, 'field_value': '', 'field_name': 'field_name'}

    Attributes:
        field_name (str):
        field_value (Any):
        greater_than (bool):
    """

    field_name: str
    field_value: Any
    greater_than: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_name = self.field_name
        field_value = self.field_value
        greater_than = self.greater_than

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_name": field_name,
                "field_value": field_value,
                "greater_than": greater_than,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_name = d.pop("field_name")

        field_value = d.pop("field_value")

        greater_than = d.pop("greater_than")

        reporters_compare_filter = cls(
            field_name=field_name,
            field_value=field_value,
            greater_than=greater_than,
        )

        reporters_compare_filter.additional_properties = d
        return reporters_compare_filter

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
