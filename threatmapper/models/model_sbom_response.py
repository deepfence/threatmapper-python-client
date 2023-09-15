from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelSbomResponse")


@_attrs_define
class ModelSbomResponse:
    """
    Example:
        {'severity': 'severity', 'licenses': ['licenses', 'licenses'], 'cve_id': 'cve_id', 'package_name':
            'package_name', 'locations': ['locations', 'locations'], 'version': 'version'}

    Attributes:
        cve_id (Union[Unset, str]):
        licenses (Union[Unset, List[str]]):
        locations (Union[Unset, List[str]]):
        package_name (Union[Unset, str]):
        severity (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    cve_id: Union[Unset, str] = UNSET
    licenses: Union[Unset, List[str]] = UNSET
    locations: Union[Unset, List[str]] = UNSET
    package_name: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cve_id = self.cve_id
        licenses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.licenses, Unset):
            licenses = self.licenses

        locations: Union[Unset, List[str]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = self.locations

        package_name = self.package_name
        severity = self.severity
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve_id is not UNSET:
            field_dict["cve_id"] = cve_id
        if licenses is not UNSET:
            field_dict["licenses"] = licenses
        if locations is not UNSET:
            field_dict["locations"] = locations
        if package_name is not UNSET:
            field_dict["package_name"] = package_name
        if severity is not UNSET:
            field_dict["severity"] = severity
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cve_id = d.pop("cve_id", UNSET)

        licenses = cast(List[str], d.pop("licenses", UNSET))

        locations = cast(List[str], d.pop("locations", UNSET))

        package_name = d.pop("package_name", UNSET)

        severity = d.pop("severity", UNSET)

        version = d.pop("version", UNSET)

        model_sbom_response = cls(
            cve_id=cve_id,
            licenses=licenses,
            locations=locations,
            package_name=package_name,
            severity=severity,
            version=version,
        )

        model_sbom_response.additional_properties = d
        return model_sbom_response

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
