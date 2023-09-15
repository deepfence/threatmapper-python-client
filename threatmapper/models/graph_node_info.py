from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GraphNodeInfo")


@_attrs_define
class GraphNodeInfo:
    """
    Attributes:
        cloud_compliance_count (int):
        compliance_count (int):
        name (str):
        node_id (str):
        secrets_count (int):
        vulnerability_count (int):
    """

    cloud_compliance_count: int
    compliance_count: int
    name: str
    node_id: str
    secrets_count: int
    vulnerability_count: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloud_compliance_count = self.cloud_compliance_count
        compliance_count = self.compliance_count
        name = self.name
        node_id = self.node_id
        secrets_count = self.secrets_count
        vulnerability_count = self.vulnerability_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_compliance_count": cloud_compliance_count,
                "compliance_count": compliance_count,
                "name": name,
                "node_id": node_id,
                "secrets_count": secrets_count,
                "vulnerability_count": vulnerability_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cloud_compliance_count = d.pop("cloud_compliance_count")

        compliance_count = d.pop("compliance_count")

        name = d.pop("name")

        node_id = d.pop("node_id")

        secrets_count = d.pop("secrets_count")

        vulnerability_count = d.pop("vulnerability_count")

        graph_node_info = cls(
            cloud_compliance_count=cloud_compliance_count,
            compliance_count=compliance_count,
            name=name,
            node_id=node_id,
            secrets_count=secrets_count,
            vulnerability_count=vulnerability_count,
        )

        graph_node_info.additional_properties = d
        return graph_node_info

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
