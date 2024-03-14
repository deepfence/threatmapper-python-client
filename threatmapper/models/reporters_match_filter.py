from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reporters_match_filter_filter_in_type_0 import ReportersMatchFilterFilterInType0


T = TypeVar("T", bound="ReportersMatchFilter")


@_attrs_define
class ReportersMatchFilter:
    """
    Attributes:
        filter_in (Union['ReportersMatchFilterFilterInType0', None]):
    """

    filter_in: Union["ReportersMatchFilterFilterInType0", None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.reporters_match_filter_filter_in_type_0 import ReportersMatchFilterFilterInType0

        filter_in: Union[Dict[str, Any], None]
        if isinstance(self.filter_in, ReportersMatchFilterFilterInType0):
            filter_in = self.filter_in.to_dict()
        else:
            filter_in = self.filter_in

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
        from ..models.reporters_match_filter_filter_in_type_0 import ReportersMatchFilterFilterInType0

        d = src_dict.copy()

        def _parse_filter_in(data: object) -> Union["ReportersMatchFilterFilterInType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filter_in_type_0 = ReportersMatchFilterFilterInType0.from_dict(data)

                return filter_in_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ReportersMatchFilterFilterInType0", None], data)

        filter_in = _parse_filter_in(d.pop("filter_in"))

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
