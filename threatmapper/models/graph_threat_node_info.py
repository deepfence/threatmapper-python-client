from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.graph_threat_node_info_nodes_type_0 import GraphThreatNodeInfoNodesType0


T = TypeVar("T", bound="GraphThreatNodeInfo")


@_attrs_define
class GraphThreatNodeInfo:
    """
    Attributes:
        attack_path (Union[List[List[str]], None]):
        cloud_compliance_count (int):
        cloud_warn_alarm_count (int):
        compliance_count (int):
        count (int):
        exploitable_secrets_count (int):
        exploitable_vulnerabilities_count (int):
        id (str):
        label (str):
        node_type (str):
        nodes (Union['GraphThreatNodeInfoNodesType0', None]):
        secrets_count (int):
        vulnerability_count (int):
        warn_alarm_count (int):
    """

    attack_path: Union[List[List[str]], None]
    cloud_compliance_count: int
    cloud_warn_alarm_count: int
    compliance_count: int
    count: int
    exploitable_secrets_count: int
    exploitable_vulnerabilities_count: int
    id: str
    label: str
    node_type: str
    nodes: Union["GraphThreatNodeInfoNodesType0", None]
    secrets_count: int
    vulnerability_count: int
    warn_alarm_count: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.graph_threat_node_info_nodes_type_0 import GraphThreatNodeInfoNodesType0

        attack_path: Union[List[List[str]], None]
        if isinstance(self.attack_path, list):
            attack_path = []
            for attack_path_type_0_item_data in self.attack_path:
                attack_path_type_0_item = attack_path_type_0_item_data

                attack_path.append(attack_path_type_0_item)

        else:
            attack_path = self.attack_path

        cloud_compliance_count = self.cloud_compliance_count

        cloud_warn_alarm_count = self.cloud_warn_alarm_count

        compliance_count = self.compliance_count

        count = self.count

        exploitable_secrets_count = self.exploitable_secrets_count

        exploitable_vulnerabilities_count = self.exploitable_vulnerabilities_count

        id = self.id

        label = self.label

        node_type = self.node_type

        nodes: Union[Dict[str, Any], None]
        if isinstance(self.nodes, GraphThreatNodeInfoNodesType0):
            nodes = self.nodes.to_dict()
        else:
            nodes = self.nodes

        secrets_count = self.secrets_count

        vulnerability_count = self.vulnerability_count

        warn_alarm_count = self.warn_alarm_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attack_path": attack_path,
                "cloud_compliance_count": cloud_compliance_count,
                "cloud_warn_alarm_count": cloud_warn_alarm_count,
                "compliance_count": compliance_count,
                "count": count,
                "exploitable_secrets_count": exploitable_secrets_count,
                "exploitable_vulnerabilities_count": exploitable_vulnerabilities_count,
                "id": id,
                "label": label,
                "node_type": node_type,
                "nodes": nodes,
                "secrets_count": secrets_count,
                "vulnerability_count": vulnerability_count,
                "warn_alarm_count": warn_alarm_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.graph_threat_node_info_nodes_type_0 import GraphThreatNodeInfoNodesType0

        d = src_dict.copy()

        def _parse_attack_path(data: object) -> Union[List[List[str]], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attack_path_type_0 = []
                _attack_path_type_0 = data
                for attack_path_type_0_item_data in _attack_path_type_0:
                    attack_path_type_0_item = cast(List[str], attack_path_type_0_item_data)

                    attack_path_type_0.append(attack_path_type_0_item)

                return attack_path_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[List[str]], None], data)

        attack_path = _parse_attack_path(d.pop("attack_path"))

        cloud_compliance_count = d.pop("cloud_compliance_count")

        cloud_warn_alarm_count = d.pop("cloud_warn_alarm_count")

        compliance_count = d.pop("compliance_count")

        count = d.pop("count")

        exploitable_secrets_count = d.pop("exploitable_secrets_count")

        exploitable_vulnerabilities_count = d.pop("exploitable_vulnerabilities_count")

        id = d.pop("id")

        label = d.pop("label")

        node_type = d.pop("node_type")

        def _parse_nodes(data: object) -> Union["GraphThreatNodeInfoNodesType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nodes_type_0 = GraphThreatNodeInfoNodesType0.from_dict(data)

                return nodes_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GraphThreatNodeInfoNodesType0", None], data)

        nodes = _parse_nodes(d.pop("nodes"))

        secrets_count = d.pop("secrets_count")

        vulnerability_count = d.pop("vulnerability_count")

        warn_alarm_count = d.pop("warn_alarm_count")

        graph_threat_node_info = cls(
            attack_path=attack_path,
            cloud_compliance_count=cloud_compliance_count,
            cloud_warn_alarm_count=cloud_warn_alarm_count,
            compliance_count=compliance_count,
            count=count,
            exploitable_secrets_count=exploitable_secrets_count,
            exploitable_vulnerabilities_count=exploitable_vulnerabilities_count,
            id=id,
            label=label,
            node_type=node_type,
            nodes=nodes,
            secrets_count=secrets_count,
            vulnerability_count=vulnerability_count,
            warn_alarm_count=warn_alarm_count,
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
