from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelCloudComplianceBenchmark")


@_attrs_define
class ModelCloudComplianceBenchmark:
    """
    Attributes:
        compliance_type (Union[Unset, str]):
        controls (Union[List[str], None, Unset]):
        id (Union[Unset, str]):
    """

    compliance_type: Union[Unset, str] = UNSET
    controls: Union[List[str], None, Unset] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compliance_type = self.compliance_type

        controls: Union[List[str], None, Unset]
        if isinstance(self.controls, Unset):
            controls = UNSET
        elif isinstance(self.controls, list):
            controls = self.controls

        else:
            controls = self.controls

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compliance_type is not UNSET:
            field_dict["compliance_type"] = compliance_type
        if controls is not UNSET:
            field_dict["controls"] = controls
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        compliance_type = d.pop("compliance_type", UNSET)

        def _parse_controls(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                controls_type_0 = cast(List[str], data)

                return controls_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        controls = _parse_controls(d.pop("controls", UNSET))

        id = d.pop("id", UNSET)

        model_cloud_compliance_benchmark = cls(
            compliance_type=compliance_type,
            controls=controls,
            id=id,
        )

        model_cloud_compliance_benchmark.additional_properties = d
        return model_cloud_compliance_benchmark

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
