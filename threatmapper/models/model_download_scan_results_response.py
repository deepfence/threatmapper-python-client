from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_scan_results_common import ModelScanResultsCommon


T = TypeVar("T", bound="ModelDownloadScanResultsResponse")


@_attrs_define
class ModelDownloadScanResultsResponse:
    """
    Example:
        {'scan_results': ['', ''], 'scan_info': {'cloud_account_id': 'cloud_account_id', 'node_type': 'node_type',
            'docker_container_name': 'docker_container_name', 'updated_at': 6, 'kubernetes_cluster_name':
            'kubernetes_cluster_name', 'node_name': 'node_name', 'created_at': 0, 'scan_id': 'scan_id', 'docker_image_name':
            'docker_image_name', 'host_name': 'host_name', 'node_id': 'node_id'}}

    Attributes:
        scan_info (Union[Unset, ModelScanResultsCommon]):  Example: {'cloud_account_id': 'cloud_account_id',
            'node_type': 'node_type', 'docker_container_name': 'docker_container_name', 'updated_at': 6,
            'kubernetes_cluster_name': 'kubernetes_cluster_name', 'node_name': 'node_name', 'created_at': 0, 'scan_id':
            'scan_id', 'docker_image_name': 'docker_image_name', 'host_name': 'host_name', 'node_id': 'node_id'}.
        scan_results (Union[Unset, None, List[Any]]):
    """

    scan_info: Union[Unset, "ModelScanResultsCommon"] = UNSET
    scan_results: Union[Unset, None, List[Any]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scan_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.scan_info, Unset):
            scan_info = self.scan_info.to_dict()

        scan_results: Union[Unset, None, List[Any]] = UNSET
        if not isinstance(self.scan_results, Unset):
            if self.scan_results is None:
                scan_results = None
            else:
                scan_results = self.scan_results

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scan_info is not UNSET:
            field_dict["scan_info"] = scan_info
        if scan_results is not UNSET:
            field_dict["scan_results"] = scan_results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_scan_results_common import ModelScanResultsCommon

        d = src_dict.copy()
        _scan_info = d.pop("scan_info", UNSET)
        scan_info: Union[Unset, ModelScanResultsCommon]
        if isinstance(_scan_info, Unset):
            scan_info = UNSET
        else:
            scan_info = ModelScanResultsCommon.from_dict(_scan_info)

        scan_results = cast(List[Any], d.pop("scan_results", UNSET))

        model_download_scan_results_response = cls(
            scan_info=scan_info,
            scan_results=scan_results,
        )

        model_download_scan_results_response.additional_properties = d
        return model_download_scan_results_response

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
