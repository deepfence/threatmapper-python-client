from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_integration_add_req_config import ModelIntegrationAddReqConfig
    from ..models.model_integration_filters import ModelIntegrationFilters


T = TypeVar("T", bound="ModelIntegrationAddReq")


@_attrs_define
class ModelIntegrationAddReq:
    """
    Example:
        {'notification_type': 'notification_type', 'filters': {'fields_filters': {'compare_filter': [{'greater_than':
            True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than': True, 'field_value': '', 'field_name':
            'field_name'}], 'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter': {'order_fields':
            [{'size': 0, 'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name':
            'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in':
            {'key': ['', '']}}, 'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in':
            {'key': ['', '']}}}, 'node_ids': [{'node_type': 'image', 'node_id': 'node_id'}, {'node_type': 'image',
            'node_id': 'node_id'}]}, 'integration_type': 'integration_type', 'config': {'key': ''}}

    Attributes:
        config (Union[Unset, None, ModelIntegrationAddReqConfig]):
        filters (Union[Unset, ModelIntegrationFilters]):  Example: {'fields_filters': {'compare_filter':
            [{'greater_than': True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than': True, 'field_value':
            '', 'field_name': 'field_name'}], 'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter':
            {'order_fields': [{'size': 0, 'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True,
            'field_name': 'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}}, 'contains_in_array_filter':
            {'filter_in': {'key': ['', '']}}, 'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter':
            {'filter_in': {'key': ['', '']}}}, 'node_ids': [{'node_type': 'image', 'node_id': 'node_id'}, {'node_type':
            'image', 'node_id': 'node_id'}]}.
        integration_type (Union[Unset, str]):
        notification_type (Union[Unset, str]):
    """

    config: Union[Unset, None, "ModelIntegrationAddReqConfig"] = UNSET
    filters: Union[Unset, "ModelIntegrationFilters"] = UNSET
    integration_type: Union[Unset, str] = UNSET
    notification_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict() if self.config else None

        filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        integration_type = self.integration_type
        notification_type = self.notification_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if filters is not UNSET:
            field_dict["filters"] = filters
        if integration_type is not UNSET:
            field_dict["integration_type"] = integration_type
        if notification_type is not UNSET:
            field_dict["notification_type"] = notification_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_integration_add_req_config import ModelIntegrationAddReqConfig
        from ..models.model_integration_filters import ModelIntegrationFilters

        d = src_dict.copy()
        _config = d.pop("config", UNSET)
        config: Union[Unset, None, ModelIntegrationAddReqConfig]
        if _config is None:
            config = None
        elif isinstance(_config, Unset):
            config = UNSET
        else:
            config = ModelIntegrationAddReqConfig.from_dict(_config)

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, ModelIntegrationFilters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = ModelIntegrationFilters.from_dict(_filters)

        integration_type = d.pop("integration_type", UNSET)

        notification_type = d.pop("notification_type", UNSET)

        model_integration_add_req = cls(
            config=config,
            filters=filters,
            integration_type=integration_type,
            notification_type=notification_type,
        )

        model_integration_add_req.additional_properties = d
        return model_integration_add_req

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
