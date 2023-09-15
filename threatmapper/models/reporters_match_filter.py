from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reporters_match_filter_filter_in import ReportersMatchFilterFilterIn


T = TypeVar("T", bound="ReportersMatchFilter")


@_attrs_define
class ReportersMatchFilter:
    """
    Example:
        {'filter_in': {'key': ['', '']}}

    Attributes:
        filter_in (Optional[ReportersMatchFilterFilterIn]):
    """

    filter_in: Optional["ReportersMatchFilterFilterIn"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filter_in = self.filter_in.to_dict() if self.filter_in else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter_in": filter_in,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reporters_match_filter_filter_in import ReportersMatchFilterFilterIn

        d = src_dict.copy()
        _filter_in = d.pop("filter_in")
        filter_in: Optional[ReportersMatchFilterFilterIn]
        if _filter_in is None:
            filter_in = None
        else:
            filter_in = ReportersMatchFilterFilterIn.from_dict(_filter_in)

        reporters_match_filter = cls(
            filter_in=filter_in,
        )

        reporters_match_filter.additional_properties = d
        return reporters_match_filter

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
