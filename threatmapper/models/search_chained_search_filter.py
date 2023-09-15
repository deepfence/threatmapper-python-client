from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_search_filter import SearchSearchFilter


T = TypeVar("T", bound="SearchChainedSearchFilter")


@_attrs_define
class SearchChainedSearchFilter:
    """
    Example:
        {'node_filter': {'in_field_filter': ['in_field_filter', 'in_field_filter'], 'filters': {'compare_filter':
            [{'greater_than': True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than': True, 'field_value':
            '', 'field_name': 'field_name'}], 'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter':
            {'order_fields': [{'size': 0, 'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True,
            'field_name': 'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}}, 'contains_in_array_filter':
            {'filter_in': {'key': ['', '']}}, 'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter':
            {'filter_in': {'key': ['', '']}}}, 'window': {'offset': 0, 'size': 6}}, 'next_filter': '', 'relation_ship':
            'relation_ship'}

    Attributes:
        node_filter (SearchSearchFilter):  Example: {'in_field_filter': ['in_field_filter', 'in_field_filter'],
            'filters': {'compare_filter': [{'greater_than': True, 'field_value': '', 'field_name': 'field_name'},
            {'greater_than': True, 'field_value': '', 'field_name': 'field_name'}], 'not_contains_filter': {'filter_in':
            {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0, 'descending': True, 'field_name':
            'field_name'}, {'size': 0, 'descending': True, 'field_name': 'field_name'}]}, 'contains_filter': {'filter_in':
            {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in': {'key': ['', '']}}, 'match_filter': {'filter_in':
            {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['', '']}}}, 'window': {'offset': 0, 'size':
            6}}.
        relation_ship (str):
        next_filter (Union[Unset, Any]):
    """

    node_filter: "SearchSearchFilter"
    relation_ship: str
    next_filter: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_filter = self.node_filter.to_dict()

        relation_ship = self.relation_ship
        next_filter = self.next_filter

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_filter": node_filter,
                "relation_ship": relation_ship,
            }
        )
        if next_filter is not UNSET:
            field_dict["next_filter"] = next_filter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.search_search_filter import SearchSearchFilter

        d = src_dict.copy()
        node_filter = SearchSearchFilter.from_dict(d.pop("node_filter"))

        relation_ship = d.pop("relation_ship")

        next_filter = d.pop("next_filter", UNSET)

        search_chained_search_filter = cls(
            node_filter=node_filter,
            relation_ship=relation_ship,
            next_filter=next_filter,
        )

        search_chained_search_filter.additional_properties = d
        return search_chained_search_filter

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
