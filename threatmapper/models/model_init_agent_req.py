from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelInitAgentReq")


@_attrs_define
class ModelInitAgentReq:
    """
    Example:
        {'node_type': 'node_type', 'available_workload': 0, 'version': 'version', 'node_id': 'node_id'}

    Attributes:
        available_workload (int):
        node_id (str):
        node_type (str):
        version (str):
    """

    available_workload: int
    node_id: str
    node_type: str
    version: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        available_workload = self.available_workload

        node_id = self.node_id

        node_type = self.node_type

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "available_workload": available_workload,
                "node_id": node_id,
                "node_type": node_type,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        available_workload = d.pop("available_workload")

        node_id = d.pop("node_id")

        node_type = d.pop("node_type")

        version = d.pop("version")

        model_init_agent_req = cls(
            available_workload=available_workload,
            node_id=node_id,
            node_type=node_type,
            version=version,
        )

        model_init_agent_req.additional_properties = d
        return model_init_agent_req

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
