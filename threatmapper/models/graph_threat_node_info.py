from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.graph_threat_node_info_nodes import GraphThreatNodeInfoNodes


T = TypeVar("T", bound="GraphThreatNodeInfo")


@_attrs_define
class GraphThreatNodeInfo:
    """
    Attributes:
        cloud_compliance_count (int):
        compliance_count (int):
        count (int):
        id (str):
        label (str):
        node_type (str):
        secrets_count (int):
        vulnerability_count (int):
        attack_path (Optional[List[List[str]]]):
        nodes (Optional[GraphThreatNodeInfoNodes]):
    """

    cloud_compliance_count: int
    compliance_count: int
    count: int
    id: str
    label: str
    node_type: str
    secrets_count: int
    vulnerability_count: int
    attack_path: Optional[List[List[str]]]
    nodes: Optional["GraphThreatNodeInfoNodes"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloud_compliance_count = self.cloud_compliance_count
        compliance_count = self.compliance_count
        count = self.count
        id = self.id
        label = self.label
        node_type = self.node_type
        secrets_count = self.secrets_count
        vulnerability_count = self.vulnerability_count
        if self.attack_path is None:
            attack_path = None
        else:
            attack_path = []
            for attack_path_item_data in self.attack_path:
                attack_path_item = attack_path_item_data

                attack_path.append(attack_path_item)

        nodes = self.nodes.to_dict() if self.nodes else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_compliance_count": cloud_compliance_count,
                "compliance_count": compliance_count,
                "count": count,
                "id": id,
                "label": label,
                "node_type": node_type,
                "secrets_count": secrets_count,
                "vulnerability_count": vulnerability_count,
                "attack_path": attack_path,
                "nodes": nodes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.graph_threat_node_info_nodes import GraphThreatNodeInfoNodes

        d = src_dict.copy()
        cloud_compliance_count = d.pop("cloud_compliance_count")

        compliance_count = d.pop("compliance_count")

        count = d.pop("count")

        id = d.pop("id")

        label = d.pop("label")

        node_type = d.pop("node_type")

        secrets_count = d.pop("secrets_count")

        vulnerability_count = d.pop("vulnerability_count")

        attack_path = []
        _attack_path = d.pop("attack_path")
        for attack_path_item_data in _attack_path or []:
            attack_path_item = cast(List[str], attack_path_item_data)

            attack_path.append(attack_path_item)

        _nodes = d.pop("nodes")
        nodes: Optional[GraphThreatNodeInfoNodes]
        if _nodes is None:
            nodes = None
        else:
            nodes = GraphThreatNodeInfoNodes.from_dict(_nodes)

        graph_threat_node_info = cls(
            cloud_compliance_count=cloud_compliance_count,
            compliance_count=compliance_count,
            count=count,
            id=id,
            label=label,
            node_type=node_type,
            secrets_count=secrets_count,
            vulnerability_count=vulnerability_count,
            attack_path=attack_path,
            nodes=nodes,
        )

        graph_threat_node_info.additional_properties = d
        return graph_threat_node_info

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
