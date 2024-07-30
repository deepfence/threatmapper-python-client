from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelCloudComplianceControl")


@_attrs_define
class ModelCloudComplianceControl:
    """
    Example:
        {'control_id': 'control_id', 'documentation': 'documentation', 'active': True, 'description': 'description',
            'cloud_provider': 'cloud_provider', 'title': 'title', 'category_hierarchy_short': 'category_hierarchy_short',
            'executable': True, 'category_hierarchy': ['category_hierarchy', 'category_hierarchy'], 'service': 'service',
            'parent_control_hierarchy': ['parent_control_hierarchy', 'parent_control_hierarchy'], 'compliance_type':
            'compliance_type', 'disabled': True, 'category': 'category', 'node_id': 'node_id'}

    Attributes:
        active (Union[Unset, bool]):
        category (Union[Unset, str]):
        category_hierarchy (Union[List[str], None, Unset]):
        category_hierarchy_short (Union[Unset, str]):
        cloud_provider (Union[Unset, str]):
        compliance_type (Union[Unset, str]):
        control_id (Union[Unset, str]):
        description (Union[Unset, str]):
        disabled (Union[Unset, bool]):
        documentation (Union[Unset, str]):
        executable (Union[Unset, bool]):
        node_id (Union[Unset, str]):
        parent_control_hierarchy (Union[List[str], None, Unset]):
        service (Union[Unset, str]):
        title (Union[Unset, str]):
    """

    active: Union[Unset, bool] = UNSET
    category: Union[Unset, str] = UNSET
    category_hierarchy: Union[List[str], None, Unset] = UNSET
    category_hierarchy_short: Union[Unset, str] = UNSET
    cloud_provider: Union[Unset, str] = UNSET
    compliance_type: Union[Unset, str] = UNSET
    control_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET
    documentation: Union[Unset, str] = UNSET
    executable: Union[Unset, bool] = UNSET
    node_id: Union[Unset, str] = UNSET
    parent_control_hierarchy: Union[List[str], None, Unset] = UNSET
    service: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active = self.active

        category = self.category

        category_hierarchy: Union[List[str], None, Unset]
        if isinstance(self.category_hierarchy, Unset):
            category_hierarchy = UNSET
        elif isinstance(self.category_hierarchy, list):
            category_hierarchy = self.category_hierarchy

        else:
            category_hierarchy = self.category_hierarchy

        category_hierarchy_short = self.category_hierarchy_short

        cloud_provider = self.cloud_provider

        compliance_type = self.compliance_type

        control_id = self.control_id

        description = self.description

        disabled = self.disabled

        documentation = self.documentation

        executable = self.executable

        node_id = self.node_id

        parent_control_hierarchy: Union[List[str], None, Unset]
        if isinstance(self.parent_control_hierarchy, Unset):
            parent_control_hierarchy = UNSET
        elif isinstance(self.parent_control_hierarchy, list):
            parent_control_hierarchy = self.parent_control_hierarchy

        else:
            parent_control_hierarchy = self.parent_control_hierarchy

        service = self.service

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if category is not UNSET:
            field_dict["category"] = category
        if category_hierarchy is not UNSET:
            field_dict["category_hierarchy"] = category_hierarchy
        if category_hierarchy_short is not UNSET:
            field_dict["category_hierarchy_short"] = category_hierarchy_short
        if cloud_provider is not UNSET:
            field_dict["cloud_provider"] = cloud_provider
        if compliance_type is not UNSET:
            field_dict["compliance_type"] = compliance_type
        if control_id is not UNSET:
            field_dict["control_id"] = control_id
        if description is not UNSET:
            field_dict["description"] = description
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if documentation is not UNSET:
            field_dict["documentation"] = documentation
        if executable is not UNSET:
            field_dict["executable"] = executable
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if parent_control_hierarchy is not UNSET:
            field_dict["parent_control_hierarchy"] = parent_control_hierarchy
        if service is not UNSET:
            field_dict["service"] = service
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        active = d.pop("active", UNSET)

        category = d.pop("category", UNSET)

        def _parse_category_hierarchy(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                category_hierarchy_type_0 = cast(List[str], data)

                return category_hierarchy_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        category_hierarchy = _parse_category_hierarchy(d.pop("category_hierarchy", UNSET))

        category_hierarchy_short = d.pop("category_hierarchy_short", UNSET)

        cloud_provider = d.pop("cloud_provider", UNSET)

        compliance_type = d.pop("compliance_type", UNSET)

        control_id = d.pop("control_id", UNSET)

        description = d.pop("description", UNSET)

        disabled = d.pop("disabled", UNSET)

        documentation = d.pop("documentation", UNSET)

        executable = d.pop("executable", UNSET)

        node_id = d.pop("node_id", UNSET)

        def _parse_parent_control_hierarchy(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                parent_control_hierarchy_type_0 = cast(List[str], data)

                return parent_control_hierarchy_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        parent_control_hierarchy = _parse_parent_control_hierarchy(d.pop("parent_control_hierarchy", UNSET))

        service = d.pop("service", UNSET)

        title = d.pop("title", UNSET)

        model_cloud_compliance_control = cls(
            active=active,
            category=category,
            category_hierarchy=category_hierarchy,
            category_hierarchy_short=category_hierarchy_short,
            cloud_provider=cloud_provider,
            compliance_type=compliance_type,
            control_id=control_id,
            description=description,
            disabled=disabled,
            documentation=documentation,
            executable=executable,
            node_id=node_id,
            parent_control_hierarchy=parent_control_hierarchy,
            service=service,
            title=title,
        )

        model_cloud_compliance_control.additional_properties = d
        return model_cloud_compliance_control

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
