from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelAgentPluginDisable")


@_attrs_define
class ModelAgentPluginDisable:
    """
    Attributes:
        node_id (str):
        plugin_name (str):
    """

    node_id: str
    plugin_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_id = self.node_id

        plugin_name = self.plugin_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_id": node_id,
                "plugin_name": plugin_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        node_id = d.pop("node_id")

        plugin_name = d.pop("plugin_name")

        model_agent_plugin_disable = cls(
            node_id=node_id,
            plugin_name=plugin_name,
        )

        model_agent_plugin_disable.additional_properties = d
        return model_agent_plugin_disable

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
