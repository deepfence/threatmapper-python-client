from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.utils_report_filters_node_type import UtilsReportFiltersNodeType
from ..models.utils_report_filters_scan_type import UtilsReportFiltersScanType
from ..models.utils_report_filters_severity_or_check_type import UtilsReportFiltersSeverityOrCheckType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.utils_advanced_report_filters import UtilsAdvancedReportFilters


T = TypeVar("T", bound="UtilsReportFilters")


@_attrs_define
class UtilsReportFilters:
    """
    Example:
        {'include_dead_nodes': True, 'node_type': 'host', 'most_exploitable_report': True, 'advanced_report_filters':
            {'image_name': ['image_name', 'image_name'], 'account_id': ['account_id', 'account_id'], 'container_name':
            ['container_name', 'container_name'], 'scan_status': ['scan_status', 'scan_status'], 'kubernetes_cluster_name':
            ['kubernetes_cluster_name', 'kubernetes_cluster_name'], 'masked': [True, True], 'host_name': ['host_name',
            'host_name'], 'pod_name': ['pod_name', 'pod_name']}, 'scan_type': 'vulnerability', 'scan_id': 'scan_id',
            'severity_or_check_type': ['severity_or_check_type', 'severity_or_check_type']}

    Attributes:
        node_type (UtilsReportFiltersNodeType):
        scan_type (UtilsReportFiltersScanType):
        advanced_report_filters (Union[Unset, UtilsAdvancedReportFilters]):  Example: {'image_name': ['image_name',
            'image_name'], 'account_id': ['account_id', 'account_id'], 'container_name': ['container_name',
            'container_name'], 'scan_status': ['scan_status', 'scan_status'], 'kubernetes_cluster_name':
            ['kubernetes_cluster_name', 'kubernetes_cluster_name'], 'masked': [True, True], 'host_name': ['host_name',
            'host_name'], 'pod_name': ['pod_name', 'pod_name']}.
        include_dead_nodes (Union[Unset, bool]):
        most_exploitable_report (Union[Unset, bool]):
        scan_id (Union[Unset, str]):
        severity_or_check_type (Union[Unset, None, UtilsReportFiltersSeverityOrCheckType]):
    """

    node_type: UtilsReportFiltersNodeType
    scan_type: UtilsReportFiltersScanType
    advanced_report_filters: Union[Unset, "UtilsAdvancedReportFilters"] = UNSET
    include_dead_nodes: Union[Unset, bool] = UNSET
    most_exploitable_report: Union[Unset, bool] = UNSET
    scan_id: Union[Unset, str] = UNSET
    severity_or_check_type: Union[Unset, None, UtilsReportFiltersSeverityOrCheckType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_type = self.node_type.value

        scan_type = self.scan_type.value

        advanced_report_filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.advanced_report_filters, Unset):
            advanced_report_filters = self.advanced_report_filters.to_dict()

        include_dead_nodes = self.include_dead_nodes
        most_exploitable_report = self.most_exploitable_report
        scan_id = self.scan_id
        severity_or_check_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.severity_or_check_type, Unset):
            severity_or_check_type = self.severity_or_check_type.value if self.severity_or_check_type else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_type": node_type,
                "scan_type": scan_type,
            }
        )
        if advanced_report_filters is not UNSET:
            field_dict["advanced_report_filters"] = advanced_report_filters
        if include_dead_nodes is not UNSET:
            field_dict["include_dead_nodes"] = include_dead_nodes
        if most_exploitable_report is not UNSET:
            field_dict["most_exploitable_report"] = most_exploitable_report
        if scan_id is not UNSET:
            field_dict["scan_id"] = scan_id
        if severity_or_check_type is not UNSET:
            field_dict["severity_or_check_type"] = severity_or_check_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.utils_advanced_report_filters import UtilsAdvancedReportFilters

        d = src_dict.copy()
        node_type = UtilsReportFiltersNodeType(d.pop("node_type"))

        scan_type = UtilsReportFiltersScanType(d.pop("scan_type"))

        _advanced_report_filters = d.pop("advanced_report_filters", UNSET)
        advanced_report_filters: Union[Unset, UtilsAdvancedReportFilters]
        if isinstance(_advanced_report_filters, Unset):
            advanced_report_filters = UNSET
        else:
            advanced_report_filters = UtilsAdvancedReportFilters.from_dict(_advanced_report_filters)

        include_dead_nodes = d.pop("include_dead_nodes", UNSET)

        most_exploitable_report = d.pop("most_exploitable_report", UNSET)

        scan_id = d.pop("scan_id", UNSET)

        _severity_or_check_type = d.pop("severity_or_check_type", UNSET)
        severity_or_check_type: Union[Unset, None, UtilsReportFiltersSeverityOrCheckType]
        if _severity_or_check_type is None:
            severity_or_check_type = None
        elif isinstance(_severity_or_check_type, Unset):
            severity_or_check_type = UNSET
        else:
            severity_or_check_type = UtilsReportFiltersSeverityOrCheckType(_severity_or_check_type)

        utils_report_filters = cls(
            node_type=node_type,
            scan_type=scan_type,
            advanced_report_filters=advanced_report_filters,
            include_dead_nodes=include_dead_nodes,
            most_exploitable_report=most_exploitable_report,
            scan_id=scan_id,
            severity_or_check_type=severity_or_check_type,
        )

        utils_report_filters.additional_properties = d
        return utils_report_filters

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
