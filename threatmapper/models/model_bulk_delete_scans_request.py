from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_bulk_delete_scans_request_scan_type import ModelBulkDeleteScansRequestScanType

if TYPE_CHECKING:
    from ..models.reporters_fields_filters import ReportersFieldsFilters


T = TypeVar("T", bound="ModelBulkDeleteScansRequest")


@_attrs_define
class ModelBulkDeleteScansRequest:
    """
    Example:
        {'scan_type': 'Secret', 'filters': {'compare_filter': [{'greater_than': True, 'field_value': '', 'field_name':
            'field_name'}, {'greater_than': True, 'field_value': '', 'field_name': 'field_name'}], 'not_contains_filter':
            {'filter_in': {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0, 'descending': True,
            'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name': 'field_name'}]}, 'contains_filter':
            {'filter_in': {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in': {'key': ['', '']}}, 'match_filter':
            {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['', '']}}}}

    Attributes:
        filters (ReportersFieldsFilters):  Example: {'compare_filter': [{'greater_than': True, 'field_value': '',
            'field_name': 'field_name'}, {'greater_than': True, 'field_value': '', 'field_name': 'field_name'}],
            'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0,
            'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name': 'field_name'}]},
            'contains_filter': {'filter_in': {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in': {'key': ['',
            '']}}, 'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['',
            '']}}}.
        scan_type (ModelBulkDeleteScansRequestScanType):
    """

    filters: "ReportersFieldsFilters"
    scan_type: ModelBulkDeleteScansRequestScanType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filters = self.filters.to_dict()

        scan_type = self.scan_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
                "scan_type": scan_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reporters_fields_filters import ReportersFieldsFilters

        d = src_dict.copy()
        filters = ReportersFieldsFilters.from_dict(d.pop("filters"))

        scan_type = ModelBulkDeleteScansRequestScanType(d.pop("scan_type"))

        model_bulk_delete_scans_request = cls(
            filters=filters,
            scan_type=scan_type,
        )

        model_bulk_delete_scans_request.additional_properties = d
        return model_bulk_delete_scans_request

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
