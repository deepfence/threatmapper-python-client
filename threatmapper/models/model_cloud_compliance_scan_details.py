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
    Attributes:
        account_id (Union[Unset, str]):
        benchmarks (Union[List['ModelCloudComplianceBenchmark'], None, Unset]):
        scan_id (Union[Unset, str]):
        scan_types (Union[List[str], None, Unset]):
        stop_requested (Union[Unset, bool]):
    """

    account_id: Union[Unset, str] = UNSET
    benchmarks: Union[List["ModelCloudComplianceBenchmark"], None, Unset] = UNSET
    scan_id: Union[Unset, str] = UNSET
    scan_types: Union[List[str], None, Unset] = UNSET
    stop_requested: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id

        benchmarks: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.benchmarks, Unset):
            benchmarks = UNSET
        elif isinstance(self.benchmarks, list):
            benchmarks = []
            for benchmarks_type_0_item_data in self.benchmarks:
                benchmarks_type_0_item = benchmarks_type_0_item_data.to_dict()
                benchmarks.append(benchmarks_type_0_item)

        else:
            benchmarks = self.benchmarks

        scan_id = self.scan_id

        scan_types: Union[List[str], None, Unset]
        if isinstance(self.scan_types, Unset):
            scan_types = UNSET
        elif isinstance(self.scan_types, list):
            scan_types = self.scan_types

        else:
            scan_types = self.scan_types

        stop_requested = self.stop_requested

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
        if stop_requested is not UNSET:
            field_dict["stop_requested"] = stop_requested

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_cloud_compliance_benchmark import ModelCloudComplianceBenchmark

        d = src_dict.copy()
        account_id = d.pop("account_id", UNSET)

        def _parse_benchmarks(data: object) -> Union[List["ModelCloudComplianceBenchmark"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                benchmarks_type_0 = []
                _benchmarks_type_0 = data
                for benchmarks_type_0_item_data in _benchmarks_type_0:
                    benchmarks_type_0_item = ModelCloudComplianceBenchmark.from_dict(benchmarks_type_0_item_data)

                    benchmarks_type_0.append(benchmarks_type_0_item)

                return benchmarks_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelCloudComplianceBenchmark"], None, Unset], data)

        benchmarks = _parse_benchmarks(d.pop("benchmarks", UNSET))

        scan_id = d.pop("scan_id", UNSET)

        def _parse_scan_types(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scan_types_type_0 = cast(List[str], data)

                return scan_types_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        scan_types = _parse_scan_types(d.pop("scan_types", UNSET))

        stop_requested = d.pop("stop_requested", UNSET)

        model_cloud_compliance_scan_details = cls(
            account_id=account_id,
            benchmarks=benchmarks,
            scan_id=scan_id,
            scan_types=scan_types,
            stop_requested=stop_requested,
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
