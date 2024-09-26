from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IngestersSecretMatch")


@_attrs_define
class IngestersSecretMatch:
    """
    Attributes:
        full_filename (Union[Unset, str]):
        matched_content (Union[Unset, str]):
        relative_ending_index (Union[Unset, int]):
        relative_starting_index (Union[Unset, int]):
        starting_index (Union[Unset, int]):
    """

    full_filename: Union[Unset, str] = UNSET
    matched_content: Union[Unset, str] = UNSET
    relative_ending_index: Union[Unset, int] = UNSET
    relative_starting_index: Union[Unset, int] = UNSET
    starting_index: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        full_filename = self.full_filename

        matched_content = self.matched_content

        relative_ending_index = self.relative_ending_index

        relative_starting_index = self.relative_starting_index

        starting_index = self.starting_index

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if full_filename is not UNSET:
            field_dict["full_filename"] = full_filename
        if matched_content is not UNSET:
            field_dict["matched_content"] = matched_content
        if relative_ending_index is not UNSET:
            field_dict["relative_ending_index"] = relative_ending_index
        if relative_starting_index is not UNSET:
            field_dict["relative_starting_index"] = relative_starting_index
        if starting_index is not UNSET:
            field_dict["starting_index"] = starting_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        full_filename = d.pop("full_filename", UNSET)

        matched_content = d.pop("matched_content", UNSET)

        relative_ending_index = d.pop("relative_ending_index", UNSET)

        relative_starting_index = d.pop("relative_starting_index", UNSET)

        starting_index = d.pop("starting_index", UNSET)

        ingesters_secret_match = cls(
            full_filename=full_filename,
            matched_content=matched_content,
            relative_ending_index=relative_ending_index,
            relative_starting_index=relative_starting_index,
            starting_index=starting_index,
        )

        ingesters_secret_match.additional_properties = d
        return ingesters_secret_match

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
