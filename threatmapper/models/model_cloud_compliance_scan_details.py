from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cloud_compliance_benchmark import ModelCloudComplianceBenchmark


T = TypeVar("T", bound="ModelCloudComplianceScanDetails")


@_attrs_define
class ModelCloudComplianceScanDetails:
    """
    Example:
        {'account_id': 'account_id', 'benchmarks': [{'controls': ['controls', 'controls'], 'compliance_type':
            'compliance_type', 'id': 'id'}, {'controls': ['controls', 'controls'], 'compliance_type': 'compliance_type',
            'id': 'id'}], 'scan_id': 'scan_id', 'scan_types': ['scan_types', 'scan_types']}

    Attributes:
        account_id (Union[Unset, str]):
        benchmarks (Union[Unset, None, List['ModelCloudComplianceBenchmark']]):
        scan_id (Union[Unset, str]):
        scan_types (Union[Unset, None, List[str]]):
    """

    account_id: Union[Unset, str] = UNSET
    benchmarks: Union[Unset, None, List["ModelCloudComplianceBenchmark"]] = UNSET
    scan_id: Union[Unset, str] = UNSET
    scan_types: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        benchmarks: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.benchmarks, Unset):
            if self.benchmarks is None:
                benchmarks = None
            else:
                benchmarks = []
                for benchmarks_item_data in self.benchmarks:
                    benchmarks_item = benchmarks_item_data.to_dict()

                    benchmarks.append(benchmarks_item)

        scan_id = self.scan_id
        scan_types: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.scan_types, Unset):
            if self.scan_types is None:
                scan_types = None
            else:
                scan_types = self.scan_types

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if benchmarks is not UNSET:
            field_dict["benchmarks"] = benchmarks
        if scan_id is not UNSET:
            field_dict["scan_id"] = scan_id
        if scan_types is not UNSET:
            field_dict["scan_types"] = scan_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_cloud_compliance_benchmark import ModelCloudComplianceBenchmark

        d = src_dict.copy()
        account_id = d.pop("account_id", UNSET)

        benchmarks = []
        _benchmarks = d.pop("benchmarks", UNSET)
        for benchmarks_item_data in _benchmarks or []:
            benchmarks_item = ModelCloudComplianceBenchmark.from_dict(benchmarks_item_data)

            benchmarks.append(benchmarks_item)

        scan_id = d.pop("scan_id", UNSET)

        scan_types = cast(List[str], d.pop("scan_types", UNSET))

        model_cloud_compliance_scan_details = cls(
            account_id=account_id,
            benchmarks=benchmarks,
            scan_id=scan_id,
            scan_types=scan_types,
        )

        model_cloud_compliance_scan_details.additional_properties = d
        return model_cloud_compliance_scan_details

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
