from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchResultGroup")


@_attrs_define
class SearchResultGroup:
    """
    Example:
        {'severity': 'severity', 'count': 0, 'name': 'name'}

    Attributes:
        count (Union[Unset, int]):
        name (Union[Unset, str]):
        severity (Union[Unset, str]):
    """

    count: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

        name = self.name

        severity = self.severity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if name is not UNSET:
            field_dict["name"] = name
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count", UNSET)

        name = d.pop("name", UNSET)

        severity = d.pop("severity", UNSET)

        search_result_group = cls(
            count=count,
            name=name,
            severity=severity,
        )

        search_result_group.additional_properties = d
        return search_result_group

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
