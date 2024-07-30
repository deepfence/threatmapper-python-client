from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_compliance_scan_result_control_group_counts import ModelComplianceScanResultControlGroupCounts


T = TypeVar("T", bound="ModelComplianceScanResultControlGroup")


@_attrs_define
class ModelComplianceScanResultControlGroup:
    """
    Example:
        {'benchmark_types': ['benchmark_types', 'benchmark_types'], 'counts': {'key': 0}, 'problem_title':
            'problem_title'}

    Attributes:
        benchmark_types (Union[Unset, List[str]]):
        counts (Union[Unset, ModelComplianceScanResultControlGroupCounts]):
        problem_title (Union[Unset, str]):
    """

    benchmark_types: Union[Unset, List[str]] = UNSET
    counts: Union[Unset, "ModelComplianceScanResultControlGroupCounts"] = UNSET
    problem_title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        benchmark_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.benchmark_types, Unset):
            benchmark_types = self.benchmark_types

        counts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()

        problem_title = self.problem_title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if benchmark_types is not UNSET:
            field_dict["benchmark_types"] = benchmark_types
        if counts is not UNSET:
            field_dict["counts"] = counts
        if problem_title is not UNSET:
            field_dict["problem_title"] = problem_title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_compliance_scan_result_control_group_counts import (
            ModelComplianceScanResultControlGroupCounts,
        )

        d = src_dict.copy()
        benchmark_types = cast(List[str], d.pop("benchmark_types", UNSET))

        _counts = d.pop("counts", UNSET)
        counts: Union[Unset, ModelComplianceScanResultControlGroupCounts]
        if isinstance(_counts, Unset):
            counts = UNSET
        else:
            counts = ModelComplianceScanResultControlGroupCounts.from_dict(_counts)

        problem_title = d.pop("problem_title", UNSET)

        model_compliance_scan_result_control_group = cls(
            benchmark_types=benchmark_types,
            counts=counts,
            problem_title=problem_title,
        )

        model_compliance_scan_result_control_group.additional_properties = d
        return model_compliance_scan_result_control_group

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
