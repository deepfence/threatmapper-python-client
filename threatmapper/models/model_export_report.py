from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelExportReport")


@_attrs_define
class ModelExportReport:
    """
    Attributes:
        created_at (Union[Unset, int]):
        duration (Union[Unset, int]):
        filters (Union[Unset, str]):
        report_id (Union[Unset, str]):
        status (Union[Unset, str]):
        storage_path (Union[Unset, str]):
        type (Union[Unset, str]):
        updated_at (Union[Unset, int]):
        url (Union[Unset, str]):
    """

    created_at: Union[Unset, int] = UNSET
    duration: Union[Unset, int] = UNSET
    filters: Union[Unset, str] = UNSET
    report_id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    storage_path: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at

        duration = self.duration

        filters = self.filters

        report_id = self.report_id

        status = self.status

        storage_path = self.storage_path

        type = self.type

        updated_at = self.updated_at

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if duration is not UNSET:
            field_dict["duration"] = duration
        if filters is not UNSET:
            field_dict["filters"] = filters
        if report_id is not UNSET:
            field_dict["report_id"] = report_id
        if status is not UNSET:
            field_dict["status"] = status
        if storage_path is not UNSET:
            field_dict["storage_path"] = storage_path
        if type is not UNSET:
            field_dict["type"] = type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("created_at", UNSET)

        duration = d.pop("duration", UNSET)

        filters = d.pop("filters", UNSET)

        report_id = d.pop("report_id", UNSET)

        status = d.pop("status", UNSET)

        storage_path = d.pop("storage_path", UNSET)

        type = d.pop("type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        model_export_report = cls(
            created_at=created_at,
            duration=duration,
            filters=filters,
            report_id=report_id,
            status=status,
            storage_path=storage_path,
            type=type,
            updated_at=updated_at,
            url=url,
        )

        model_export_report.additional_properties = d
        return model_export_report

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
