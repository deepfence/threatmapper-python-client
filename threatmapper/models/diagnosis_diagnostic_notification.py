from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagnosisDiagnosticNotification")


@_attrs_define
class DiagnosisDiagnosticNotification:
    """
    Attributes:
        content (Union[Unset, str]):
        expiry_in_secs (Union[Unset, Any]):
        follow_url (Union[Unset, Any]):
        source_application_id (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    content: Union[Unset, str] = UNSET
    expiry_in_secs: Union[Unset, Any] = UNSET
    follow_url: Union[Unset, Any] = UNSET
    source_application_id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = self.content

        expiry_in_secs = self.expiry_in_secs

        follow_url = self.follow_url

        source_application_id = self.source_application_id

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if expiry_in_secs is not UNSET:
            field_dict["expiry_in_secs"] = expiry_in_secs
        if follow_url is not UNSET:
            field_dict["follow_url"] = follow_url
        if source_application_id is not UNSET:
            field_dict["source_application_id"] = source_application_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content", UNSET)

        expiry_in_secs = d.pop("expiry_in_secs", UNSET)

        follow_url = d.pop("follow_url", UNSET)

        source_application_id = d.pop("source_application_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        diagnosis_diagnostic_notification = cls(
            content=content,
            expiry_in_secs=expiry_in_secs,
            follow_url=follow_url,
            source_application_id=source_application_id,
            updated_at=updated_at,
        )

        diagnosis_diagnostic_notification.additional_properties = d
        return diagnosis_diagnostic_notification

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
