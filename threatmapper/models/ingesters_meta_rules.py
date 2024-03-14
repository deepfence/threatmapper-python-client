from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IngestersMetaRules")


@_attrs_define
class IngestersMetaRules:
    """
    Attributes:
        author (Union[Unset, str]):
        date (Union[Unset, str]):
        description (Union[Unset, str]):
        file_severity (Union[Unset, str]):
        filetype (Union[Unset, str]):
        info (Union[Unset, str]):
        reference (Union[Unset, str]):
        rule_id (Union[Unset, str]):
        rule_name (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    author: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    file_severity: Union[Unset, str] = UNSET
    filetype: Union[Unset, str] = UNSET
    info: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    rule_id: Union[Unset, str] = UNSET
    rule_name: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        author = self.author

        date = self.date

        description = self.description

        file_severity = self.file_severity

        filetype = self.filetype

        info = self.info

        reference = self.reference

        rule_id = self.rule_id

        rule_name = self.rule_name

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if file_severity is not UNSET:
            field_dict["file_severity"] = file_severity
        if filetype is not UNSET:
            field_dict["filetype"] = filetype
        if info is not UNSET:
            field_dict["info"] = info
        if reference is not UNSET:
            field_dict["reference"] = reference
        if rule_id is not UNSET:
            field_dict["rule_id"] = rule_id
        if rule_name is not UNSET:
            field_dict["rule_name"] = rule_name
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        author = d.pop("author", UNSET)

        date = d.pop("date", UNSET)

        description = d.pop("description", UNSET)

        file_severity = d.pop("file_severity", UNSET)

        filetype = d.pop("filetype", UNSET)

        info = d.pop("info", UNSET)

        reference = d.pop("reference", UNSET)

        rule_id = d.pop("rule_id", UNSET)

        rule_name = d.pop("rule_name", UNSET)

        version = d.pop("version", UNSET)

        ingesters_meta_rules = cls(
            author=author,
            date=date,
            description=description,
            file_severity=file_severity,
            filetype=filetype,
            info=info,
            reference=reference,
            rule_id=rule_id,
            rule_name=rule_name,
            version=version,
        )

        ingesters_meta_rules.additional_properties = d
        return ingesters_meta_rules

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
