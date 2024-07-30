from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CompletionCompletionNodeFieldRes")


@_attrs_define
class CompletionCompletionNodeFieldRes:
    """
    Example:
        {'possible_values': ['possible_values', 'possible_values']}

    Attributes:
        possible_values (Union[List[str], None]):
    """

    possible_values: Union[List[str], None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        possible_values: Union[List[str], None]
        if isinstance(self.possible_values, list):
            possible_values = self.possible_values

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

        def _parse_possible_values(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                possible_values_type_0 = cast(List[str], data)

                return possible_values_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        possible_values = _parse_possible_values(d.pop("possible_values"))

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
