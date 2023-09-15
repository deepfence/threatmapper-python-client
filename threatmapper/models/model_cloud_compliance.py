from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelCloudCompliance")


@_attrs_define
class ModelCloudCompliance:
    """
    Example:
        {'severity': 'severity', 'reason': 'reason', 'control_id': 'control_id', 'resource': 'resource', 'masked': True,
            'count': 0, 'node_name': 'node_name', 'description': 'description', 'resources': ['resources', 'resources'],
            'cloud_provider': 'cloud_provider', 'title': 'title', 'type': 'type', 'compliance_check_type':
            'compliance_check_type', 'account_id': 'account_id', 'updated_at': 6, 'service': 'service', 'region': 'region',
            'group': 'group', 'node_id': 'node_id', 'status': 'status'}

    Attributes:
        account_id (str):
        cloud_provider (str):
        compliance_check_type (str):
        control_id (str):
        count (int):
        description (str):
        group (str):
        masked (bool):
        node_id (str):
        node_name (str):
        reason (str):
        region (str):
        resource (str):
        service (str):
        severity (str):
        status (str):
        title (str):
        type (str):
        updated_at (int):
        resources (Union[Unset, None, List[str]]):
    """

    account_id: str
    cloud_provider: str
    compliance_check_type: str
    control_id: str
    count: int
    description: str
    group: str
    masked: bool
    node_id: str
    node_name: str
    reason: str
    region: str
    resource: str
    service: str
    severity: str
    status: str
    title: str
    type: str
    updated_at: int
    resources: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        cloud_provider = self.cloud_provider
        compliance_check_type = self.compliance_check_type
        control_id = self.control_id
        count = self.count
        description = self.description
        group = self.group
        masked = self.masked
        node_id = self.node_id
        node_name = self.node_name
        reason = self.reason
        region = self.region
        resource = self.resource
        service = self.service
        severity = self.severity
        status = self.status
        title = self.title
        type = self.type
        updated_at = self.updated_at
        resources: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.resources, Unset):
            if self.resources is None:
                resources = None
            else:
                resources = self.resources

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "cloud_provider": cloud_provider,
                "compliance_check_type": compliance_check_type,
                "control_id": control_id,
                "count": count,
                "description": description,
                "group": group,
                "masked": masked,
                "node_id": node_id,
                "node_name": node_name,
                "reason": reason,
                "region": region,
                "resource": resource,
                "service": service,
                "severity": severity,
                "status": status,
                "title": title,
                "type": type,
                "updated_at": updated_at,
            }
        )
        if resources is not UNSET:
            field_dict["resources"] = resources

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("account_id")

        cloud_provider = d.pop("cloud_provider")

        compliance_check_type = d.pop("compliance_check_type")

        control_id = d.pop("control_id")

        count = d.pop("count")

        description = d.pop("description")

        group = d.pop("group")

        masked = d.pop("masked")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        reason = d.pop("reason")

        region = d.pop("region")

        resource = d.pop("resource")

        service = d.pop("service")

        severity = d.pop("severity")

        status = d.pop("status")

        title = d.pop("title")

        type = d.pop("type")

        updated_at = d.pop("updated_at")

        resources = cast(List[str], d.pop("resources", UNSET))

        model_cloud_compliance = cls(
            account_id=account_id,
            cloud_provider=cloud_provider,
            compliance_check_type=compliance_check_type,
            control_id=control_id,
            count=count,
            description=description,
            group=group,
            masked=masked,
            node_id=node_id,
            node_name=node_name,
            reason=reason,
            region=region,
            resource=resource,
            service=service,
            severity=severity,
            status=status,
            title=title,
            type=type,
            updated_at=updated_at,
            resources=resources,
        )

        model_cloud_compliance.additional_properties = d
        return model_cloud_compliance

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
