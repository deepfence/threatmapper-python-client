from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_node_identifier import ModelNodeIdentifier
    from ..models.model_scan_filter import ModelScanFilter


T = TypeVar("T", bound="ModelComplianceScanTriggerReq")


@_attrs_define
class ModelComplianceScanTriggerReq:
    """
    Attributes:
        benchmark_types (Union[List[str], None]):
        filters (ModelScanFilter):
        node_ids (Union[List['ModelNodeIdentifier'], None]):
        is_priority (Union[Unset, bool]):
    """

    benchmark_types: Union[List[str], None]
    filters: "ModelScanFilter"
    node_ids: Union[List["ModelNodeIdentifier"], None]
    is_priority: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        benchmark_types: Union[List[str], None]
        if isinstance(self.benchmark_types, list):
            benchmark_types = self.benchmark_types

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

        is_priority = self.is_priority

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "benchmark_types": benchmark_types,
                "filters": filters,
                "node_ids": node_ids,
            }
        )
        if is_priority is not UNSET:
            field_dict["is_priority"] = is_priority

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_node_identifier import ModelNodeIdentifier
        from ..models.model_scan_filter import ModelScanFilter

        d = src_dict.copy()

        def _parse_benchmark_types(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                benchmark_types_type_0 = cast(List[str], data)

                return benchmark_types_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

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

        is_priority = d.pop("is_priority", UNSET)

        model_compliance_scan_trigger_req = cls(
            benchmark_types=benchmark_types,
            filters=filters,
            node_ids=node_ids,
            is_priority=is_priority,
        )

        model_compliance_scan_trigger_req.additional_properties = d
        return model_compliance_scan_trigger_req

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
