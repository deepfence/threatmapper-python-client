from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_add_scheduled_task_request_action import ModelAddScheduledTaskRequestAction
from ..models.model_benchmark_type import ModelBenchmarkType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_node_identifier import ModelNodeIdentifier
    from ..models.model_scan_filter import ModelScanFilter
    from ..models.model_vulnerability_scan_config_language import ModelVulnerabilityScanConfigLanguage


T = TypeVar("T", bound="ModelAddScheduledTaskRequest")


@_attrs_define
class ModelAddScheduledTaskRequest:
    """
    Attributes:
        action (ModelAddScheduledTaskRequestAction):
        benchmark_types (Union[List[ModelBenchmarkType], None]):
        filters (ModelScanFilter):
        node_ids (Union[List['ModelNodeIdentifier'], None]):
        scan_config (Union[List['ModelVulnerabilityScanConfigLanguage'], None]):
        cron_expr (Union[Unset, str]):
        deepfence_system_scan (Union[Unset, bool]):
        description (Union[Unset, str]):
        is_priority (Union[Unset, bool]):
    """

    action: ModelAddScheduledTaskRequestAction
    benchmark_types: Union[List[ModelBenchmarkType], None]
    filters: "ModelScanFilter"
    node_ids: Union[List["ModelNodeIdentifier"], None]
    scan_config: Union[List["ModelVulnerabilityScanConfigLanguage"], None]
    cron_expr: Union[Unset, str] = UNSET
    deepfence_system_scan: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    is_priority: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action.value

        benchmark_types: Union[List[str], None]
        if isinstance(self.benchmark_types, list):
            benchmark_types = []
            for benchmark_types_type_0_item_data in self.benchmark_types:
                benchmark_types_type_0_item = benchmark_types_type_0_item_data.value
                benchmark_types.append(benchmark_types_type_0_item)

        else:
            benchmark_types = self.benchmark_types

        filters = self.filters.to_dict()

        node_ids: Union[List[Dict[str, Any]], None]
        if isinstance(self.node_ids, list):
            node_ids = []
            for node_ids_type_0_item_data in self.node_ids:
                node_ids_type_0_item = node_ids_type_0_item_data.to_dict()
                node_ids.append(node_ids_type_0_item)

        else:
            node_ids = self.node_ids

        scan_config: Union[List[Dict[str, Any]], None]
        if isinstance(self.scan_config, list):
            scan_config = []
            for scan_config_type_0_item_data in self.scan_config:
                scan_config_type_0_item = scan_config_type_0_item_data.to_dict()
                scan_config.append(scan_config_type_0_item)

        else:
            scan_config = self.scan_config

        cron_expr = self.cron_expr

        deepfence_system_scan = self.deepfence_system_scan

        description = self.description

        is_priority = self.is_priority

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "benchmark_types": benchmark_types,
                "filters": filters,
                "node_ids": node_ids,
                "scan_config": scan_config,
            }
        )
        if cron_expr is not UNSET:
            field_dict["cron_expr"] = cron_expr
        if deepfence_system_scan is not UNSET:
            field_dict["deepfence_system_scan"] = deepfence_system_scan
        if description is not UNSET:
            field_dict["description"] = description
        if is_priority is not UNSET:
            field_dict["is_priority"] = is_priority

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_node_identifier import ModelNodeIdentifier
        from ..models.model_scan_filter import ModelScanFilter
        from ..models.model_vulnerability_scan_config_language import ModelVulnerabilityScanConfigLanguage

        d = src_dict.copy()
        action = ModelAddScheduledTaskRequestAction(d.pop("action"))

        def _parse_benchmark_types(data: object) -> Union[List[ModelBenchmarkType], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                benchmark_types_type_0 = []
                _benchmark_types_type_0 = data
                for benchmark_types_type_0_item_data in _benchmark_types_type_0:
                    benchmark_types_type_0_item = ModelBenchmarkType(benchmark_types_type_0_item_data)

                    benchmark_types_type_0.append(benchmark_types_type_0_item)

                return benchmark_types_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[ModelBenchmarkType], None], data)

        benchmark_types = _parse_benchmark_types(d.pop("benchmark_types"))

        filters = ModelScanFilter.from_dict(d.pop("filters"))

        def _parse_node_ids(data: object) -> Union[List["ModelNodeIdentifier"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                node_ids_type_0 = []
                _node_ids_type_0 = data
                for node_ids_type_0_item_data in _node_ids_type_0:
                    node_ids_type_0_item = ModelNodeIdentifier.from_dict(node_ids_type_0_item_data)

                    node_ids_type_0.append(node_ids_type_0_item)

                return node_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelNodeIdentifier"], None], data)

        node_ids = _parse_node_ids(d.pop("node_ids"))

        def _parse_scan_config(data: object) -> Union[List["ModelVulnerabilityScanConfigLanguage"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scan_config_type_0 = []
                _scan_config_type_0 = data
                for scan_config_type_0_item_data in _scan_config_type_0:
                    scan_config_type_0_item = ModelVulnerabilityScanConfigLanguage.from_dict(
                        scan_config_type_0_item_data
                    )

                    scan_config_type_0.append(scan_config_type_0_item)

                return scan_config_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelVulnerabilityScanConfigLanguage"], None], data)

        scan_config = _parse_scan_config(d.pop("scan_config"))

        cron_expr = d.pop("cron_expr", UNSET)

        deepfence_system_scan = d.pop("deepfence_system_scan", UNSET)

        description = d.pop("description", UNSET)

        is_priority = d.pop("is_priority", UNSET)

        model_add_scheduled_task_request = cls(
            action=action,
            benchmark_types=benchmark_types,
            filters=filters,
            node_ids=node_ids,
            scan_config=scan_config,
            cron_expr=cron_expr,
            deepfence_system_scan=deepfence_system_scan,
            description=description,
            is_priority=is_priority,
        )

        model_add_scheduled_task_request.additional_properties = d
        return model_add_scheduled_task_request

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
