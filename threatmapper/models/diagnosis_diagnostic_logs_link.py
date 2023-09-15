from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagnosisDiagnosticLogsLink")


@_attrs_define
class DiagnosisDiagnosticLogsLink:
    """
    Example:
        {'url_link': 'url_link', 'created_at': 'created_at', 'label': 'label', 'message': 'message'}

    Attributes:
        created_at (Union[Unset, str]):
        label (Union[Unset, str]):
        message (Union[Unset, str]):
        url_link (Union[Unset, str]):
    """

    created_at: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    url_link: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at
        label = self.label
        message = self.message
        url_link = self.url_link

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if label is not UNSET:
            field_dict["label"] = label
        if message is not UNSET:
            field_dict["message"] = message
        if url_link is not UNSET:
            field_dict["url_link"] = url_link

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("created_at", UNSET)

        label = d.pop("label", UNSET)

        message = d.pop("message", UNSET)

        url_link = d.pop("url_link", UNSET)

        diagnosis_diagnostic_logs_link = cls(
            created_at=created_at,
            label=label,
            message=message,
            url_link=url_link,
        )

        diagnosis_diagnostic_logs_link.additional_properties = d
        return diagnosis_diagnostic_logs_link

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
