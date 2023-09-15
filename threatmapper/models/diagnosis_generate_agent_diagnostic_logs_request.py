from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.diagnosis_node_identifier import DiagnosisNodeIdentifier


T = TypeVar("T", bound="DiagnosisGenerateAgentDiagnosticLogsRequest")


@_attrs_define
class DiagnosisGenerateAgentDiagnosticLogsRequest:
    """
    Example:
        {'tail': 0, 'node_ids': [{'node_type': 'host', 'node_id': 'node_id'}, {'node_type': 'host', 'node_id':
            'node_id'}]}

    Attributes:
        tail (int):
        node_ids (Optional[List['DiagnosisNodeIdentifier']]):
    """

    tail: int
    node_ids: Optional[List["DiagnosisNodeIdentifier"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tail = self.tail
        if self.node_ids is None:
            node_ids = None
        else:
            node_ids = []
            for node_ids_item_data in self.node_ids:
                node_ids_item = node_ids_item_data.to_dict()

                node_ids.append(node_ids_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tail": tail,
                "node_ids": node_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.diagnosis_node_identifier import DiagnosisNodeIdentifier

        d = src_dict.copy()
        tail = d.pop("tail")

        node_ids = []
        _node_ids = d.pop("node_ids")
        for node_ids_item_data in _node_ids or []:
            node_ids_item = DiagnosisNodeIdentifier.from_dict(node_ids_item_data)

            node_ids.append(node_ids_item)

        diagnosis_generate_agent_diagnostic_logs_request = cls(
            tail=tail,
            node_ids=node_ids,
        )

        diagnosis_generate_agent_diagnostic_logs_request.additional_properties = d
        return diagnosis_generate_agent_diagnostic_logs_request

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
