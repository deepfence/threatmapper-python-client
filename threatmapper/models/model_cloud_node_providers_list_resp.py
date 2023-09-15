from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_posture_provider import ModelPostureProvider


T = TypeVar("T", bound="ModelCloudNodeProvidersListResp")


@_attrs_define
class ModelCloudNodeProvidersListResp:
    """
    Example:
        {'providers': [{'node_count_inactive': 1, 'compliance_percentage': 0.8008281904610115, 'node_label':
            'node_label', 'name': 'name', 'scan_count': 5, 'node_count': 6, 'resource_count': 5}, {'node_count_inactive': 1,
            'compliance_percentage': 0.8008281904610115, 'node_label': 'node_label', 'name': 'name', 'scan_count': 5,
            'node_count': 6, 'resource_count': 5}]}

    Attributes:
        providers (Optional[List['ModelPostureProvider']]):
    """

    providers: Optional[List["ModelPostureProvider"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if self.providers is None:
            providers = None
        else:
            providers = []
            for providers_item_data in self.providers:
                providers_item = providers_item_data.to_dict()

                providers.append(providers_item)

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
        providers = []
        _providers = d.pop("providers")
        for providers_item_data in _providers or []:
            providers_item = ModelPostureProvider.from_dict(providers_item_data)

            providers.append(providers_item)

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
