from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.diagnosis_node_identifier_node_type import DiagnosisNodeIdentifierNodeType

T = TypeVar("T", bound="DiagnosisNodeIdentifier")


@_attrs_define
class DiagnosisNodeIdentifier:
    """
    Attributes:
        node_id (str):
        node_type (DiagnosisNodeIdentifierNodeType):
    """

    node_id: str
    node_type: DiagnosisNodeIdentifierNodeType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_id = self.node_id

        node_type = self.node_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_id": node_id,
                "node_type": node_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        node_id = d.pop("node_id")

        node_type = DiagnosisNodeIdentifierNodeType(d.pop("node_type"))

        diagnosis_node_identifier = cls(
            node_id=node_id,
            node_type=node_type,
        )

        diagnosis_node_identifier.additional_properties = d
        return diagnosis_node_identifier

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
