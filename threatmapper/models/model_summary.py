from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelSummary")


@_attrs_define
class ModelSummary:
    """
    Example:
        {'images': 0, 'scans_total': 5, 'registries': 6, 'scans_complete': 1, 'scans_in_progress': 5, 'tags': 2}

    Attributes:
        images (Union[Unset, int]):
        registries (Union[Unset, int]):
        scans_complete (Union[Unset, int]):
        scans_in_progress (Union[Unset, int]):
        scans_total (Union[Unset, int]):
        tags (Union[Unset, int]):
    """

    images: Union[Unset, int] = UNSET
    registries: Union[Unset, int] = UNSET
    scans_complete: Union[Unset, int] = UNSET
    scans_in_progress: Union[Unset, int] = UNSET
    scans_total: Union[Unset, int] = UNSET
    tags: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        images = self.images
        registries = self.registries
        scans_complete = self.scans_complete
        scans_in_progress = self.scans_in_progress
        scans_total = self.scans_total
        tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if images is not UNSET:
            field_dict["images"] = images
        if registries is not UNSET:
            field_dict["registries"] = registries
        if scans_complete is not UNSET:
            field_dict["scans_complete"] = scans_complete
        if scans_in_progress is not UNSET:
            field_dict["scans_in_progress"] = scans_in_progress
        if scans_total is not UNSET:
            field_dict["scans_total"] = scans_total
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        images = d.pop("images", UNSET)

        registries = d.pop("registries", UNSET)

        scans_complete = d.pop("scans_complete", UNSET)

        scans_in_progress = d.pop("scans_in_progress", UNSET)

        scans_total = d.pop("scans_total", UNSET)

        tags = d.pop("tags", UNSET)

        model_summary = cls(
            images=images,
            registries=registries,
            scans_complete=scans_complete,
            scans_in_progress=scans_in_progress,
            scans_total=scans_total,
            tags=tags,
        )

        model_summary.additional_properties = d
        return model_summary

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