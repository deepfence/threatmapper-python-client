from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
            {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['', '']}}}, 'cloud_provider':
            'cloud_provider', 'container_names': ['container_names', 'container_names'], 'node_ids': [{'node_type': 'image',
            'node_id': 'node_id'}, {'node_type': 'image', 'node_id': 'node_id'}]}

    Attributes:
        node_ids (Union[List['ModelNodeIdentifier'], None]):
        cloud_provider (Union[Unset, str]):
        container_names (Union[List[str], None, Unset]):
        fields_filters (Union[Unset, ReportersFieldsFilters]):  Example: {'compare_filter': [{'greater_than': True,
            'field_value': '', 'field_name': 'field_name'}, {'greater_than': True, 'field_value': '', 'field_name':
            'field_name'}], 'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter': {'order_fields':
            [{'size': 0, 'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name':
            'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in':
            {'key': ['', '']}}, 'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in':
            {'key': ['', '']}}}.
    """

    node_ids: Union[List["ModelNodeIdentifier"], None]
    cloud_provider: Union[Unset, str] = UNSET
    container_names: Union[List[str], None, Unset] = UNSET
    fields_filters: Union[Unset, "ReportersFieldsFilters"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_ids: Union[List[Dict[str, Any]], None]
        if isinstance(self.node_ids, list):
            node_ids = []
            for node_ids_type_0_item_data in self.node_ids:
                node_ids_type_0_item = node_ids_type_0_item_data.to_dict()
                node_ids.append(node_ids_type_0_item)

        else:
            node_ids = self.node_ids

        cloud_provider = self.cloud_provider

        container_names: Union[List[str], None, Unset]
        if isinstance(self.container_names, Unset):
            container_names = UNSET
        elif isinstance(self.container_names, list):
            container_names = self.container_names

        else:
            container_names = self.container_names

        fields_filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fields_filters, Unset):
            fields_filters = self.fields_filters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_ids": node_ids,
            }
        )
        if cloud_provider is not UNSET:
            field_dict["cloud_provider"] = cloud_provider
        if container_names is not UNSET:
            field_dict["container_names"] = container_names
        if fields_filters is not UNSET:
            field_dict["fields_filters"] = fields_filters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_node_identifier import ModelNodeIdentifier
        from ..models.reporters_fields_filters import ReportersFieldsFilters

        d = src_dict.copy()

        def _parse_node_ids(data: object) -> Union[List["ModelNodeIdentifier"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                node_ids_type_0 = []
                _node_ids_type_0 = data
                for node_ids_type_0_item_data in _node_ids_type_0:
                    node_ids_type_0_item = ModelNodeIdentifier.from_dict(node_ids_type_0_item_data)

                    node_ids_type_0.append(node_ids_type_0_item)

                return node_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelNodeIdentifier"], None], data)

        node_ids = _parse_node_ids(d.pop("node_ids"))

        cloud_provider = d.pop("cloud_provider", UNSET)

        def _parse_container_names(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                container_names_type_0 = cast(List[str], data)

                return container_names_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        container_names = _parse_container_names(d.pop("container_names", UNSET))

        _fields_filters = d.pop("fields_filters", UNSET)
        fields_filters: Union[Unset, ReportersFieldsFilters]
        if isinstance(_fields_filters, Unset):
            fields_filters = UNSET
        else:
            fields_filters = ReportersFieldsFilters.from_dict(_fields_filters)

        model_integration_filters = cls(
            node_ids=node_ids,
            cloud_provider=cloud_provider,
            container_names=container_names,
            fields_filters=fields_filters,
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
