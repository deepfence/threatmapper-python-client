import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ingesters_compliance_stats import IngestersComplianceStats


T = TypeVar("T", bound="IngestersCloudComplianceScanStatus")


@_attrs_define
class IngestersCloudComplianceScanStatus:
    """
    Example:
        {'result': {'compliance_percentage': 6.027456183070403, 'alarm': 0, 'skip': 2, 'error': 1, 'ok': 5, 'info': 5},
            'scan_message': 'scan_message', '@timestamp': datetime.datetime(2000, 1, 23, 4, 56, 7,
            tzinfo=datetime.timezone.utc), 'total_checks': 7, 'scan_status': 'scan_status', 'scan_id': 'scan_id', 'type':
            'type', 'compliance_check_types': ['compliance_check_types', 'compliance_check_types']}

    Attributes:
        timestamp (Union[Unset, datetime.datetime]):
        compliance_check_types (Union[Unset, None, List[str]]):
        result (Union[Unset, IngestersComplianceStats]):  Example: {'compliance_percentage': 6.027456183070403, 'alarm':
            0, 'skip': 2, 'error': 1, 'ok': 5, 'info': 5}.
        scan_id (Union[Unset, str]):
        scan_message (Union[Unset, str]):
        scan_status (Union[Unset, str]):
        total_checks (Union[Unset, int]):
        type (Union[Unset, str]):
    """

    timestamp: Union[Unset, datetime.datetime] = UNSET
    compliance_check_types: Union[Unset, None, List[str]] = UNSET
    result: Union[Unset, "IngestersComplianceStats"] = UNSET
    scan_id: Union[Unset, str] = UNSET
    scan_message: Union[Unset, str] = UNSET
    scan_status: Union[Unset, str] = UNSET
    total_checks: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        compliance_check_types: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.compliance_check_types, Unset):
            if self.compliance_check_types is None:
                compliance_check_types = None
            else:
                compliance_check_types = self.compliance_check_types

        result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        scan_id = self.scan_id
        scan_message = self.scan_message
        scan_status = self.scan_status
        total_checks = self.total_checks
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["@timestamp"] = timestamp
        if compliance_check_types is not UNSET:
            field_dict["compliance_check_types"] = compliance_check_types
        if result is not UNSET:
            field_dict["result"] = result
        if scan_id is not UNSET:
            field_dict["scan_id"] = scan_id
        if scan_message is not UNSET:
            field_dict["scan_message"] = scan_message
        if scan_status is not UNSET:
            field_dict["scan_status"] = scan_status
        if total_checks is not UNSET:
            field_dict["total_checks"] = total_checks
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ingesters_compliance_stats import IngestersComplianceStats

        d = src_dict.copy()
        _timestamp = d.pop("@timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        compliance_check_types = cast(List[str], d.pop("compliance_check_types", UNSET))

        _result = d.pop("result", UNSET)
        result: Union[Unset, IngestersComplianceStats]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = IngestersComplianceStats.from_dict(_result)

        scan_id = d.pop("scan_id", UNSET)

        scan_message = d.pop("scan_message", UNSET)

        scan_status = d.pop("scan_status", UNSET)

        total_checks = d.pop("total_checks", UNSET)

        type = d.pop("type", UNSET)

        ingesters_cloud_compliance_scan_status = cls(
            timestamp=timestamp,
            compliance_check_types=compliance_check_types,
            result=result,
            scan_id=scan_id,
            scan_message=scan_message,
            scan_status=scan_status,
            total_checks=total_checks,
            type=type,
        )

        ingesters_cloud_compliance_scan_status.additional_properties = d
        return ingesters_cloud_compliance_scan_status

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
