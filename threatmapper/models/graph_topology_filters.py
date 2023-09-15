from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reporters_fields_filters import ReportersFieldsFilters


T = TypeVar("T", bound="GraphTopologyFilters")


@_attrs_define
class GraphTopologyFilters:
    """
    Example:
        {'host_filter': ['host_filter', 'host_filter'], 'field_filters': {'compare_filter': [{'greater_than': True,
            'field_value': '', 'field_name': 'field_name'}, {'greater_than': True, 'field_value': '', 'field_name':
            'field_name'}], 'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter': {'order_fields':
            [{'size': 0, 'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name':
            'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in':
            {'key': ['', '']}}, 'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in':
            {'key': ['', '']}}}, 'container_filter': ['container_filter', 'container_filter'], 'cloud_filter':
            ['cloud_filter', 'cloud_filter'], 'kubernetes_filter': ['kubernetes_filter', 'kubernetes_filter'], 'pod_filter':
            ['pod_filter', 'pod_filter'], 'region_filter': ['region_filter', 'region_filter'], 'skip_connections': True}

    Attributes:
        field_filters (ReportersFieldsFilters):  Example: {'compare_filter': [{'greater_than': True, 'field_value': '',
            'field_name': 'field_name'}, {'greater_than': True, 'field_value': '', 'field_name': 'field_name'}],
            'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0,
            'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name': 'field_name'}]},
            'contains_filter': {'filter_in': {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in': {'key': ['',
            '']}}, 'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['',
            '']}}}.
        skip_connections (bool):
        cloud_filter (Optional[List[str]]):
        container_filter (Optional[List[str]]):
        host_filter (Optional[List[str]]):
        kubernetes_filter (Optional[List[str]]):
        pod_filter (Optional[List[str]]):
        region_filter (Optional[List[str]]):
    """

    field_filters: "ReportersFieldsFilters"
    skip_connections: bool
    cloud_filter: Optional[List[str]]
    container_filter: Optional[List[str]]
    host_filter: Optional[List[str]]
    kubernetes_filter: Optional[List[str]]
    pod_filter: Optional[List[str]]
    region_filter: Optional[List[str]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_filters = self.field_filters.to_dict()

        skip_connections = self.skip_connections
        if self.cloud_filter is None:
            cloud_filter = None
        else:
            cloud_filter = self.cloud_filter

        if self.container_filter is None:
            container_filter = None
        else:
            container_filter = self.container_filter

        if self.host_filter is None:
            host_filter = None
        else:
            host_filter = self.host_filter

        if self.kubernetes_filter is None:
            kubernetes_filter = None
        else:
            kubernetes_filter = self.kubernetes_filter

        if self.pod_filter is None:
            pod_filter = None
        else:
            pod_filter = self.pod_filter

        if self.region_filter is None:
            region_filter = None
        else:
            region_filter = self.region_filter

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_filters": field_filters,
                "skip_connections": skip_connections,
                "cloud_filter": cloud_filter,
                "container_filter": container_filter,
                "host_filter": host_filter,
                "kubernetes_filter": kubernetes_filter,
                "pod_filter": pod_filter,
                "region_filter": region_filter,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reporters_fields_filters import ReportersFieldsFilters

        d = src_dict.copy()
        field_filters = ReportersFieldsFilters.from_dict(d.pop("field_filters"))

        skip_connections = d.pop("skip_connections")

        cloud_filter = cast(List[str], d.pop("cloud_filter"))

        container_filter = cast(List[str], d.pop("container_filter"))

        host_filter = cast(List[str], d.pop("host_filter"))

        kubernetes_filter = cast(List[str], d.pop("kubernetes_filter"))

        pod_filter = cast(List[str], d.pop("pod_filter"))

        region_filter = cast(List[str], d.pop("region_filter"))

        graph_topology_filters = cls(
            field_filters=field_filters,
            skip_connections=skip_connections,
            cloud_filter=cloud_filter,
            container_filter=container_filter,
            host_filter=host_filter,
            kubernetes_filter=kubernetes_filter,
            pod_filter=pod_filter,
            region_filter=region_filter,
        )

        graph_topology_filters.additional_properties = d
        return graph_topology_filters

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
