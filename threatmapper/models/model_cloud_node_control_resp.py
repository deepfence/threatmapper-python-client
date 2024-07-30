from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cloud_node_compliance_control import ModelCloudNodeComplianceControl


T = TypeVar("T", bound="ModelCloudNodeControlResp")


@_attrs_define
class ModelCloudNodeControlResp:
    """
    Example:
        {'controls': [{'category_hierarchy': ['category_hierarchy', 'category_hierarchy'], 'control_id': 'control_id',
            'service': 'service', 'description': 'description', 'compliance_type': 'compliance_type', 'problem_title':
            'problem_title', 'title': 'title', 'category_hierarchy_short': 'category_hierarchy_short', 'enabled': True,
            'node_id': 'node_id'}, {'category_hierarchy': ['category_hierarchy', 'category_hierarchy'], 'control_id':
            'control_id', 'service': 'service', 'description': 'description', 'compliance_type': 'compliance_type',
            'problem_title': 'problem_title', 'title': 'title', 'category_hierarchy_short': 'category_hierarchy_short',
            'enabled': True, 'node_id': 'node_id'}]}

    Attributes:
        controls (Union[List['ModelCloudNodeComplianceControl'], None, Unset]):
    """

    controls: Union[List["ModelCloudNodeComplianceControl"], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        controls: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.controls, Unset):
            controls = UNSET
        elif isinstance(self.controls, list):
            controls = []
            for controls_type_0_item_data in self.controls:
                controls_type_0_item = controls_type_0_item_data.to_dict()
                controls.append(controls_type_0_item)

        else:
            controls = self.controls

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if controls is not UNSET:
            field_dict["controls"] = controls

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_cloud_node_compliance_control import ModelCloudNodeComplianceControl

        d = src_dict.copy()

        def _parse_controls(data: object) -> Union[List["ModelCloudNodeComplianceControl"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                controls_type_0 = []
                _controls_type_0 = data
                for controls_type_0_item_data in _controls_type_0:
                    controls_type_0_item = ModelCloudNodeComplianceControl.from_dict(controls_type_0_item_data)

                    controls_type_0.append(controls_type_0_item)

                return controls_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelCloudNodeComplianceControl"], None, Unset], data)

        controls = _parse_controls(d.pop("controls", UNSET))

        model_cloud_node_control_resp = cls(
            controls=controls,
        )

        model_cloud_node_control_resp.additional_properties = d
        return model_cloud_node_control_resp

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
