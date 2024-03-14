from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reporters_contains_filter import ReportersContainsFilter


T = TypeVar("T", bound="ModelScanFilter")


@_attrs_define
class ModelScanFilter:
    """
    Attributes:
        cloud_account_scan_filter (ReportersContainsFilter):
        container_scan_filter (ReportersContainsFilter):
        host_scan_filter (ReportersContainsFilter):
        image_scan_filter (ReportersContainsFilter):
        kubernetes_cluster_scan_filter (ReportersContainsFilter):
    """

    cloud_account_scan_filter: "ReportersContainsFilter"
    container_scan_filter: "ReportersContainsFilter"
    host_scan_filter: "ReportersContainsFilter"
    image_scan_filter: "ReportersContainsFilter"
    kubernetes_cluster_scan_filter: "ReportersContainsFilter"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloud_account_scan_filter = self.cloud_account_scan_filter.to_dict()

        container_scan_filter = self.container_scan_filter.to_dict()

        host_scan_filter = self.host_scan_filter.to_dict()

        image_scan_filter = self.image_scan_filter.to_dict()

        kubernetes_cluster_scan_filter = self.kubernetes_cluster_scan_filter.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_account_scan_filter": cloud_account_scan_filter,
                "container_scan_filter": container_scan_filter,
                "host_scan_filter": host_scan_filter,
                "image_scan_filter": image_scan_filter,
                "kubernetes_cluster_scan_filter": kubernetes_cluster_scan_filter,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reporters_contains_filter import ReportersContainsFilter

        d = src_dict.copy()
        cloud_account_scan_filter = ReportersContainsFilter.from_dict(d.pop("cloud_account_scan_filter"))

        container_scan_filter = ReportersContainsFilter.from_dict(d.pop("container_scan_filter"))

        host_scan_filter = ReportersContainsFilter.from_dict(d.pop("host_scan_filter"))

        image_scan_filter = ReportersContainsFilter.from_dict(d.pop("image_scan_filter"))

        kubernetes_cluster_scan_filter = ReportersContainsFilter.from_dict(d.pop("kubernetes_cluster_scan_filter"))

        model_scan_filter = cls(
            cloud_account_scan_filter=cloud_account_scan_filter,
            container_scan_filter=container_scan_filter,
            host_scan_filter=host_scan_filter,
            image_scan_filter=image_scan_filter,
            kubernetes_cluster_scan_filter=kubernetes_cluster_scan_filter,
        )

        model_scan_filter.additional_properties = d
        return model_scan_filter

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
