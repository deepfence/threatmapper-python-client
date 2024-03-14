from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cloud_node_account_info_scan_status_map_type_0 import (
        ModelCloudNodeAccountInfoScanStatusMapType0,
    )


T = TypeVar("T", bound="ModelCloudNodeAccountInfo")


@_attrs_define
class ModelCloudNodeAccountInfo:
    """
    Attributes:
        active (Union[Unset, bool]):
        cloud_provider (Union[Unset, str]):
        compliance_percentage (Union[Unset, float]):
        host_node_id (Union[Unset, str]):
        last_scan_id (Union[Unset, str]):
        last_scan_status (Union[Unset, str]):
        node_id (Union[Unset, str]):
        node_name (Union[Unset, str]):
        scan_status_map (Union['ModelCloudNodeAccountInfoScanStatusMapType0', None, Unset]):
        version (Union[Unset, str]):
    """

    active: Union[Unset, bool] = UNSET
    cloud_provider: Union[Unset, str] = UNSET
    compliance_percentage: Union[Unset, float] = UNSET
    host_node_id: Union[Unset, str] = UNSET
    last_scan_id: Union[Unset, str] = UNSET
    last_scan_status: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    node_name: Union[Unset, str] = UNSET
    scan_status_map: Union["ModelCloudNodeAccountInfoScanStatusMapType0", None, Unset] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.model_cloud_node_account_info_scan_status_map_type_0 import (
            ModelCloudNodeAccountInfoScanStatusMapType0,
        )

        active = self.active

        cloud_provider = self.cloud_provider

        compliance_percentage = self.compliance_percentage

        host_node_id = self.host_node_id

        last_scan_id = self.last_scan_id

        last_scan_status = self.last_scan_status

        node_id = self.node_id

        node_name = self.node_name

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
        if scan_status_map is not UNSET:
            field_dict["scan_status_map"] = scan_status_map
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_cloud_node_account_info_scan_status_map_type_0 import (
            ModelCloudNodeAccountInfoScanStatusMapType0,
        )

        d = src_dict.copy()
        active = d.pop("active", UNSET)

        cloud_provider = d.pop("cloud_provider", UNSET)

        compliance_percentage = d.pop("compliance_percentage", UNSET)

        host_node_id = d.pop("host_node_id", UNSET)

        last_scan_id = d.pop("last_scan_id", UNSET)

        last_scan_status = d.pop("last_scan_status", UNSET)

        node_id = d.pop("node_id", UNSET)

        node_name = d.pop("node_name", UNSET)

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
            active=active,
            cloud_provider=cloud_provider,
            compliance_percentage=compliance_percentage,
            host_node_id=host_node_id,
            last_scan_id=last_scan_id,
            last_scan_status=last_scan_status,
            node_id=node_id,
            node_name=node_name,
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
