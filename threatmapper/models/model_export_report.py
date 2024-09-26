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
        filters (Union[Unset, str]):
        from_timestamp (Union[Unset, int]):
        report_id (Union[Unset, str]):
        status (Union[Unset, str]):
        status_message (Union[Unset, str]):
        storage_path (Union[Unset, str]):
        to_timestamp (Union[Unset, int]):
        type (Union[Unset, str]):
        updated_at (Union[Unset, int]):
        url (Union[Unset, str]):
    """

    created_at: Union[Unset, int] = UNSET
    filters: Union[Unset, str] = UNSET
    from_timestamp: Union[Unset, int] = UNSET
    report_id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    status_message: Union[Unset, str] = UNSET
    storage_path: Union[Unset, str] = UNSET
    to_timestamp: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at

        filters = self.filters

        from_timestamp = self.from_timestamp

        report_id = self.report_id

        status = self.status

        status_message = self.status_message

        storage_path = self.storage_path

        to_timestamp = self.to_timestamp

        type = self.type

        updated_at = self.updated_at

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if filters is not UNSET:
            field_dict["filters"] = filters
        if from_timestamp is not UNSET:
            field_dict["from_timestamp"] = from_timestamp
        if report_id is not UNSET:
            field_dict["report_id"] = report_id
        if status is not UNSET:
            field_dict["status"] = status
        if status_message is not UNSET:
            field_dict["status_message"] = status_message
        if storage_path is not UNSET:
            field_dict["storage_path"] = storage_path
        if to_timestamp is not UNSET:
            field_dict["to_timestamp"] = to_timestamp
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

        filters = d.pop("filters", UNSET)

        from_timestamp = d.pop("from_timestamp", UNSET)

        report_id = d.pop("report_id", UNSET)

        status = d.pop("status", UNSET)

        status_message = d.pop("status_message", UNSET)

        storage_path = d.pop("storage_path", UNSET)

        to_timestamp = d.pop("to_timestamp", UNSET)

        type = d.pop("type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        model_export_report = cls(
            created_at=created_at,
            filters=filters,
            from_timestamp=from_timestamp,
            report_id=report_id,
            status=status,
            status_message=status_message,
            storage_path=storage_path,
            to_timestamp=to_timestamp,
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
