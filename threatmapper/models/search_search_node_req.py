from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_fetch_window import ModelFetchWindow
    from ..models.search_chained_search_filter import SearchChainedSearchFilter
    from ..models.search_search_filter import SearchSearchFilter


T = TypeVar("T", bound="SearchSearchNodeReq")


@_attrs_define
class SearchSearchNodeReq:
    """
    Example:
        {'node_filter': {'in_field_filter': ['in_field_filter', 'in_field_filter'], 'filters': {'compare_filter':
            [{'greater_than': True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than': True, 'field_value':
            '', 'field_name': 'field_name'}], 'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter':
            {'order_fields': [{'size': 0, 'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True,
            'field_name': 'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}}, 'contains_in_array_filter':
            {'filter_in': {'key': ['', '']}}, 'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter':
            {'filter_in': {'key': ['', '']}}}, 'window': {'offset': 0, 'size': 6}}, 'extended_node_filter':
            {'in_field_filter': ['in_field_filter', 'in_field_filter'], 'filters': {'compare_filter': [{'greater_than':
            True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than': True, 'field_value': '', 'field_name':
            'field_name'}], 'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter': {'order_fields':
            [{'size': 0, 'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name':
            'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in':
            {'key': ['', '']}}, 'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in':
            {'key': ['', '']}}}, 'window': {'offset': 0, 'size': 6}}, 'related_node_filter': {'node_filter':
            {'in_field_filter': ['in_field_filter', 'in_field_filter'], 'filters': {'compare_filter': [{'greater_than':
            True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than': True, 'field_value': '', 'field_name':
            'field_name'}], 'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter': {'order_fields':
            [{'size': 0, 'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name':
            'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in':
            {'key': ['', '']}}, 'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in':
            {'key': ['', '']}}}, 'window': {'offset': 0, 'size': 6}}, 'next_filter': None, 'relation_ship':
            'relation_ship'}, 'window': {'offset': 0, 'size': 6}}

    Attributes:
        node_filter (SearchSearchFilter):  Example: {'in_field_filter': ['in_field_filter', 'in_field_filter'],
            'filters': {'compare_filter': [{'greater_than': True, 'field_value': '', 'field_name': 'field_name'},
            {'greater_than': True, 'field_value': '', 'field_name': 'field_name'}], 'not_contains_filter': {'filter_in':
            {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0, 'descending': True, 'field_name':
            'field_name'}, {'size': 0, 'descending': True, 'field_name': 'field_name'}]}, 'contains_filter': {'filter_in':
            {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in': {'key': ['', '']}}, 'match_filter': {'filter_in':
            {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['', '']}}}, 'window': {'offset': 0, 'size':
            6}}.
        window (ModelFetchWindow):  Example: {'offset': 0, 'size': 6}.
        extended_node_filter (Union[Unset, SearchSearchFilter]):  Example: {'in_field_filter': ['in_field_filter',
            'in_field_filter'], 'filters': {'compare_filter': [{'greater_than': True, 'field_value': '', 'field_name':
            'field_name'}, {'greater_than': True, 'field_value': '', 'field_name': 'field_name'}], 'not_contains_filter':
            {'filter_in': {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0, 'descending': True,
            'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name': 'field_name'}]}, 'contains_filter':
            {'filter_in': {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in': {'key': ['', '']}}, 'match_filter':
            {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['', '']}}}, 'window':
            {'offset': 0, 'size': 6}}.
        related_node_filter (Union[Unset, SearchChainedSearchFilter]):  Example: {'node_filter': {'in_field_filter':
            ['in_field_filter', 'in_field_filter'], 'filters': {'compare_filter': [{'greater_than': True, 'field_value': '',
            'field_name': 'field_name'}, {'greater_than': True, 'field_value': '', 'field_name': 'field_name'}],
            'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0,
            'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name': 'field_name'}]},
            'contains_filter': {'filter_in': {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in': {'key': ['',
            '']}}, 'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['',
            '']}}}, 'window': {'offset': 0, 'size': 6}}, 'next_filter': None, 'relation_ship': 'relation_ship'}.
    """

    node_filter: "SearchSearchFilter"
    window: "ModelFetchWindow"
    extended_node_filter: Union[Unset, "SearchSearchFilter"] = UNSET
    related_node_filter: Union[Unset, "SearchChainedSearchFilter"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_filter = self.node_filter.to_dict()

        window = self.window.to_dict()

        extended_node_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extended_node_filter, Unset):
            extended_node_filter = self.extended_node_filter.to_dict()

        related_node_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.related_node_filter, Unset):
            related_node_filter = self.related_node_filter.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_filter": node_filter,
                "window": window,
            }
        )
        if extended_node_filter is not UNSET:
            field_dict["extended_node_filter"] = extended_node_filter
        if related_node_filter is not UNSET:
            field_dict["related_node_filter"] = related_node_filter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_fetch_window import ModelFetchWindow
        from ..models.search_chained_search_filter import SearchChainedSearchFilter
        from ..models.search_search_filter import SearchSearchFilter

        d = src_dict.copy()
        node_filter = SearchSearchFilter.from_dict(d.pop("node_filter"))

        window = ModelFetchWindow.from_dict(d.pop("window"))

        _extended_node_filter = d.pop("extended_node_filter", UNSET)
        extended_node_filter: Union[Unset, SearchSearchFilter]
        if isinstance(_extended_node_filter, Unset):
            extended_node_filter = UNSET
        else:
            extended_node_filter = SearchSearchFilter.from_dict(_extended_node_filter)

        _related_node_filter = d.pop("related_node_filter", UNSET)
        related_node_filter: Union[Unset, SearchChainedSearchFilter]
        if isinstance(_related_node_filter, Unset):
            related_node_filter = UNSET
        else:
            related_node_filter = SearchChainedSearchFilter.from_dict(_related_node_filter)

        search_search_node_req = cls(
            node_filter=node_filter,
            window=window,
            extended_node_filter=extended_node_filter,
            related_node_filter=related_node_filter,
        )

        search_search_node_req.additional_properties = d
        return search_search_node_req

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
