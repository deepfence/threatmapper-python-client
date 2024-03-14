from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.detailed_node_summaries import DetailedNodeSummaries
    from ..models.detailed_topology_connection_summaries import DetailedTopologyConnectionSummaries


T = TypeVar("T", bound="ModelGraphResult")


@_attrs_define
class ModelGraphResult:
    """
    Attributes:
        edges (DetailedTopologyConnectionSummaries):
        nodes (DetailedNodeSummaries):
    """

    edges: "DetailedTopologyConnectionSummaries"
    nodes: "DetailedNodeSummaries"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        edges = self.edges.to_dict()

        nodes = self.nodes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "edges": edges,
                "nodes": nodes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.detailed_node_summaries import DetailedNodeSummaries
        from ..models.detailed_topology_connection_summaries import DetailedTopologyConnectionSummaries

        d = src_dict.copy()
        edges = DetailedTopologyConnectionSummaries.from_dict(d.pop("edges"))

        nodes = DetailedNodeSummaries.from_dict(d.pop("nodes"))

        model_graph_result = cls(
            edges=edges,
            nodes=nodes,
        )

        model_graph_result.additional_properties = d
        return model_graph_result

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
