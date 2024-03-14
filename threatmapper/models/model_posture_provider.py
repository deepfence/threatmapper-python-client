from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelPostureProvider")


@_attrs_define
class ModelPostureProvider:
    """
    Attributes:
        compliance_percentage (Union[Unset, float]):
        name (Union[Unset, str]):
        node_count (Union[Unset, int]):
        node_count_inactive (Union[Unset, int]):
        node_label (Union[Unset, str]):
        resource_count (Union[Unset, int]):
        scan_count (Union[Unset, int]):
    """

    compliance_percentage: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    node_count: Union[Unset, int] = UNSET
    node_count_inactive: Union[Unset, int] = UNSET
    node_label: Union[Unset, str] = UNSET
    resource_count: Union[Unset, int] = UNSET
    scan_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compliance_percentage = self.compliance_percentage

        name = self.name

        node_count = self.node_count

        node_count_inactive = self.node_count_inactive

        node_label = self.node_label

        resource_count = self.resource_count

        scan_count = self.scan_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compliance_percentage is not UNSET:
            field_dict["compliance_percentage"] = compliance_percentage
        if name is not UNSET:
            field_dict["name"] = name
        if node_count is not UNSET:
            field_dict["node_count"] = node_count
        if node_count_inactive is not UNSET:
            field_dict["node_count_inactive"] = node_count_inactive
        if node_label is not UNSET:
            field_dict["node_label"] = node_label
        if resource_count is not UNSET:
            field_dict["resource_count"] = resource_count
        if scan_count is not UNSET:
            field_dict["scan_count"] = scan_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        compliance_percentage = d.pop("compliance_percentage", UNSET)

        name = d.pop("name", UNSET)

        node_count = d.pop("node_count", UNSET)

        node_count_inactive = d.pop("node_count_inactive", UNSET)

        node_label = d.pop("node_label", UNSET)

        resource_count = d.pop("resource_count", UNSET)

        scan_count = d.pop("scan_count", UNSET)

        model_posture_provider = cls(
            compliance_percentage=compliance_percentage,
            name=name,
            node_count=node_count,
            node_count_inactive=node_count_inactive,
            node_label=node_label,
            resource_count=resource_count,
            scan_count=scan_count,
        )

        model_posture_provider.additional_properties = d
        return model_posture_provider

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
