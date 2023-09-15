from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ingesters_secret_match import IngestersSecretMatch
    from ..models.ingesters_secret_rule import IngestersSecretRule
    from ..models.ingesters_secret_severity import IngestersSecretSeverity


T = TypeVar("T", bound="IngestersSecret")


@_attrs_define
class IngestersSecret:
    """
    Example:
        {'ImageLayerId': 'ImageLayerId', 'masked': True, 'Severity': {'score': 5.637376656633329, 'level': 'level'},
            'Rule': {'part': 'part', 'name': 'name', 'signature_to_match': 'signature_to_match', 'id': 5}, 'scan_id':
            'scan_id', 'Match': {'full_filename': 'full_filename', 'matched_content': 'matched_content',
            'relative_ending_index': 0, 'starting_index': 1, 'relative_starting_index': 6}}

    Attributes:
        image_layer_id (Union[Unset, str]):
        match (Union[Unset, IngestersSecretMatch]):  Example: {'full_filename': 'full_filename', 'matched_content':
            'matched_content', 'relative_ending_index': 0, 'starting_index': 1, 'relative_starting_index': 6}.
        rule (Union[Unset, IngestersSecretRule]):  Example: {'part': 'part', 'name': 'name', 'signature_to_match':
            'signature_to_match', 'id': 5}.
        severity (Union[Unset, IngestersSecretSeverity]):  Example: {'score': 5.637376656633329, 'level': 'level'}.
        masked (Union[Unset, bool]):
        scan_id (Union[Unset, str]):
    """

    image_layer_id: Union[Unset, str] = UNSET
    match: Union[Unset, "IngestersSecretMatch"] = UNSET
    rule: Union[Unset, "IngestersSecretRule"] = UNSET
    severity: Union[Unset, "IngestersSecretSeverity"] = UNSET
    masked: Union[Unset, bool] = UNSET
    scan_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image_layer_id = self.image_layer_id
        match: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.match, Unset):
            match = self.match.to_dict()

        rule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rule, Unset):
            rule = self.rule.to_dict()

        severity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.to_dict()

        masked = self.masked
        scan_id = self.scan_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_layer_id is not UNSET:
            field_dict["ImageLayerId"] = image_layer_id
        if match is not UNSET:
            field_dict["Match"] = match
        if rule is not UNSET:
            field_dict["Rule"] = rule
        if severity is not UNSET:
            field_dict["Severity"] = severity
        if masked is not UNSET:
            field_dict["masked"] = masked
        if scan_id is not UNSET:
            field_dict["scan_id"] = scan_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ingesters_secret_match import IngestersSecretMatch
        from ..models.ingesters_secret_rule import IngestersSecretRule
        from ..models.ingesters_secret_severity import IngestersSecretSeverity

        d = src_dict.copy()
        image_layer_id = d.pop("ImageLayerId", UNSET)

        _match = d.pop("Match", UNSET)
        match: Union[Unset, IngestersSecretMatch]
        if isinstance(_match, Unset):
            match = UNSET
        else:
            match = IngestersSecretMatch.from_dict(_match)

        _rule = d.pop("Rule", UNSET)
        rule: Union[Unset, IngestersSecretRule]
        if isinstance(_rule, Unset):
            rule = UNSET
        else:
            rule = IngestersSecretRule.from_dict(_rule)

        _severity = d.pop("Severity", UNSET)
        severity: Union[Unset, IngestersSecretSeverity]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = IngestersSecretSeverity.from_dict(_severity)

        masked = d.pop("masked", UNSET)

        scan_id = d.pop("scan_id", UNSET)

        ingesters_secret = cls(
            image_layer_id=image_layer_id,
            match=match,
            rule=rule,
            severity=severity,
            masked=masked,
            scan_id=scan_id,
        )

        ingesters_secret.additional_properties = d
        return ingesters_secret

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
