from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GraphIndividualThreatGraph")


@_attrs_define
class GraphIndividualThreatGraph:
    """
    Example:
        {'cve_id': ['cve_id', 'cve_id'], 'ports': ['', ''], 'attack_path': [['attack_path', 'attack_path'],
            ['attack_path', 'attack_path']], 'cve_attack_vector': 'cve_attack_vector'}

    Attributes:
        attack_path (Union[Unset, None, List[List[str]]]):
        cve_attack_vector (Union[Unset, str]):
        cve_id (Union[Unset, None, List[str]]):
        ports (Union[Unset, None, List[Any]]):
    """

    attack_path: Union[Unset, None, List[List[str]]] = UNSET
    cve_attack_vector: Union[Unset, str] = UNSET
    cve_id: Union[Unset, None, List[str]] = UNSET
    ports: Union[Unset, None, List[Any]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attack_path: Union[Unset, None, List[List[str]]] = UNSET
        if not isinstance(self.attack_path, Unset):
            if self.attack_path is None:
                attack_path = None
            else:
                attack_path = []
                for attack_path_item_data in self.attack_path:
                    attack_path_item = attack_path_item_data

                    attack_path.append(attack_path_item)

        cve_attack_vector = self.cve_attack_vector
        cve_id: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.cve_id, Unset):
            if self.cve_id is None:
                cve_id = None
            else:
                cve_id = self.cve_id

        ports: Union[Unset, None, List[Any]] = UNSET
        if not isinstance(self.ports, Unset):
            if self.ports is None:
                ports = None
            else:
                ports = self.ports

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attack_path is not UNSET:
            field_dict["attack_path"] = attack_path
        if cve_attack_vector is not UNSET:
            field_dict["cve_attack_vector"] = cve_attack_vector
        if cve_id is not UNSET:
            field_dict["cve_id"] = cve_id
        if ports is not UNSET:
            field_dict["ports"] = ports

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attack_path = []
        _attack_path = d.pop("attack_path", UNSET)
        for attack_path_item_data in _attack_path or []:
            attack_path_item = cast(List[str], attack_path_item_data)

            attack_path.append(attack_path_item)

        cve_attack_vector = d.pop("cve_attack_vector", UNSET)

        cve_id = cast(List[str], d.pop("cve_id", UNSET))

        ports = cast(List[Any], d.pop("ports", UNSET))

        graph_individual_threat_graph = cls(
            attack_path=attack_path,
            cve_attack_vector=cve_attack_vector,
            cve_id=cve_id,
            ports=ports,
        )

        graph_individual_threat_graph.additional_properties = d
        return graph_individual_threat_graph

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
