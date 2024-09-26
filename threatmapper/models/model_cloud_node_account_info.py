from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_cloud_node_account_info_cloud_provider import ModelCloudNodeAccountInfoCloudProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cloud_node_account_info_refresh_status_map_type_0 import (
        ModelCloudNodeAccountInfoRefreshStatusMapType0,
    )
    from ..models.model_cloud_node_account_info_scan_status_map_type_0 import (
        ModelCloudNodeAccountInfoScanStatusMapType0,
    )


T = TypeVar("T", bound="ModelCloudNodeAccountInfo")


@_attrs_define
class ModelCloudNodeAccountInfo:
    """
    Attributes:
        account_name (Union[Unset, str]):
        active (Union[Unset, bool]):
        cloud_provider (Union[Unset, ModelCloudNodeAccountInfoCloudProvider]):
        compliance_percentage (Union[Unset, float]):
        host_node_id (Union[Unset, str]):
        last_scan_id (Union[Unset, str]):
        last_scan_status (Union[Unset, str]):
        node_id (Union[Unset, str]):
        node_name (Union[Unset, str]):
        refresh_message (Union[Unset, str]):
        refresh_status (Union[Unset, str]):
        refresh_status_map (Union['ModelCloudNodeAccountInfoRefreshStatusMapType0', None, Unset]):
        scan_status_map (Union['ModelCloudNodeAccountInfoScanStatusMapType0', None, Unset]):
        version (Union[Unset, str]):
    """

    account_name: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    cloud_provider: Union[Unset, ModelCloudNodeAccountInfoCloudProvider] = UNSET
    compliance_percentage: Union[Unset, float] = UNSET
    host_node_id: Union[Unset, str] = UNSET
    last_scan_id: Union[Unset, str] = UNSET
    last_scan_status: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    node_name: Union[Unset, str] = UNSET
    refresh_message: Union[Unset, str] = UNSET
    refresh_status: Union[Unset, str] = UNSET
    refresh_status_map: Union["ModelCloudNodeAccountInfoRefreshStatusMapType0", None, Unset] = UNSET
    scan_status_map: Union["ModelCloudNodeAccountInfoScanStatusMapType0", None, Unset] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.model_cloud_node_account_info_refresh_status_map_type_0 import (
            ModelCloudNodeAccountInfoRefreshStatusMapType0,
        )
        from ..models.model_cloud_node_account_info_scan_status_map_type_0 import (
            ModelCloudNodeAccountInfoScanStatusMapType0,
        )

        account_name = self.account_name

        active = self.active

        cloud_provider: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_provider, Unset):
            cloud_provider = self.cloud_provider.value

        compliance_percentage = self.compliance_percentage

        host_node_id = self.host_node_id

        last_scan_id = self.last_scan_id

        last_scan_status = self.last_scan_status

        node_id = self.node_id

        node_name = self.node_name

        refresh_message = self.refresh_message

        refresh_status = self.refresh_status

        refresh_status_map: Union[Dict[str, Any], None, Unset]
        if isinstance(self.refresh_status_map, Unset):
            refresh_status_map = UNSET
        elif isinstance(self.refresh_status_map, ModelCloudNodeAccountInfoRefreshStatusMapType0):
            refresh_status_map = self.refresh_status_map.to_dict()
        else:
            refresh_status_map = self.refresh_status_map

        scan_status_map: Union[Dict[str, Any], None, Unset]
        if isinstance(self.scan_status_map, Unset):
            scan_status_map = UNSET
        elif isinstance(self.scan_status_map, ModelCloudNodeAccountInfoScanStatusMapType0):
            scan_status_map = self.scan_status_map.to_dict()
        else:
            scan_status_map = self.scan_status_map

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_name is not UNSET:
            field_dict["account_name"] = account_name
        if active is not UNSET:
            field_dict["active"] = active
        if cloud_provider is not UNSET:
            field_dict["cloud_provider"] = cloud_provider
        if compliance_percentage is not UNSET:
            field_dict["compliance_percentage"] = compliance_percentage
        if host_node_id is not UNSET:
            field_dict["host_node_id"] = host_node_id
        if last_scan_id is not UNSET:
            field_dict["last_scan_id"] = last_scan_id
        if last_scan_status is not UNSET:
            field_dict["last_scan_status"] = last_scan_status
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if node_name is not UNSET:
            field_dict["node_name"] = node_name
        if refresh_message is not UNSET:
            field_dict["refresh_message"] = refresh_message
        if refresh_status is not UNSET:
            field_dict["refresh_status"] = refresh_status
        if refresh_status_map is not UNSET:
            field_dict["refresh_status_map"] = refresh_status_map
        if scan_status_map is not UNSET:
            field_dict["scan_status_map"] = scan_status_map
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_cloud_node_account_info_refresh_status_map_type_0 import (
            ModelCloudNodeAccountInfoRefreshStatusMapType0,
        )
        from ..models.model_cloud_node_account_info_scan_status_map_type_0 import (
            ModelCloudNodeAccountInfoScanStatusMapType0,
        )

        d = src_dict.copy()
        account_name = d.pop("account_name", UNSET)

        active = d.pop("active", UNSET)

        _cloud_provider = d.pop("cloud_provider", UNSET)
        cloud_provider: Union[Unset, ModelCloudNodeAccountInfoCloudProvider]
        if isinstance(_cloud_provider, Unset):
            cloud_provider = UNSET
        else:
            cloud_provider = ModelCloudNodeAccountInfoCloudProvider(_cloud_provider)

        compliance_percentage = d.pop("compliance_percentage", UNSET)

        host_node_id = d.pop("host_node_id", UNSET)

        last_scan_id = d.pop("last_scan_id", UNSET)

        last_scan_status = d.pop("last_scan_status", UNSET)

        node_id = d.pop("node_id", UNSET)

        node_name = d.pop("node_name", UNSET)

        refresh_message = d.pop("refresh_message", UNSET)

        refresh_status = d.pop("refresh_status", UNSET)

        def _parse_refresh_status_map(
            data: object,
        ) -> Union["ModelCloudNodeAccountInfoRefreshStatusMapType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                refresh_status_map_type_0 = ModelCloudNodeAccountInfoRefreshStatusMapType0.from_dict(data)

                return refresh_status_map_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelCloudNodeAccountInfoRefreshStatusMapType0", None, Unset], data)

        refresh_status_map = _parse_refresh_status_map(d.pop("refresh_status_map", UNSET))

        def _parse_scan_status_map(data: object) -> Union["ModelCloudNodeAccountInfoScanStatusMapType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                scan_status_map_type_0 = ModelCloudNodeAccountInfoScanStatusMapType0.from_dict(data)

                return scan_status_map_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelCloudNodeAccountInfoScanStatusMapType0", None, Unset], data)

        scan_status_map = _parse_scan_status_map(d.pop("scan_status_map", UNSET))

        version = d.pop("version", UNSET)

        model_cloud_node_account_info = cls(
            account_name=account_name,
            active=active,
            cloud_provider=cloud_provider,
            compliance_percentage=compliance_percentage,
            host_node_id=host_node_id,
            last_scan_id=last_scan_id,
            last_scan_status=last_scan_status,
            node_id=node_id,
            node_name=node_name,
            refresh_message=refresh_message,
            refresh_status=refresh_status,
            refresh_status_map=refresh_status_map,
            scan_status_map=scan_status_map,
            version=version,
        )

        model_cloud_node_account_info.additional_properties = d
        return model_cloud_node_account_info

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
