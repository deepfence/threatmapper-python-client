from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.controls_action import ControlsAction


T = TypeVar("T", bound="ControlsAgentControls")


@_attrs_define
class ControlsAgentControls:
    """
    Example:
        {'beatrate': 0, 'commands': [{'id': 0, 'request_payload': 'request_payload'}, {'id': 0, 'request_payload':
            'request_payload'}]}

    Attributes:
        beatrate (int):
        commands (Optional[List['ControlsAction']]):
    """

    beatrate: int
    commands: Optional[List["ControlsAction"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        beatrate = self.beatrate
        if self.commands is None:
            commands = None
        else:
            commands = []
            for commands_item_data in self.commands:
                commands_item = commands_item_data.to_dict()

                commands.append(commands_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "beatrate": beatrate,
                "commands": commands,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controls_action import ControlsAction

        d = src_dict.copy()
        beatrate = d.pop("beatrate")

        commands = []
        _commands = d.pop("commands")
        for commands_item_data in _commands or []:
            commands_item = ControlsAction.from_dict(commands_item_data)

            commands.append(commands_item)

        controls_agent_controls = cls(
            beatrate=beatrate,
            commands=commands,
        )

        controls_agent_controls.additional_properties = d
        return controls_agent_controls

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
