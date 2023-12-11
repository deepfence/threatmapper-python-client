from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CompletionCompletionNodeFieldRes")


@_attrs_define
class CompletionCompletionNodeFieldRes:
    """
    Example:
        {'possible_values': ['possible_values', 'possible_values']}

    Attributes:
        possible_values (Optional[List[str]]):
    """

    possible_values: Optional[List[str]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if self.possible_values is None:
            possible_values = None
        else:
            possible_values = self.possible_values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "possible_values": possible_values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        possible_values = cast(List[str], d.pop("possible_values"))

        completion_completion_node_field_res = cls(
            possible_values=possible_values,
        )

        completion_completion_node_field_res.additional_properties = d
        return completion_completion_node_field_res

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
