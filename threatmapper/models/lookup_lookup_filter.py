from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_fetch_window import ModelFetchWindow


T = TypeVar("T", bound="LookupLookupFilter")


@_attrs_define
class LookupLookupFilter:
    """
    Example:
        {'in_field_filter': ['in_field_filter', 'in_field_filter'], 'window': {'offset': 0, 'size': 6}, 'node_ids':
            ['node_ids', 'node_ids']}

    Attributes:
        window (ModelFetchWindow):  Example: {'offset': 0, 'size': 6}.
        in_field_filter (Optional[List[str]]):
        node_ids (Optional[List[str]]):
    """

    window: "ModelFetchWindow"
    in_field_filter: Optional[List[str]]
    node_ids: Optional[List[str]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        window = self.window.to_dict()

        if self.in_field_filter is None:
            in_field_filter = None
        else:
            in_field_filter = self.in_field_filter

        if self.node_ids is None:
            node_ids = None
        else:
            node_ids = self.node_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "window": window,
                "in_field_filter": in_field_filter,
                "node_ids": node_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_fetch_window import ModelFetchWindow

        d = src_dict.copy()
        window = ModelFetchWindow.from_dict(d.pop("window"))

        in_field_filter = cast(List[str], d.pop("in_field_filter"))

        node_ids = cast(List[str], d.pop("node_ids"))

        lookup_lookup_filter = cls(
            window=window,
            in_field_filter=in_field_filter,
            node_ids=node_ids,
        )

        lookup_lookup_filter.additional_properties = d
        return lookup_lookup_filter

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
