from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_node_identifier import ModelNodeIdentifier
    from ..models.reporters_fields_filters import ReportersFieldsFilters


T = TypeVar("T", bound="ModelIntegrationFilters")


@_attrs_define
class ModelIntegrationFilters:
    """
    Example:
        {'fields_filters': {'compare_filter': [{'greater_than': True, 'field_value': '', 'field_name': 'field_name'},
            {'greater_than': True, 'field_value': '', 'field_name': 'field_name'}], 'not_contains_filter': {'filter_in':
            {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0, 'descending': True, 'field_name':
            'field_name'}, {'size': 0, 'descending': True, 'field_name': 'field_name'}]}, 'contains_filter': {'filter_in':
            {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in': {'key': ['', '']}}, 'match_filter': {'filter_in':
            {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['', '']}}}, 'node_ids': [{'node_type':
            'image', 'node_id': 'node_id'}, {'node_type': 'image', 'node_id': 'node_id'}]}

    Attributes:
        fields_filters (Union[Unset, ReportersFieldsFilters]):  Example: {'compare_filter': [{'greater_than': True,
            'field_value': '', 'field_name': 'field_name'}, {'greater_than': True, 'field_value': '', 'field_name':
            'field_name'}], 'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter': {'order_fields':
            [{'size': 0, 'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name':
            'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in':
            {'key': ['', '']}}, 'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in':
            {'key': ['', '']}}}.
        node_ids (Optional[List['ModelNodeIdentifier']]):
    """

    node_ids: Optional[List["ModelNodeIdentifier"]]
    fields_filters: Union[Unset, "ReportersFieldsFilters"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fields_filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fields_filters, Unset):
            fields_filters = self.fields_filters.to_dict()

        if self.node_ids is None:
            node_ids = None
        else:
            node_ids = []
            for node_ids_item_data in self.node_ids:
                node_ids_item = node_ids_item_data.to_dict()

                node_ids.append(node_ids_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_ids": node_ids,
            }
        )
        if fields_filters is not UNSET:
            field_dict["fields_filters"] = fields_filters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_node_identifier import ModelNodeIdentifier
        from ..models.reporters_fields_filters import ReportersFieldsFilters

        d = src_dict.copy()
        _fields_filters = d.pop("fields_filters", UNSET)
        fields_filters: Union[Unset, ReportersFieldsFilters]
        if isinstance(_fields_filters, Unset):
            fields_filters = UNSET
        else:
            fields_filters = ReportersFieldsFilters.from_dict(_fields_filters)

        node_ids = []
        _node_ids = d.pop("node_ids")
        for node_ids_item_data in _node_ids or []:
            node_ids_item = ModelNodeIdentifier.from_dict(node_ids_item_data)

            node_ids.append(node_ids_item)

        model_integration_filters = cls(
            fields_filters=fields_filters,
            node_ids=node_ids,
        )

        model_integration_filters.additional_properties = d
        return model_integration_filters

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
