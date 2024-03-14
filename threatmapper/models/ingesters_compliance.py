from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IngestersCompliance")


@_attrs_define
class IngestersCompliance:
    """
    Attributes:
        compliance_check_type (Union[Unset, str]):
        description (Union[Unset, str]):
        node_id (Union[Unset, str]):
        node_type (Union[Unset, str]):
        remediation_ansible (Union[Unset, str]):
        remediation_puppet (Union[Unset, str]):
        remediation_script (Union[Unset, str]):
        resource (Union[Unset, str]):
        scan_id (Union[Unset, str]):
        status (Union[Unset, str]):
        test_category (Union[Unset, str]):
        test_desc (Union[Unset, str]):
        test_number (Union[Unset, str]):
        test_rationale (Union[Unset, str]):
        test_severity (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    compliance_check_type: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    node_type: Union[Unset, str] = UNSET
    remediation_ansible: Union[Unset, str] = UNSET
    remediation_puppet: Union[Unset, str] = UNSET
    remediation_script: Union[Unset, str] = UNSET
    resource: Union[Unset, str] = UNSET
    scan_id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    test_category: Union[Unset, str] = UNSET
    test_desc: Union[Unset, str] = UNSET
    test_number: Union[Unset, str] = UNSET
    test_rationale: Union[Unset, str] = UNSET
    test_severity: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compliance_check_type = self.compliance_check_type

        description = self.description

        node_id = self.node_id

        node_type = self.node_type

        remediation_ansible = self.remediation_ansible

        remediation_puppet = self.remediation_puppet

        remediation_script = self.remediation_script

        resource = self.resource

        scan_id = self.scan_id

        status = self.status

        test_category = self.test_category

        test_desc = self.test_desc

        test_number = self.test_number

        test_rationale = self.test_rationale

        test_severity = self.test_severity

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compliance_check_type is not UNSET:
            field_dict["compliance_check_type"] = compliance_check_type
        if description is not UNSET:
            field_dict["description"] = description
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if node_type is not UNSET:
            field_dict["node_type"] = node_type
        if remediation_ansible is not UNSET:
            field_dict["remediation_ansible"] = remediation_ansible
        if remediation_puppet is not UNSET:
            field_dict["remediation_puppet"] = remediation_puppet
        if remediation_script is not UNSET:
            field_dict["remediation_script"] = remediation_script
        if resource is not UNSET:
            field_dict["resource"] = resource
        if scan_id is not UNSET:
            field_dict["scan_id"] = scan_id
        if status is not UNSET:
            field_dict["status"] = status
        if test_category is not UNSET:
            field_dict["test_category"] = test_category
        if test_desc is not UNSET:
            field_dict["test_desc"] = test_desc
        if test_number is not UNSET:
            field_dict["test_number"] = test_number
        if test_rationale is not UNSET:
            field_dict["test_rationale"] = test_rationale
        if test_severity is not UNSET:
            field_dict["test_severity"] = test_severity
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        compliance_check_type = d.pop("compliance_check_type", UNSET)

        description = d.pop("description", UNSET)

        node_id = d.pop("node_id", UNSET)

        node_type = d.pop("node_type", UNSET)

        remediation_ansible = d.pop("remediation_ansible", UNSET)

        remediation_puppet = d.pop("remediation_puppet", UNSET)

        remediation_script = d.pop("remediation_script", UNSET)

        resource = d.pop("resource", UNSET)

        scan_id = d.pop("scan_id", UNSET)

        status = d.pop("status", UNSET)

        test_category = d.pop("test_category", UNSET)

        test_desc = d.pop("test_desc", UNSET)

        test_number = d.pop("test_number", UNSET)

        test_rationale = d.pop("test_rationale", UNSET)

        test_severity = d.pop("test_severity", UNSET)

        type = d.pop("type", UNSET)

        ingesters_compliance = cls(
            compliance_check_type=compliance_check_type,
            description=description,
            node_id=node_id,
            node_type=node_type,
            remediation_ansible=remediation_ansible,
            remediation_puppet=remediation_puppet,
            remediation_script=remediation_script,
            resource=resource,
            scan_id=scan_id,
            status=status,
            test_category=test_category,
            test_desc=test_desc,
            test_number=test_number,
            test_rationale=test_rationale,
            test_severity=test_severity,
            type=type,
        )

        ingesters_compliance.additional_properties = d
        return ingesters_compliance

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
