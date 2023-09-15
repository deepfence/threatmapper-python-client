from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_generate_report_req_duration import ModelGenerateReportReqDuration
from ..models.model_generate_report_req_report_type import ModelGenerateReportReqReportType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.utils_report_filters import UtilsReportFilters


T = TypeVar("T", bound="ModelGenerateReportReq")


@_attrs_define
class ModelGenerateReportReq:
    """
    Example:
        {'duration': 0, 'filters': {'include_dead_nodes': True, 'node_type': 'host', 'advanced_report_filters':
            {'image_name': ['image_name', 'image_name'], 'account_id': ['account_id', 'account_id'], 'container_name':
            ['container_name', 'container_name'], 'scan_status': ['scan_status', 'scan_status'], 'kubernetes_cluster_name':
            ['kubernetes_cluster_name', 'kubernetes_cluster_name'], 'masked': [True, True], 'host_name': ['host_name',
            'host_name'], 'pod_name': ['pod_name', 'pod_name']}, 'scan_type': 'vulnerability', 'scan_id': 'scan_id',
            'severity_or_check_type': ['severity_or_check_type', 'severity_or_check_type']}, 'report_type': 'pdf'}

    Attributes:
        report_type (ModelGenerateReportReqReportType):
        duration (Union[Unset, ModelGenerateReportReqDuration]):
        filters (Union[Unset, UtilsReportFilters]):  Example: {'include_dead_nodes': True, 'node_type': 'host',
            'advanced_report_filters': {'image_name': ['image_name', 'image_name'], 'account_id': ['account_id',
            'account_id'], 'container_name': ['container_name', 'container_name'], 'scan_status': ['scan_status',
            'scan_status'], 'kubernetes_cluster_name': ['kubernetes_cluster_name', 'kubernetes_cluster_name'], 'masked':
            [True, True], 'host_name': ['host_name', 'host_name'], 'pod_name': ['pod_name', 'pod_name']}, 'scan_type':
            'vulnerability', 'scan_id': 'scan_id', 'severity_or_check_type': ['severity_or_check_type',
            'severity_or_check_type']}.
    """

    report_type: ModelGenerateReportReqReportType
    duration: Union[Unset, ModelGenerateReportReqDuration] = UNSET
    filters: Union[Unset, "UtilsReportFilters"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        report_type = self.report_type.value

        duration: Union[Unset, int] = UNSET
        if not isinstance(self.duration, Unset):
            duration = self.duration.value

        filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "report_type": report_type,
            }
        )
        if duration is not UNSET:
            field_dict["duration"] = duration
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.utils_report_filters import UtilsReportFilters

        d = src_dict.copy()
        report_type = ModelGenerateReportReqReportType(d.pop("report_type"))

        _duration = d.pop("duration", UNSET)
        duration: Union[Unset, ModelGenerateReportReqDuration]
        if isinstance(_duration, Unset):
            duration = UNSET
        else:
            duration = ModelGenerateReportReqDuration(_duration)

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, UtilsReportFilters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = UtilsReportFilters.from_dict(_filters)

        model_generate_report_req = cls(
            report_type=report_type,
            duration=duration,
            filters=filters,
        )

        model_generate_report_req.additional_properties = d
        return model_generate_report_req

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
