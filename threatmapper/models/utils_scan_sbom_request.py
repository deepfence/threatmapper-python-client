from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UtilsScanSbomRequest")


@_attrs_define
class UtilsScanSbomRequest:
    """
    Example:
        {'skip_scan': True, 'kubernetes_cluster_name': 'kubernetes_cluster_name', 'scan_type': 'scan_type',
            'sbom_file_path': 'sbom_file_path', 'registry_id': 'registry_id', 'mode': 'mode', 'image_name': 'image_name',
            'node_type': 'node_type', 'container_name': 'container_name', 'sbom': 'sbom', 'scan_id': 'scan_id', 'image_id':
            'image_id', 'host_name': 'host_name', 'node_id': 'node_id'}

    Attributes:
        sbom (str):
        scan_id (str):
        container_name (Union[Unset, str]):
        host_name (Union[Unset, str]):
        image_id (Union[Unset, str]):
        image_name (Union[Unset, str]):
        kubernetes_cluster_name (Union[Unset, str]):
        mode (Union[Unset, str]):
        node_id (Union[Unset, str]):
        node_type (Union[Unset, str]):
        registry_id (Union[Unset, str]):
        sbom_file_path (Union[Unset, str]):
        scan_type (Union[Unset, str]):
        skip_scan (Union[Unset, bool]):
    """

    sbom: str
    scan_id: str
    container_name: Union[Unset, str] = UNSET
    host_name: Union[Unset, str] = UNSET
    image_id: Union[Unset, str] = UNSET
    image_name: Union[Unset, str] = UNSET
    kubernetes_cluster_name: Union[Unset, str] = UNSET
    mode: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    node_type: Union[Unset, str] = UNSET
    registry_id: Union[Unset, str] = UNSET
    sbom_file_path: Union[Unset, str] = UNSET
    scan_type: Union[Unset, str] = UNSET
    skip_scan: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sbom = self.sbom
        scan_id = self.scan_id
        container_name = self.container_name
        host_name = self.host_name
        image_id = self.image_id
        image_name = self.image_name
        kubernetes_cluster_name = self.kubernetes_cluster_name
        mode = self.mode
        node_id = self.node_id
        node_type = self.node_type
        registry_id = self.registry_id
        sbom_file_path = self.sbom_file_path
        scan_type = self.scan_type
        skip_scan = self.skip_scan

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sbom": sbom,
                "scan_id": scan_id,
            }
        )
        if container_name is not UNSET:
            field_dict["container_name"] = container_name
        if host_name is not UNSET:
            field_dict["host_name"] = host_name
        if image_id is not UNSET:
            field_dict["image_id"] = image_id
        if image_name is not UNSET:
            field_dict["image_name"] = image_name
        if kubernetes_cluster_name is not UNSET:
            field_dict["kubernetes_cluster_name"] = kubernetes_cluster_name
        if mode is not UNSET:
            field_dict["mode"] = mode
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if node_type is not UNSET:
            field_dict["node_type"] = node_type
        if registry_id is not UNSET:
            field_dict["registry_id"] = registry_id
        if sbom_file_path is not UNSET:
            field_dict["sbom_file_path"] = sbom_file_path
        if scan_type is not UNSET:
            field_dict["scan_type"] = scan_type
        if skip_scan is not UNSET:
            field_dict["skip_scan"] = skip_scan

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sbom = d.pop("sbom")

        scan_id = d.pop("scan_id")

        container_name = d.pop("container_name", UNSET)

        host_name = d.pop("host_name", UNSET)

        image_id = d.pop("image_id", UNSET)

        image_name = d.pop("image_name", UNSET)

        kubernetes_cluster_name = d.pop("kubernetes_cluster_name", UNSET)

        mode = d.pop("mode", UNSET)

        node_id = d.pop("node_id", UNSET)

        node_type = d.pop("node_type", UNSET)

        registry_id = d.pop("registry_id", UNSET)

        sbom_file_path = d.pop("sbom_file_path", UNSET)

        scan_type = d.pop("scan_type", UNSET)

        skip_scan = d.pop("skip_scan", UNSET)

        utils_scan_sbom_request = cls(
            sbom=sbom,
            scan_id=scan_id,
            container_name=container_name,
            host_name=host_name,
            image_id=image_id,
            image_name=image_name,
            kubernetes_cluster_name=kubernetes_cluster_name,
            mode=mode,
            node_id=node_id,
            node_type=node_type,
            registry_id=registry_id,
            sbom_file_path=sbom_file_path,
            scan_type=scan_type,
            skip_scan=skip_scan,
        )

        utils_scan_sbom_request.additional_properties = d
        return utils_scan_sbom_request

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
