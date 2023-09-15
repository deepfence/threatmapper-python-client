from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.graph_threat_node_info import GraphThreatNodeInfo


T = TypeVar("T", bound="GraphProviderThreatGraph")


@_attrs_define
class GraphProviderThreatGraph:
    """
    Attributes:
        cloud_compliance_count (int):
        compliance_count (int):
        secrets_count (int):
        vulnerability_count (int):
        resources (Optional[List['GraphThreatNodeInfo']]):
    """

    cloud_compliance_count: int
    compliance_count: int
    secrets_count: int
    vulnerability_count: int
    resources: Optional[List["GraphThreatNodeInfo"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloud_compliance_count = self.cloud_compliance_count
        compliance_count = self.compliance_count
        secrets_count = self.secrets_count
        vulnerability_count = self.vulnerability_count
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
                "cloud_compliance_count": cloud_compliance_count,
                "compliance_count": compliance_count,
                "secrets_count": secrets_count,
                "vulnerability_count": vulnerability_count,
                "resources": resources,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.graph_threat_node_info import GraphThreatNodeInfo

        d = src_dict.copy()
        cloud_compliance_count = d.pop("cloud_compliance_count")

        compliance_count = d.pop("compliance_count")

        secrets_count = d.pop("secrets_count")

        vulnerability_count = d.pop("vulnerability_count")

        resources = []
        _resources = d.pop("resources")
        for resources_item_data in _resources or []:
            resources_item = GraphThreatNodeInfo.from_dict(resources_item_data)

            resources.append(resources_item)

        graph_provider_threat_graph = cls(
            cloud_compliance_count=cloud_compliance_count,
            compliance_count=compliance_count,
            secrets_count=secrets_count,
            vulnerability_count=vulnerability_count,
            resources=resources,
        )

        graph_provider_threat_graph.additional_properties = d
        return graph_provider_threat_graph

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
