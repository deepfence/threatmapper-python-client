from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelScanReportFieldsResponse")


@_attrs_define
class ModelScanReportFieldsResponse:
    """
    Example:
        {'malware': ['malware', 'malware'], 'compliance': ['compliance', 'compliance'], 'secret': ['secret', 'secret'],
            'vulnerability': ['vulnerability', 'vulnerability']}

    Attributes:
        compliance (Union[Unset, None, List[str]]):
        malware (Union[Unset, None, List[str]]):
        secret (Union[Unset, None, List[str]]):
        vulnerability (Union[Unset, None, List[str]]):
    """

    compliance: Union[Unset, None, List[str]] = UNSET
    malware: Union[Unset, None, List[str]] = UNSET
    secret: Union[Unset, None, List[str]] = UNSET
    vulnerability: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compliance: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.compliance, Unset):
            if self.compliance is None:
                compliance = None
            else:
                compliance = self.compliance

        malware: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.malware, Unset):
            if self.malware is None:
                malware = None
            else:
                malware = self.malware

        secret: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.secret, Unset):
            if self.secret is None:
                secret = None
            else:
                secret = self.secret

        vulnerability: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.vulnerability, Unset):
            if self.vulnerability is None:
                vulnerability = None
            else:
                vulnerability = self.vulnerability

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compliance is not UNSET:
            field_dict["compliance"] = compliance
        if malware is not UNSET:
            field_dict["malware"] = malware
        if secret is not UNSET:
            field_dict["secret"] = secret
        if vulnerability is not UNSET:
            field_dict["vulnerability"] = vulnerability

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        compliance = cast(List[str], d.pop("compliance", UNSET))

        malware = cast(List[str], d.pop("malware", UNSET))

        secret = cast(List[str], d.pop("secret", UNSET))

        vulnerability = cast(List[str], d.pop("vulnerability", UNSET))

        model_scan_report_fields_response = cls(
            compliance=compliance,
            malware=malware,
            secret=secret,
            vulnerability=vulnerability,
        )

        model_scan_report_fields_response.additional_properties = d
        return model_scan_report_fields_response

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
