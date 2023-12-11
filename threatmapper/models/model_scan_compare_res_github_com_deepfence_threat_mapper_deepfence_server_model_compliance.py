from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_compliance import ModelCompliance


T = TypeVar("T", bound="ModelScanCompareResGithubComDeepfenceThreatMapperDeepfenceServerModelCompliance")


@_attrs_define
class ModelScanCompareResGithubComDeepfenceThreatMapperDeepfenceServerModelCompliance:
    """
    Example:
        {'new': [{'resource': 'resource', 'masked': True, 'description': 'description', 'resources': [{'node_type':
            'node_type', 'name': 'name', 'host_name': 'host_name', 'node_id': 'node_id'}, {'node_type': 'node_type', 'name':
            'name', 'host_name': 'host_name', 'node_id': 'node_id'}], 'test_category': 'test_category',
            'remediation_ansible': 'remediation_ansible', 'compliance_check_type': 'compliance_check_type', 'rule_id':
            'rule_id', 'test_rationale': 'test_rationale', 'test_severity': 'test_severity', 'node_type': 'node_type',
            'updated_at': 0, 'remediation_puppet': 'remediation_puppet', 'remediation_script': 'remediation_script',
            'node_id': 'node_id', 'status': 'status', 'test_desc': 'test_desc', 'test_number': 'test_number'}, {'resource':
            'resource', 'masked': True, 'description': 'description', 'resources': [{'node_type': 'node_type', 'name':
            'name', 'host_name': 'host_name', 'node_id': 'node_id'}, {'node_type': 'node_type', 'name': 'name', 'host_name':
            'host_name', 'node_id': 'node_id'}], 'test_category': 'test_category', 'remediation_ansible':
            'remediation_ansible', 'compliance_check_type': 'compliance_check_type', 'rule_id': 'rule_id', 'test_rationale':
            'test_rationale', 'test_severity': 'test_severity', 'node_type': 'node_type', 'updated_at': 0,
            'remediation_puppet': 'remediation_puppet', 'remediation_script': 'remediation_script', 'node_id': 'node_id',
            'status': 'status', 'test_desc': 'test_desc', 'test_number': 'test_number'}]}

    Attributes:
        new (Optional[List['ModelCompliance']]):
    """

    new: Optional[List["ModelCompliance"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if self.new is None:
            new = None
        else:
            new = []
            for new_item_data in self.new:
                new_item = new_item_data.to_dict()

                new.append(new_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "new": new,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_compliance import ModelCompliance

        d = src_dict.copy()
        new = []
        _new = d.pop("new")
        for new_item_data in _new or []:
            new_item = ModelCompliance.from_dict(new_item_data)

            new.append(new_item)

        model_scan_compare_res_github_com_deepfence_threat_mapper_deepfence_server_model_compliance = cls(
            new=new,
        )

        model_scan_compare_res_github_com_deepfence_threat_mapper_deepfence_server_model_compliance.additional_properties = (
            d
        )
        return model_scan_compare_res_github_com_deepfence_threat_mapper_deepfence_server_model_compliance

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
