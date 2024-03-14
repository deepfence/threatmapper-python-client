from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IngestersCloudCompliance")


@_attrs_define
class IngestersCloudCompliance:
    """
    Attributes:
        timestamp (Union[Unset, str]):
        account_id (Union[Unset, str]):
        cloud_provider (Union[Unset, str]):
        compliance_check_type (Union[Unset, str]):
        control_id (Union[Unset, str]):
        count (Union[Unset, int]):
        description (Union[Unset, str]):
        doc_id (Union[Unset, str]):
        group (Union[Unset, str]):
        reason (Union[Unset, str]):
        region (Union[Unset, str]):
        resource (Union[Unset, str]):
        scan_id (Union[Unset, str]):
        service (Union[Unset, str]):
        severity (Union[Unset, str]):
        status (Union[Unset, str]):
        title (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    timestamp: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    cloud_provider: Union[Unset, str] = UNSET
    compliance_check_type: Union[Unset, str] = UNSET
    control_id: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    doc_id: Union[Unset, str] = UNSET
    group: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    resource: Union[Unset, str] = UNSET
    scan_id: Union[Unset, str] = UNSET
    service: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp

        account_id = self.account_id

        cloud_provider = self.cloud_provider

        compliance_check_type = self.compliance_check_type

        control_id = self.control_id

        count = self.count

        description = self.description

        doc_id = self.doc_id

        group = self.group

        reason = self.reason

        region = self.region

        resource = self.resource

        scan_id = self.scan_id

        service = self.service

        severity = self.severity

        status = self.status

        title = self.title

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["@timestamp"] = timestamp
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if cloud_provider is not UNSET:
            field_dict["cloud_provider"] = cloud_provider
        if compliance_check_type is not UNSET:
            field_dict["compliance_check_type"] = compliance_check_type
        if control_id is not UNSET:
            field_dict["control_id"] = control_id
        if count is not UNSET:
            field_dict["count"] = count
        if description is not UNSET:
            field_dict["description"] = description
        if doc_id is not UNSET:
            field_dict["doc_id"] = doc_id
        if group is not UNSET:
            field_dict["group"] = group
        if reason is not UNSET:
            field_dict["reason"] = reason
        if region is not UNSET:
            field_dict["region"] = region
        if resource is not UNSET:
            field_dict["resource"] = resource
        if scan_id is not UNSET:
            field_dict["scan_id"] = scan_id
        if service is not UNSET:
            field_dict["service"] = service
        if severity is not UNSET:
            field_dict["severity"] = severity
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = d.pop("@timestamp", UNSET)

        account_id = d.pop("account_id", UNSET)

        cloud_provider = d.pop("cloud_provider", UNSET)

        compliance_check_type = d.pop("compliance_check_type", UNSET)

        control_id = d.pop("control_id", UNSET)

        count = d.pop("count", UNSET)

        description = d.pop("description", UNSET)

        doc_id = d.pop("doc_id", UNSET)

        group = d.pop("group", UNSET)

        reason = d.pop("reason", UNSET)

        region = d.pop("region", UNSET)

        resource = d.pop("resource", UNSET)

        scan_id = d.pop("scan_id", UNSET)

        service = d.pop("service", UNSET)

        severity = d.pop("severity", UNSET)

        status = d.pop("status", UNSET)

        title = d.pop("title", UNSET)

        type = d.pop("type", UNSET)

        ingesters_cloud_compliance = cls(
            timestamp=timestamp,
            account_id=account_id,
            cloud_provider=cloud_provider,
            compliance_check_type=compliance_check_type,
            control_id=control_id,
            count=count,
            description=description,
            doc_id=doc_id,
            group=group,
            reason=reason,
            region=region,
            resource=resource,
            scan_id=scan_id,
            service=service,
            severity=severity,
            status=status,
            title=title,
            type=type,
        )

        ingesters_cloud_compliance.additional_properties = d
        return ingesters_cloud_compliance

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
