from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_fetch_window import ModelFetchWindow
    from ..models.reporters_fields_filters import ReportersFieldsFilters


T = TypeVar("T", bound="SearchSearchFilter")


@_attrs_define
class SearchSearchFilter:
    """
    Example:
        {'in_field_filter': ['in_field_filter', 'in_field_filter'], 'filters': {'compare_filter': [{'greater_than':
            True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than': True, 'field_value': '', 'field_name':
            'field_name'}], 'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter': {'order_fields':
            [{'size': 0, 'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name':
            'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in':
            {'key': ['', '']}}, 'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in':
            {'key': ['', '']}}}, 'window': {'offset': 0, 'size': 6}}

    Attributes:
        filters (ReportersFieldsFilters):  Example: {'compare_filter': [{'greater_than': True, 'field_value': '',
            'field_name': 'field_name'}, {'greater_than': True, 'field_value': '', 'field_name': 'field_name'}],
            'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0,
            'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name': 'field_name'}]},
            'contains_filter': {'filter_in': {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in': {'key': ['',
            '']}}, 'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['',
            '']}}}.
        in_field_filter (Union[List[str], None]):
        window (ModelFetchWindow):  Example: {'offset': 0, 'size': 6}.
    """

    filters: "ReportersFieldsFilters"
    in_field_filter: Union[List[str], None]
    window: "ModelFetchWindow"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filters = self.filters.to_dict()

        in_field_filter: Union[List[str], None]
        if isinstance(self.in_field_filter, list):
            in_field_filter = self.in_field_filter

        else:
            in_field_filter = self.in_field_filter

        window = self.window.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
                "in_field_filter": in_field_filter,
                "window": window,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_fetch_window import ModelFetchWindow
        from ..models.reporters_fields_filters import ReportersFieldsFilters

        d = src_dict.copy()
        filters = ReportersFieldsFilters.from_dict(d.pop("filters"))

        def _parse_in_field_filter(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                in_field_filter_type_0 = cast(List[str], data)

                return in_field_filter_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        in_field_filter = _parse_in_field_filter(d.pop("in_field_filter"))

        window = ModelFetchWindow.from_dict(d.pop("window"))

        search_search_filter = cls(
            filters=filters,
            in_field_filter=in_field_filter,
            window=window,
        )

        search_search_filter.additional_properties = d
        return search_search_filter

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
