from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelSecret")


@_attrs_define
class ModelSecret:
    """
    Example:
        {'full_filename': 'full_filename', 'level': 'level', 'masked': True, 'part': 'part', 'relative_ending_index': 0,
            'starting_index': 5, 'resources': ['resources', 'resources'], 'signature_to_match': 'signature_to_match',
            'rule_id': 1, 'score': 5.962133916683182, 'matched_content': 'matched_content', 'updated_at': 2, 'name': 'name',
            'relative_starting_index': 6, 'node_id': 'node_id'}

    Attributes:
        full_filename (str):
        level (str):
        masked (bool):
        matched_content (str):
        name (str):
        node_id (str):
        part (str):
        relative_ending_index (int):
        relative_starting_index (int):
        rule_id (int):
        score (float):
        signature_to_match (str):
        starting_index (int):
        updated_at (int):
        resources (Union[Unset, None, List[str]]):
    """

    full_filename: str
    level: str
    masked: bool
    matched_content: str
    name: str
    node_id: str
    part: str
    relative_ending_index: int
    relative_starting_index: int
    rule_id: int
    score: float
    signature_to_match: str
    starting_index: int
    updated_at: int
    resources: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        full_filename = self.full_filename
        level = self.level
        masked = self.masked
        matched_content = self.matched_content
        name = self.name
        node_id = self.node_id
        part = self.part
        relative_ending_index = self.relative_ending_index
        relative_starting_index = self.relative_starting_index
        rule_id = self.rule_id
        score = self.score
        signature_to_match = self.signature_to_match
        starting_index = self.starting_index
        updated_at = self.updated_at
        resources: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.resources, Unset):
            if self.resources is None:
                resources = None
            else:
                resources = self.resources

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "full_filename": full_filename,
                "level": level,
                "masked": masked,
                "matched_content": matched_content,
                "name": name,
                "node_id": node_id,
                "part": part,
                "relative_ending_index": relative_ending_index,
                "relative_starting_index": relative_starting_index,
                "rule_id": rule_id,
                "score": score,
                "signature_to_match": signature_to_match,
                "starting_index": starting_index,
                "updated_at": updated_at,
            }
        )
        if resources is not UNSET:
            field_dict["resources"] = resources

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        full_filename = d.pop("full_filename")

        level = d.pop("level")

        masked = d.pop("masked")

        matched_content = d.pop("matched_content")

        name = d.pop("name")

        node_id = d.pop("node_id")

        part = d.pop("part")

        relative_ending_index = d.pop("relative_ending_index")

        relative_starting_index = d.pop("relative_starting_index")

        rule_id = d.pop("rule_id")

        score = d.pop("score")

        signature_to_match = d.pop("signature_to_match")

        starting_index = d.pop("starting_index")

        updated_at = d.pop("updated_at")

        resources = cast(List[str], d.pop("resources", UNSET))

        model_secret = cls(
            full_filename=full_filename,
            level=level,
            masked=masked,
            matched_content=matched_content,
            name=name,
            node_id=node_id,
            part=part,
            relative_ending_index=relative_ending_index,
            relative_starting_index=relative_starting_index,
            rule_id=rule_id,
            score=score,
            signature_to_match=signature_to_match,
            starting_index=starting_index,
            updated_at=updated_at,
            resources=resources,
        )

        model_secret.additional_properties = d
        return model_secret

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
