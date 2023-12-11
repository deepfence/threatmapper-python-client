from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_basic_node import ModelBasicNode


T = TypeVar("T", bound="ModelCompliance")


@_attrs_define
class ModelCompliance:
    """
    Example:
        {'resource': 'resource', 'masked': True, 'description': 'description', 'resources': [{'node_type': 'node_type',
            'name': 'name', 'host_name': 'host_name', 'node_id': 'node_id'}, {'node_type': 'node_type', 'name': 'name',
            'host_name': 'host_name', 'node_id': 'node_id'}], 'test_category': 'test_category', 'remediation_ansible':
            'remediation_ansible', 'compliance_check_type': 'compliance_check_type', 'rule_id': 'rule_id', 'test_rationale':
            'test_rationale', 'test_severity': 'test_severity', 'node_type': 'node_type', 'updated_at': 0,
            'remediation_puppet': 'remediation_puppet', 'remediation_script': 'remediation_script', 'node_id': 'node_id',
            'status': 'status', 'test_desc': 'test_desc', 'test_number': 'test_number'}

    Attributes:
        compliance_check_type (str):
        description (str):
        masked (bool):
        node_id (str):
        node_type (str):
        remediation_ansible (str):
        remediation_puppet (str):
        remediation_script (str):
        resource (str):
        rule_id (str):
        status (str):
        test_category (str):
        test_desc (str):
        test_number (str):
        test_rationale (str):
        test_severity (str):
        updated_at (int):
        resources (Union[Unset, None, List['ModelBasicNode']]):
    """

    compliance_check_type: str
    description: str
    masked: bool
    node_id: str
    node_type: str
    remediation_ansible: str
    remediation_puppet: str
    remediation_script: str
    resource: str
    rule_id: str
    status: str
    test_category: str
    test_desc: str
    test_number: str
    test_rationale: str
    test_severity: str
    updated_at: int
    resources: Union[Unset, None, List["ModelBasicNode"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compliance_check_type = self.compliance_check_type
        description = self.description
        masked = self.masked
        node_id = self.node_id
        node_type = self.node_type
        remediation_ansible = self.remediation_ansible
        remediation_puppet = self.remediation_puppet
        remediation_script = self.remediation_script
        resource = self.resource
        rule_id = self.rule_id
        status = self.status
        test_category = self.test_category
        test_desc = self.test_desc
        test_number = self.test_number
        test_rationale = self.test_rationale
        test_severity = self.test_severity
        updated_at = self.updated_at
        resources: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.resources, Unset):
            if self.resources is None:
                resources = None
            else:
                resources = []
                for resources_item_data in self.resources:
                    resources_item = resources_item_data.to_dict()

                    resources.append(resources_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "compliance_check_type": compliance_check_type,
                "description": description,
                "masked": masked,
                "node_id": node_id,
                "node_type": node_type,
                "remediation_ansible": remediation_ansible,
                "remediation_puppet": remediation_puppet,
                "remediation_script": remediation_script,
                "resource": resource,
                "rule_id": rule_id,
                "status": status,
                "test_category": test_category,
                "test_desc": test_desc,
                "test_number": test_number,
                "test_rationale": test_rationale,
                "test_severity": test_severity,
                "updated_at": updated_at,
            }
        )
        if resources is not UNSET:
            field_dict["resources"] = resources

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_basic_node import ModelBasicNode

        d = src_dict.copy()
        compliance_check_type = d.pop("compliance_check_type")

        description = d.pop("description")

        masked = d.pop("masked")

        node_id = d.pop("node_id")

        node_type = d.pop("node_type")

        remediation_ansible = d.pop("remediation_ansible")

        remediation_puppet = d.pop("remediation_puppet")

        remediation_script = d.pop("remediation_script")

        resource = d.pop("resource")

        rule_id = d.pop("rule_id")

        status = d.pop("status")

        test_category = d.pop("test_category")

        test_desc = d.pop("test_desc")

        test_number = d.pop("test_number")

        test_rationale = d.pop("test_rationale")

        test_severity = d.pop("test_severity")

        updated_at = d.pop("updated_at")

        resources = []
        _resources = d.pop("resources", UNSET)
        for resources_item_data in _resources or []:
            resources_item = ModelBasicNode.from_dict(resources_item_data)

            resources.append(resources_item)

        model_compliance = cls(
            compliance_check_type=compliance_check_type,
            description=description,
            masked=masked,
            node_id=node_id,
            node_type=node_type,
            remediation_ansible=remediation_ansible,
            remediation_puppet=remediation_puppet,
            remediation_script=remediation_script,
            resource=resource,
            rule_id=rule_id,
            status=status,
            test_category=test_category,
            test_desc=test_desc,
            test_number=test_number,
            test_rationale=test_rationale,
            test_severity=test_severity,
            updated_at=updated_at,
            resources=resources,
        )

        model_compliance.additional_properties = d
        return model_compliance

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
