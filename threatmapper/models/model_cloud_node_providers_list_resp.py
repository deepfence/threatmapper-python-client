from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_posture_provider import ModelPostureProvider


T = TypeVar("T", bound="ModelCloudNodeProvidersListResp")


@_attrs_define
class ModelCloudNodeProvidersListResp:
    """
    Attributes:
        providers (Union[List['ModelPostureProvider'], None]):
    """

    providers: Union[List["ModelPostureProvider"], None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        providers: Union[List[Dict[str, Any]], None]
        if isinstance(self.providers, list):
            providers = []
            for providers_type_0_item_data in self.providers:
                providers_type_0_item = providers_type_0_item_data.to_dict()
                providers.append(providers_type_0_item)

        else:
            providers = self.providers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providers": providers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_posture_provider import ModelPostureProvider

        d = src_dict.copy()

        def _parse_providers(data: object) -> Union[List["ModelPostureProvider"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                providers_type_0 = []
                _providers_type_0 = data
                for providers_type_0_item_data in _providers_type_0:
                    providers_type_0_item = ModelPostureProvider.from_dict(providers_type_0_item_data)

                    providers_type_0.append(providers_type_0_item)

                return providers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelPostureProvider"], None], data)

        providers = _parse_providers(d.pop("providers"))

        model_cloud_node_providers_list_resp = cls(
            providers=providers,
        )

        model_cloud_node_providers_list_resp.additional_properties = d
        return model_cloud_node_providers_list_resp

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
