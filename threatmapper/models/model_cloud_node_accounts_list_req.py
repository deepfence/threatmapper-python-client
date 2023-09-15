from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_fetch_window import ModelFetchWindow


T = TypeVar("T", bound="ModelCloudNodeAccountsListReq")


@_attrs_define
class ModelCloudNodeAccountsListReq:
    """
    Example:
        {'cloud_provider': 'cloud_provider', 'window': {'offset': 0, 'size': 6}}

    Attributes:
        window (ModelFetchWindow):  Example: {'offset': 0, 'size': 6}.
        cloud_provider (Union[Unset, str]):
    """

    window: "ModelFetchWindow"
    cloud_provider: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        window = self.window.to_dict()

        cloud_provider = self.cloud_provider

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "window": window,
            }
        )
        if cloud_provider is not UNSET:
            field_dict["cloud_provider"] = cloud_provider

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_fetch_window import ModelFetchWindow

        d = src_dict.copy()
        window = ModelFetchWindow.from_dict(d.pop("window"))

        cloud_provider = d.pop("cloud_provider", UNSET)

        model_cloud_node_accounts_list_req = cls(
            window=window,
            cloud_provider=cloud_provider,
        )

        model_cloud_node_accounts_list_req.additional_properties = d
        return model_cloud_node_accounts_list_req

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
