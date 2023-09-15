from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reporters_compare_filter import ReportersCompareFilter
    from ..models.reporters_contains_filter import ReportersContainsFilter
    from ..models.reporters_match_filter import ReportersMatchFilter
    from ..models.reporters_order_filter import ReportersOrderFilter


T = TypeVar("T", bound="ReportersFieldsFilters")


@_attrs_define
class ReportersFieldsFilters:
    """
    Example:
        {'compare_filter': [{'greater_than': True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than':
            True, 'field_value': '', 'field_name': 'field_name'}], 'not_contains_filter': {'filter_in': {'key': ['', '']}},
            'order_filter': {'order_fields': [{'size': 0, 'descending': True, 'field_name': 'field_name'}, {'size': 0,
            'descending': True, 'field_name': 'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}},
            'contains_in_array_filter': {'filter_in': {'key': ['', '']}}, 'match_filter': {'filter_in': {'key': ['', '']}},
            'match_in_array_filter': {'filter_in': {'key': ['', '']}}}

    Attributes:
        contains_filter (ReportersContainsFilter):  Example: {'filter_in': {'key': ['', '']}}.
        match_filter (ReportersMatchFilter):  Example: {'filter_in': {'key': ['', '']}}.
        order_filter (ReportersOrderFilter):  Example: {'order_fields': [{'size': 0, 'descending': True, 'field_name':
            'field_name'}, {'size': 0, 'descending': True, 'field_name': 'field_name'}]}.
        compare_filter (Optional[List['ReportersCompareFilter']]):
        contains_in_array_filter (Union[Unset, ReportersContainsFilter]):  Example: {'filter_in': {'key': ['', '']}}.
        match_in_array_filter (Union[Unset, ReportersMatchFilter]):  Example: {'filter_in': {'key': ['', '']}}.
        not_contains_filter (Union[Unset, ReportersContainsFilter]):  Example: {'filter_in': {'key': ['', '']}}.
    """

    contains_filter: "ReportersContainsFilter"
    match_filter: "ReportersMatchFilter"
    order_filter: "ReportersOrderFilter"
    compare_filter: Optional[List["ReportersCompareFilter"]]
    contains_in_array_filter: Union[Unset, "ReportersContainsFilter"] = UNSET
    match_in_array_filter: Union[Unset, "ReportersMatchFilter"] = UNSET
    not_contains_filter: Union[Unset, "ReportersContainsFilter"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contains_filter = self.contains_filter.to_dict()

        match_filter = self.match_filter.to_dict()

        order_filter = self.order_filter.to_dict()

        if self.compare_filter is None:
            compare_filter = None
        else:
            compare_filter = []
            for compare_filter_item_data in self.compare_filter:
                compare_filter_item = compare_filter_item_data.to_dict()

                compare_filter.append(compare_filter_item)

        contains_in_array_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contains_in_array_filter, Unset):
            contains_in_array_filter = self.contains_in_array_filter.to_dict()

        match_in_array_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.match_in_array_filter, Unset):
            match_in_array_filter = self.match_in_array_filter.to_dict()

        not_contains_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.not_contains_filter, Unset):
            not_contains_filter = self.not_contains_filter.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contains_filter": contains_filter,
                "match_filter": match_filter,
                "order_filter": order_filter,
                "compare_filter": compare_filter,
            }
        )
        if contains_in_array_filter is not UNSET:
            field_dict["contains_in_array_filter"] = contains_in_array_filter
        if match_in_array_filter is not UNSET:
            field_dict["match_in_array_filter"] = match_in_array_filter
        if not_contains_filter is not UNSET:
            field_dict["not_contains_filter"] = not_contains_filter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reporters_compare_filter import ReportersCompareFilter
        from ..models.reporters_contains_filter import ReportersContainsFilter
        from ..models.reporters_match_filter import ReportersMatchFilter
        from ..models.reporters_order_filter import ReportersOrderFilter

        d = src_dict.copy()
        contains_filter = ReportersContainsFilter.from_dict(d.pop("contains_filter"))

        match_filter = ReportersMatchFilter.from_dict(d.pop("match_filter"))

        order_filter = ReportersOrderFilter.from_dict(d.pop("order_filter"))

        compare_filter = []
        _compare_filter = d.pop("compare_filter")
        for compare_filter_item_data in _compare_filter or []:
            compare_filter_item = ReportersCompareFilter.from_dict(compare_filter_item_data)

            compare_filter.append(compare_filter_item)

        _contains_in_array_filter = d.pop("contains_in_array_filter", UNSET)
        contains_in_array_filter: Union[Unset, ReportersContainsFilter]
        if isinstance(_contains_in_array_filter, Unset):
            contains_in_array_filter = UNSET
        else:
            contains_in_array_filter = ReportersContainsFilter.from_dict(_contains_in_array_filter)

        _match_in_array_filter = d.pop("match_in_array_filter", UNSET)
        match_in_array_filter: Union[Unset, ReportersMatchFilter]
        if isinstance(_match_in_array_filter, Unset):
            match_in_array_filter = UNSET
        else:
            match_in_array_filter = ReportersMatchFilter.from_dict(_match_in_array_filter)

        _not_contains_filter = d.pop("not_contains_filter", UNSET)
        not_contains_filter: Union[Unset, ReportersContainsFilter]
        if isinstance(_not_contains_filter, Unset):
            not_contains_filter = UNSET
        else:
            not_contains_filter = ReportersContainsFilter.from_dict(_not_contains_filter)

        reporters_fields_filters = cls(
            contains_filter=contains_filter,
            match_filter=match_filter,
            order_filter=order_filter,
            compare_filter=compare_filter,
            contains_in_array_filter=contains_in_array_filter,
            match_in_array_filter=match_in_array_filter,
            not_contains_filter=not_contains_filter,
        )

        reporters_fields_filters.additional_properties = d
        return reporters_fields_filters

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
