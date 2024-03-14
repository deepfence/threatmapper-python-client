from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_integration_filters import ModelIntegrationFilters
    from ..models.model_integration_list_resp_config_type_0 import ModelIntegrationListRespConfigType0


T = TypeVar("T", bound="ModelIntegrationListResp")


@_attrs_define
class ModelIntegrationListResp:
    """
    Attributes:
        config (Union['ModelIntegrationListRespConfigType0', None, Unset]):
        filters (Union[Unset, ModelIntegrationFilters]):
        id (Union[Unset, int]):
        integration_type (Union[Unset, str]):
        last_error_msg (Union[Unset, str]):
        notification_type (Union[Unset, str]):
    """

    config: Union["ModelIntegrationListRespConfigType0", None, Unset] = UNSET
    filters: Union[Unset, "ModelIntegrationFilters"] = UNSET
    id: Union[Unset, int] = UNSET
    integration_type: Union[Unset, str] = UNSET
    last_error_msg: Union[Unset, str] = UNSET
    notification_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.model_integration_list_resp_config_type_0 import ModelIntegrationListRespConfigType0

        config: Union[Dict[str, Any], None, Unset]
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, ModelIntegrationListRespConfigType0):
            config = self.config.to_dict()
        else:
            config = self.config

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
        from ..models.model_integration_filters import ModelIntegrationFilters
        from ..models.model_integration_list_resp_config_type_0 import ModelIntegrationListRespConfigType0

        d = src_dict.copy()

        def _parse_config(data: object) -> Union["ModelIntegrationListRespConfigType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = ModelIntegrationListRespConfigType0.from_dict(data)

                return config_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelIntegrationListRespConfigType0", None, Unset], data)

        config = _parse_config(d.pop("config", UNSET))

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, ModelIntegrationFilters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = ModelIntegrationFilters.from_dict(_filters)

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
