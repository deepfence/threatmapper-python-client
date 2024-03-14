from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UtilsAdvancedReportFilters")


@_attrs_define
class UtilsAdvancedReportFilters:
    """
    Attributes:
        container_name (Union[Unset, List[str]]):
        host_name (Union[Unset, List[str]]):
        image_name (Union[Unset, List[str]]):
        kubernetes_cluster_name (Union[Unset, List[str]]):
        masked (Union[Unset, List[bool]]):
        node_id (Union[Unset, List[str]]):
        pod_name (Union[Unset, List[str]]):
        scan_status (Union[Unset, List[str]]):
    """

    container_name: Union[Unset, List[str]] = UNSET
    host_name: Union[Unset, List[str]] = UNSET
    image_name: Union[Unset, List[str]] = UNSET
    kubernetes_cluster_name: Union[Unset, List[str]] = UNSET
    masked: Union[Unset, List[bool]] = UNSET
    node_id: Union[Unset, List[str]] = UNSET
    pod_name: Union[Unset, List[str]] = UNSET
    scan_status: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        container_name: Union[Unset, List[str]] = UNSET
        if not isinstance(self.container_name, Unset):
            container_name = self.container_name

        host_name: Union[Unset, List[str]] = UNSET
        if not isinstance(self.host_name, Unset):
            host_name = self.host_name

        image_name: Union[Unset, List[str]] = UNSET
        if not isinstance(self.image_name, Unset):
            image_name = self.image_name

        kubernetes_cluster_name: Union[Unset, List[str]] = UNSET
        if not isinstance(self.kubernetes_cluster_name, Unset):
            kubernetes_cluster_name = self.kubernetes_cluster_name

        masked: Union[Unset, List[bool]] = UNSET
        if not isinstance(self.masked, Unset):
            masked = self.masked

        node_id: Union[Unset, List[str]] = UNSET
        if not isinstance(self.node_id, Unset):
            node_id = self.node_id

        pod_name: Union[Unset, List[str]] = UNSET
        if not isinstance(self.pod_name, Unset):
            pod_name = self.pod_name

        scan_status: Union[Unset, List[str]] = UNSET
        if not isinstance(self.scan_status, Unset):
            scan_status = self.scan_status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if container_name is not UNSET:
            field_dict["container_name"] = container_name
        if host_name is not UNSET:
            field_dict["host_name"] = host_name
        if image_name is not UNSET:
            field_dict["image_name"] = image_name
        if kubernetes_cluster_name is not UNSET:
            field_dict["kubernetes_cluster_name"] = kubernetes_cluster_name
        if masked is not UNSET:
            field_dict["masked"] = masked
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if pod_name is not UNSET:
            field_dict["pod_name"] = pod_name
        if scan_status is not UNSET:
            field_dict["scan_status"] = scan_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        container_name = cast(List[str], d.pop("container_name", UNSET))

        host_name = cast(List[str], d.pop("host_name", UNSET))

        image_name = cast(List[str], d.pop("image_name", UNSET))

        kubernetes_cluster_name = cast(List[str], d.pop("kubernetes_cluster_name", UNSET))

        masked = cast(List[bool], d.pop("masked", UNSET))

        node_id = cast(List[str], d.pop("node_id", UNSET))

        pod_name = cast(List[str], d.pop("pod_name", UNSET))

        scan_status = cast(List[str], d.pop("scan_status", UNSET))

        utils_advanced_report_filters = cls(
            container_name=container_name,
            host_name=host_name,
            image_name=image_name,
            kubernetes_cluster_name=kubernetes_cluster_name,
            masked=masked,
            node_id=node_id,
            pod_name=pod_name,
            scan_status=scan_status,
        )

        utils_advanced_report_filters.additional_properties = d
        return utils_advanced_report_filters

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
