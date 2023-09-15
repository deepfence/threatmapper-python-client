from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_integration_list_resp_config import ModelIntegrationListRespConfig
    from ..models.reporters_fields_filters import ReportersFieldsFilters


T = TypeVar("T", bound="ModelIntegrationListResp")


@_attrs_define
class ModelIntegrationListResp:
    """
    Example:
        {'notification_type': 'notification_type', 'filters': {'compare_filter': [{'greater_than': True, 'field_value':
            '', 'field_name': 'field_name'}, {'greater_than': True, 'field_value': '', 'field_name': 'field_name'}],
            'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0,
            'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name': 'field_name'}]},
            'contains_filter': {'filter_in': {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in': {'key': ['',
            '']}}, 'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['',
            '']}}}, 'id': 0, 'integration_type': 'integration_type', 'config': {'key': ''}, 'last_error_msg':
            'last_error_msg'}

    Attributes:
        config (Union[Unset, None, ModelIntegrationListRespConfig]):
        filters (Union[Unset, ReportersFieldsFilters]):  Example: {'compare_filter': [{'greater_than': True,
            'field_value': '', 'field_name': 'field_name'}, {'greater_than': True, 'field_value': '', 'field_name':
            'field_name'}], 'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter': {'order_fields':
            [{'size': 0, 'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name':
            'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in':
            {'key': ['', '']}}, 'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in':
            {'key': ['', '']}}}.
        id (Union[Unset, int]):
        integration_type (Union[Unset, str]):
        last_error_msg (Union[Unset, str]):
        notification_type (Union[Unset, str]):
    """

    config: Union[Unset, None, "ModelIntegrationListRespConfig"] = UNSET
    filters: Union[Unset, "ReportersFieldsFilters"] = UNSET
    id: Union[Unset, int] = UNSET
    integration_type: Union[Unset, str] = UNSET
    last_error_msg: Union[Unset, str] = UNSET
    notification_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict() if self.config else None

        filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        id = self.id
        integration_type = self.integration_type
        last_error_msg = self.last_error_msg
        notification_type = self.notification_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if filters is not UNSET:
            field_dict["filters"] = filters
        if id is not UNSET:
            field_dict["id"] = id
        if integration_type is not UNSET:
            field_dict["integration_type"] = integration_type
        if last_error_msg is not UNSET:
            field_dict["last_error_msg"] = last_error_msg
        if notification_type is not UNSET:
            field_dict["notification_type"] = notification_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_integration_list_resp_config import ModelIntegrationListRespConfig
        from ..models.reporters_fields_filters import ReportersFieldsFilters

        d = src_dict.copy()
        _config = d.pop("config", UNSET)
        config: Union[Unset, None, ModelIntegrationListRespConfig]
        if _config is None:
            config = None
        elif isinstance(_config, Unset):
            config = UNSET
        else:
            config = ModelIntegrationListRespConfig.from_dict(_config)

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, ReportersFieldsFilters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = ReportersFieldsFilters.from_dict(_filters)

        id = d.pop("id", UNSET)

        integration_type = d.pop("integration_type", UNSET)

        last_error_msg = d.pop("last_error_msg", UNSET)

        notification_type = d.pop("notification_type", UNSET)

        model_integration_list_resp = cls(
            config=config,
            filters=filters,
            id=id,
            integration_type=integration_type,
            last_error_msg=last_error_msg,
            notification_type=notification_type,
        )

        model_integration_list_resp.additional_properties = d
        return model_integration_list_resp

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
