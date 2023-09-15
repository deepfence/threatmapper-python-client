from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IngestersComplianceStats")


@_attrs_define
class IngestersComplianceStats:
    """
    Example:
        {'compliance_percentage': 6.027456183070403, 'alarm': 0, 'skip': 2, 'error': 1, 'ok': 5, 'info': 5}

    Attributes:
        alarm (Union[Unset, int]):
        compliance_percentage (Union[Unset, float]):
        error (Union[Unset, int]):
        info (Union[Unset, int]):
        ok (Union[Unset, int]):
        skip (Union[Unset, int]):
    """

    alarm: Union[Unset, int] = UNSET
    compliance_percentage: Union[Unset, float] = UNSET
    error: Union[Unset, int] = UNSET
    info: Union[Unset, int] = UNSET
    ok: Union[Unset, int] = UNSET
    skip: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alarm = self.alarm
        compliance_percentage = self.compliance_percentage
        error = self.error
        info = self.info
        ok = self.ok
        skip = self.skip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alarm is not UNSET:
            field_dict["alarm"] = alarm
        if compliance_percentage is not UNSET:
            field_dict["compliance_percentage"] = compliance_percentage
        if error is not UNSET:
            field_dict["error"] = error
        if info is not UNSET:
            field_dict["info"] = info
        if ok is not UNSET:
            field_dict["ok"] = ok
        if skip is not UNSET:
            field_dict["skip"] = skip

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alarm = d.pop("alarm", UNSET)

        compliance_percentage = d.pop("compliance_percentage", UNSET)

        error = d.pop("error", UNSET)

        info = d.pop("info", UNSET)

        ok = d.pop("ok", UNSET)

        skip = d.pop("skip", UNSET)

        ingesters_compliance_stats = cls(
            alarm=alarm,
            compliance_percentage=compliance_percentage,
            error=error,
            info=info,
            ok=ok,
            skip=skip,
        )

        ingesters_compliance_stats.additional_properties = d
        return ingesters_compliance_stats

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
