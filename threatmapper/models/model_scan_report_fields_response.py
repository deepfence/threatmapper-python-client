from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelScanReportFieldsResponse")


@_attrs_define
class ModelScanReportFieldsResponse:
    """
    Attributes:
        compliance (Union[List[str], None, Unset]):
        malware (Union[List[str], None, Unset]):
        secret (Union[List[str], None, Unset]):
        vulnerability (Union[List[str], None, Unset]):
    """

    compliance: Union[List[str], None, Unset] = UNSET
    malware: Union[List[str], None, Unset] = UNSET
    secret: Union[List[str], None, Unset] = UNSET
    vulnerability: Union[List[str], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compliance: Union[List[str], None, Unset]
        if isinstance(self.compliance, Unset):
            compliance = UNSET
        elif isinstance(self.compliance, list):
            compliance = self.compliance

        else:
            compliance = self.compliance

        malware: Union[List[str], None, Unset]
        if isinstance(self.malware, Unset):
            malware = UNSET
        elif isinstance(self.malware, list):
            malware = self.malware

        else:
            malware = self.malware

        secret: Union[List[str], None, Unset]
        if isinstance(self.secret, Unset):
            secret = UNSET
        elif isinstance(self.secret, list):
            secret = self.secret

        else:
            secret = self.secret

        vulnerability: Union[List[str], None, Unset]
        if isinstance(self.vulnerability, Unset):
            vulnerability = UNSET
        elif isinstance(self.vulnerability, list):
            vulnerability = self.vulnerability

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

        def _parse_compliance(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                compliance_type_0 = cast(List[str], data)

                return compliance_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        compliance = _parse_compliance(d.pop("compliance", UNSET))

        def _parse_malware(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                malware_type_0 = cast(List[str], data)

                return malware_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        malware = _parse_malware(d.pop("malware", UNSET))

        def _parse_secret(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                secret_type_0 = cast(List[str], data)

                return secret_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        secret = _parse_secret(d.pop("secret", UNSET))

        def _parse_vulnerability(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                vulnerability_type_0 = cast(List[str], data)

                return vulnerability_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        vulnerability = _parse_vulnerability(d.pop("vulnerability", UNSET))

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
