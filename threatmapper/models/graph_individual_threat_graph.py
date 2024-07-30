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
        attack_path (Union[List[List[str]], None, Unset]):
        cve_attack_vector (Union[Unset, str]):
        cve_id (Union[List[str], None, Unset]):
        ports (Union[List[Any], None, Unset]):
    """

    attack_path: Union[List[List[str]], None, Unset] = UNSET
    cve_attack_vector: Union[Unset, str] = UNSET
    cve_id: Union[List[str], None, Unset] = UNSET
    ports: Union[List[Any], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attack_path: Union[List[List[str]], None, Unset]
        if isinstance(self.attack_path, Unset):
            attack_path = UNSET
        elif isinstance(self.attack_path, list):
            attack_path = []
            for attack_path_type_0_item_data in self.attack_path:
                attack_path_type_0_item = attack_path_type_0_item_data

                attack_path.append(attack_path_type_0_item)

        else:
            attack_path = self.attack_path

        cve_attack_vector = self.cve_attack_vector

        cve_id: Union[List[str], None, Unset]
        if isinstance(self.cve_id, Unset):
            cve_id = UNSET
        elif isinstance(self.cve_id, list):
            cve_id = self.cve_id

        else:
            cve_id = self.cve_id

        ports: Union[List[Any], None, Unset]
        if isinstance(self.ports, Unset):
            ports = UNSET
        elif isinstance(self.ports, list):
            ports = self.ports

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

        def _parse_attack_path(data: object) -> Union[List[List[str]], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
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
            return cast(Union[List[List[str]], None, Unset], data)

        attack_path = _parse_attack_path(d.pop("attack_path", UNSET))

        cve_attack_vector = d.pop("cve_attack_vector", UNSET)

        def _parse_cve_id(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cve_id_type_0 = cast(List[str], data)

                return cve_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        cve_id = _parse_cve_id(d.pop("cve_id", UNSET))

        def _parse_ports(data: object) -> Union[List[Any], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ports_type_0 = cast(List[Any], data)

                return ports_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[Any], None, Unset], data)

        ports = _parse_ports(d.pop("ports", UNSET))

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
