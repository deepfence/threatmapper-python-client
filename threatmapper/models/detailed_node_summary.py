from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_metadata import ReportMetadata


T = TypeVar("T", bound="DetailedNodeSummary")


@_attrs_define
class DetailedNodeSummary:
    """
    Attributes:
        adjacency (Union[Unset, List[str]]):
        id (Union[Unset, str]):
        ids (Union[Unset, List[str]]):
        immediate_parent_id (Union[Unset, str]):
        label (Union[Unset, str]):
        metadata (Union[Unset, ReportMetadata]):
        type (Union[Unset, str]):
    """

    adjacency: Union[Unset, List[str]] = UNSET
    id: Union[Unset, str] = UNSET
    ids: Union[Unset, List[str]] = UNSET
    immediate_parent_id: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ReportMetadata"] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        adjacency: Union[Unset, List[str]] = UNSET
        if not isinstance(self.adjacency, Unset):
            adjacency = self.adjacency

        id = self.id

        ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        immediate_parent_id = self.immediate_parent_id

        label = self.label

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adjacency is not UNSET:
            field_dict["adjacency"] = adjacency
        if id is not UNSET:
            field_dict["id"] = id
        if ids is not UNSET:
            field_dict["ids"] = ids
        if immediate_parent_id is not UNSET:
            field_dict["immediate_parent_id"] = immediate_parent_id
        if label is not UNSET:
            field_dict["label"] = label
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_metadata import ReportMetadata

        d = src_dict.copy()
        adjacency = cast(List[str], d.pop("adjacency", UNSET))

        id = d.pop("id", UNSET)

        ids = cast(List[str], d.pop("ids", UNSET))

        immediate_parent_id = d.pop("immediate_parent_id", UNSET)

        label = d.pop("label", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ReportMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ReportMetadata.from_dict(_metadata)

        type = d.pop("type", UNSET)

        detailed_node_summary = cls(
            adjacency=adjacency,
            id=id,
            ids=ids,
            immediate_parent_id=immediate_parent_id,
            label=label,
            metadata=metadata,
            type=type,
        )

        detailed_node_summary.additional_properties = d
        return detailed_node_summary

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
