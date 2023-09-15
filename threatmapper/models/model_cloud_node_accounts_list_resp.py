from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_cloud_node_account_info import ModelCloudNodeAccountInfo


T = TypeVar("T", bound="ModelCloudNodeAccountsListResp")


@_attrs_define
class ModelCloudNodeAccountsListResp:
    """
    Example:
        {'total': 1, 'cloud_node_accounts_info': [{'last_scan_status': 'last_scan_status', 'compliance_percentage':
            0.8008281904610115, 'last_scan_id': 'last_scan_id', 'node_name': 'node_name', 'active': True, 'cloud_provider':
            'cloud_provider', 'scan_status_map': {'key': 6}, 'version': 'version', 'node_id': 'node_id'},
            {'last_scan_status': 'last_scan_status', 'compliance_percentage': 0.8008281904610115, 'last_scan_id':
            'last_scan_id', 'node_name': 'node_name', 'active': True, 'cloud_provider': 'cloud_provider', 'scan_status_map':
            {'key': 6}, 'version': 'version', 'node_id': 'node_id'}]}

    Attributes:
        total (int):
        cloud_node_accounts_info (Optional[List['ModelCloudNodeAccountInfo']]):
    """

    total: int
    cloud_node_accounts_info: Optional[List["ModelCloudNodeAccountInfo"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total
        if self.cloud_node_accounts_info is None:
            cloud_node_accounts_info = None
        else:
            cloud_node_accounts_info = []
            for cloud_node_accounts_info_item_data in self.cloud_node_accounts_info:
                cloud_node_accounts_info_item = cloud_node_accounts_info_item_data.to_dict()

                cloud_node_accounts_info.append(cloud_node_accounts_info_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "cloud_node_accounts_info": cloud_node_accounts_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_cloud_node_account_info import ModelCloudNodeAccountInfo

        d = src_dict.copy()
        total = d.pop("total")

        cloud_node_accounts_info = []
        _cloud_node_accounts_info = d.pop("cloud_node_accounts_info")
        for cloud_node_accounts_info_item_data in _cloud_node_accounts_info or []:
            cloud_node_accounts_info_item = ModelCloudNodeAccountInfo.from_dict(cloud_node_accounts_info_item_data)

            cloud_node_accounts_info.append(cloud_node_accounts_info_item)

        model_cloud_node_accounts_list_resp = cls(
            total=total,
            cloud_node_accounts_info=cloud_node_accounts_info,
        )

        model_cloud_node_accounts_list_resp.additional_properties = d
        return model_cloud_node_accounts_list_resp

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
