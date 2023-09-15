from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cloud_node_account_info_scan_status_map import ModelCloudNodeAccountInfoScanStatusMap


T = TypeVar("T", bound="ModelCloudNodeAccountInfo")


@_attrs_define
class ModelCloudNodeAccountInfo:
    """
    Example:
        {'last_scan_status': 'last_scan_status', 'compliance_percentage': 0.8008281904610115, 'last_scan_id':
            'last_scan_id', 'node_name': 'node_name', 'active': True, 'cloud_provider': 'cloud_provider', 'scan_status_map':
            {'key': 6}, 'version': 'version', 'node_id': 'node_id'}

    Attributes:
        active (Union[Unset, bool]):
        cloud_provider (Union[Unset, str]):
        compliance_percentage (Union[Unset, float]):
        last_scan_id (Union[Unset, str]):
        last_scan_status (Union[Unset, str]):
        node_id (Union[Unset, str]):
        node_name (Union[Unset, str]):
        scan_status_map (Union[Unset, None, ModelCloudNodeAccountInfoScanStatusMap]):
        version (Union[Unset, str]):
    """

    active: Union[Unset, bool] = UNSET
    cloud_provider: Union[Unset, str] = UNSET
    compliance_percentage: Union[Unset, float] = UNSET
    last_scan_id: Union[Unset, str] = UNSET
    last_scan_status: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    node_name: Union[Unset, str] = UNSET
    scan_status_map: Union[Unset, None, "ModelCloudNodeAccountInfoScanStatusMap"] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active = self.active
        cloud_provider = self.cloud_provider
        compliance_percentage = self.compliance_percentage
        last_scan_id = self.last_scan_id
        last_scan_status = self.last_scan_status
        node_id = self.node_id
        node_name = self.node_name
        scan_status_map: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.scan_status_map, Unset):
            scan_status_map = self.scan_status_map.to_dict() if self.scan_status_map else None

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
        from ..models.model_cloud_node_account_info_scan_status_map import ModelCloudNodeAccountInfoScanStatusMap

        d = src_dict.copy()
        active = d.pop("active", UNSET)

        cloud_provider = d.pop("cloud_provider", UNSET)

        compliance_percentage = d.pop("compliance_percentage", UNSET)

        last_scan_id = d.pop("last_scan_id", UNSET)

        last_scan_status = d.pop("last_scan_status", UNSET)

        node_id = d.pop("node_id", UNSET)

        node_name = d.pop("node_name", UNSET)

        _scan_status_map = d.pop("scan_status_map", UNSET)
        scan_status_map: Union[Unset, None, ModelCloudNodeAccountInfoScanStatusMap]
        if _scan_status_map is None:
            scan_status_map = None
        elif isinstance(_scan_status_map, Unset):
            scan_status_map = UNSET
        else:
            scan_status_map = ModelCloudNodeAccountInfoScanStatusMap.from_dict(_scan_status_map)

        version = d.pop("version", UNSET)

        model_cloud_node_account_info = cls(
            active=active,
            cloud_provider=cloud_provider,
            compliance_percentage=compliance_percentage,
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
