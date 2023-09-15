from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelCloudResource")


@_attrs_define
class ModelCloudResource:
    """
    Example:
        {'cloud_compliances_count': 0, 'account_id': 'account_id', 'cloud_compliance_latest_scan_id':
            'cloud_compliance_latest_scan_id', 'node_type': 'node_type', 'cloud_compliance_scan_status':
            'cloud_compliance_scan_status', 'cloud_region': 'cloud_region', 'node_name': 'node_name', 'cloud_provider':
            'cloud_provider', 'type_label': 'type_label', 'node_id': 'node_id'}

    Attributes:
        account_id (str):
        cloud_compliance_latest_scan_id (str):
        cloud_compliance_scan_status (str):
        cloud_compliances_count (int):
        cloud_provider (str):
        cloud_region (str):
        node_id (str):
        node_name (str):
        node_type (str):
        type_label (str):
    """

    account_id: str
    cloud_compliance_latest_scan_id: str
    cloud_compliance_scan_status: str
    cloud_compliances_count: int
    cloud_provider: str
    cloud_region: str
    node_id: str
    node_name: str
    node_type: str
    type_label: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        cloud_compliance_latest_scan_id = self.cloud_compliance_latest_scan_id
        cloud_compliance_scan_status = self.cloud_compliance_scan_status
        cloud_compliances_count = self.cloud_compliances_count
        cloud_provider = self.cloud_provider
        cloud_region = self.cloud_region
        node_id = self.node_id
        node_name = self.node_name
        node_type = self.node_type
        type_label = self.type_label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "cloud_compliance_latest_scan_id": cloud_compliance_latest_scan_id,
                "cloud_compliance_scan_status": cloud_compliance_scan_status,
                "cloud_compliances_count": cloud_compliances_count,
                "cloud_provider": cloud_provider,
                "cloud_region": cloud_region,
                "node_id": node_id,
                "node_name": node_name,
                "node_type": node_type,
                "type_label": type_label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("account_id")

        cloud_compliance_latest_scan_id = d.pop("cloud_compliance_latest_scan_id")

        cloud_compliance_scan_status = d.pop("cloud_compliance_scan_status")

        cloud_compliances_count = d.pop("cloud_compliances_count")

        cloud_provider = d.pop("cloud_provider")

        cloud_region = d.pop("cloud_region")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        node_type = d.pop("node_type")

        type_label = d.pop("type_label")

        model_cloud_resource = cls(
            account_id=account_id,
            cloud_compliance_latest_scan_id=cloud_compliance_latest_scan_id,
            cloud_compliance_scan_status=cloud_compliance_scan_status,
            cloud_compliances_count=cloud_compliances_count,
            cloud_provider=cloud_provider,
            cloud_region=cloud_region,
            node_id=node_id,
            node_name=node_name,
            node_type=node_type,
            type_label=type_label,
        )

        model_cloud_resource.additional_properties = d
        return model_cloud_resource

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
