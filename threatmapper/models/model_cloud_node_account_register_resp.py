from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cloud_node_account_register_resp_data import ModelCloudNodeAccountRegisterRespData


T = TypeVar("T", bound="ModelCloudNodeAccountRegisterResp")


@_attrs_define
class ModelCloudNodeAccountRegisterResp:
    """
    Example:
        {'data': {'cloudtrail_trails': [{'account_id': 'account_id', 'trail_name': 'trail_name'}, {'account_id':
            'account_id', 'trail_name': 'trail_name'}], 'scans': {'key': {'account_id': 'account_id', 'benchmarks':
            [{'controls': ['controls', 'controls'], 'compliance_type': 'compliance_type', 'id': 'id'}, {'controls':
            ['controls', 'controls'], 'compliance_type': 'compliance_type', 'id': 'id'}], 'scan_id': 'scan_id',
            'scan_types': ['scan_types', 'scan_types']}}, 'refresh': 'refresh'}}

    Attributes:
        data (Union[Unset, ModelCloudNodeAccountRegisterRespData]):  Example: {'cloudtrail_trails': [{'account_id':
            'account_id', 'trail_name': 'trail_name'}, {'account_id': 'account_id', 'trail_name': 'trail_name'}], 'scans':
            {'key': {'account_id': 'account_id', 'benchmarks': [{'controls': ['controls', 'controls'], 'compliance_type':
            'compliance_type', 'id': 'id'}, {'controls': ['controls', 'controls'], 'compliance_type': 'compliance_type',
            'id': 'id'}], 'scan_id': 'scan_id', 'scan_types': ['scan_types', 'scan_types']}}, 'refresh': 'refresh'}.
    """

    data: Union[Unset, "ModelCloudNodeAccountRegisterRespData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_cloud_node_account_register_resp_data import ModelCloudNodeAccountRegisterRespData

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, ModelCloudNodeAccountRegisterRespData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ModelCloudNodeAccountRegisterRespData.from_dict(_data)

        model_cloud_node_account_register_resp = cls(
            data=data,
        )

        model_cloud_node_account_register_resp.additional_properties = d
        return model_cloud_node_account_register_resp

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
