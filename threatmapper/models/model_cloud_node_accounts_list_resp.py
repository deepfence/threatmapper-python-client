from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_cloud_node_account_info import ModelCloudNodeAccountInfo


T = TypeVar("T", bound="ModelCloudNodeAccountsListResp")


@_attrs_define
class ModelCloudNodeAccountsListResp:
    """
    Example:
        {'total': 5, 'cloud_node_accounts_info': [{'last_scan_status': 'last_scan_status', 'last_scan_id':
            'last_scan_id', 'refresh_message': 'refresh_message', 'node_name': 'node_name', 'active': True,
            'cloud_provider': 'aws', 'scan_status_map': {'key': 1}, 'host_node_id': 'host_node_id', 'version': 'version',
            'refresh_status_map': {'key': 6}, 'refresh_status': 'refresh_status', 'compliance_percentage':
            0.8008281904610115, 'account_name': 'account_name', 'node_id': 'node_id'}, {'last_scan_status':
            'last_scan_status', 'last_scan_id': 'last_scan_id', 'refresh_message': 'refresh_message', 'node_name':
            'node_name', 'active': True, 'cloud_provider': 'aws', 'scan_status_map': {'key': 1}, 'host_node_id':
            'host_node_id', 'version': 'version', 'refresh_status_map': {'key': 6}, 'refresh_status': 'refresh_status',
            'compliance_percentage': 0.8008281904610115, 'account_name': 'account_name', 'node_id': 'node_id'}]}

    Attributes:
        cloud_node_accounts_info (Union[List['ModelCloudNodeAccountInfo'], None]):
        total (int):
    """

    cloud_node_accounts_info: Union[List["ModelCloudNodeAccountInfo"], None]
    total: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloud_node_accounts_info: Union[List[Dict[str, Any]], None]
        if isinstance(self.cloud_node_accounts_info, list):
            cloud_node_accounts_info = []
            for cloud_node_accounts_info_type_0_item_data in self.cloud_node_accounts_info:
                cloud_node_accounts_info_type_0_item = cloud_node_accounts_info_type_0_item_data.to_dict()
                cloud_node_accounts_info.append(cloud_node_accounts_info_type_0_item)

        else:
            cloud_node_accounts_info = self.cloud_node_accounts_info

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_node_accounts_info": cloud_node_accounts_info,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_cloud_node_account_info import ModelCloudNodeAccountInfo

        d = src_dict.copy()

        def _parse_cloud_node_accounts_info(data: object) -> Union[List["ModelCloudNodeAccountInfo"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cloud_node_accounts_info_type_0 = []
                _cloud_node_accounts_info_type_0 = data
                for cloud_node_accounts_info_type_0_item_data in _cloud_node_accounts_info_type_0:
                    cloud_node_accounts_info_type_0_item = ModelCloudNodeAccountInfo.from_dict(
                        cloud_node_accounts_info_type_0_item_data
                    )

                    cloud_node_accounts_info_type_0.append(cloud_node_accounts_info_type_0_item)

                return cloud_node_accounts_info_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelCloudNodeAccountInfo"], None], data)

        cloud_node_accounts_info = _parse_cloud_node_accounts_info(d.pop("cloud_node_accounts_info"))

        total = d.pop("total")

        model_cloud_node_accounts_list_resp = cls(
            cloud_node_accounts_info=cloud_node_accounts_info,
            total=total,
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
