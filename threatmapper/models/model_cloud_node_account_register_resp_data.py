from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.controls_action import ControlsAction
    from ..models.model_cloud_node_account_register_resp_data_scans import ModelCloudNodeAccountRegisterRespDataScans
    from ..models.model_cloud_node_cloudtrail_trail import ModelCloudNodeCloudtrailTrail


T = TypeVar("T", bound="ModelCloudNodeAccountRegisterRespData")


@_attrs_define
class ModelCloudNodeAccountRegisterRespData:
    """
    Example:
        {'cloudtrail_trails': [{'account_id': 'account_id', 'trail_name': 'trail_name'}, {'account_id': 'account_id',
            'trail_name': 'trail_name'}], 'log_action': {'id': 0, 'request_payload': 'request_payload'}, 'scans': {'key':
            {'account_id': 'account_id', 'stop_requested': True, 'benchmarks': [{'controls': ['controls', 'controls'],
            'compliance_type': 'compliance_type', 'id': 'id'}, {'controls': ['controls', 'controls'], 'compliance_type':
            'compliance_type', 'id': 'id'}], 'scan_id': 'scan_id', 'scan_types': ['scan_types', 'scan_types']}}, 'refresh':
            'refresh'}

    Attributes:
        cloudtrail_trails (Union[Unset, None, List['ModelCloudNodeCloudtrailTrail']]):
        log_action (Union[Unset, ControlsAction]):  Example: {'id': 0, 'request_payload': 'request_payload'}.
        refresh (Union[Unset, str]):
        scans (Union[Unset, None, ModelCloudNodeAccountRegisterRespDataScans]):
    """

    cloudtrail_trails: Union[Unset, None, List["ModelCloudNodeCloudtrailTrail"]] = UNSET
    log_action: Union[Unset, "ControlsAction"] = UNSET
    refresh: Union[Unset, str] = UNSET
    scans: Union[Unset, None, "ModelCloudNodeAccountRegisterRespDataScans"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloudtrail_trails: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cloudtrail_trails, Unset):
            if self.cloudtrail_trails is None:
                cloudtrail_trails = None
            else:
                cloudtrail_trails = []
                for cloudtrail_trails_item_data in self.cloudtrail_trails:
                    cloudtrail_trails_item = cloudtrail_trails_item_data.to_dict()

                    cloudtrail_trails.append(cloudtrail_trails_item)

        log_action: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.log_action, Unset):
            log_action = self.log_action.to_dict()

        refresh = self.refresh
        scans: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.scans, Unset):
            scans = self.scans.to_dict() if self.scans else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloudtrail_trails is not UNSET:
            field_dict["cloudtrail_trails"] = cloudtrail_trails
        if log_action is not UNSET:
            field_dict["log_action"] = log_action
        if refresh is not UNSET:
            field_dict["refresh"] = refresh
        if scans is not UNSET:
            field_dict["scans"] = scans

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controls_action import ControlsAction
        from ..models.model_cloud_node_account_register_resp_data_scans import (
            ModelCloudNodeAccountRegisterRespDataScans,
        )
        from ..models.model_cloud_node_cloudtrail_trail import ModelCloudNodeCloudtrailTrail

        d = src_dict.copy()
        cloudtrail_trails = []
        _cloudtrail_trails = d.pop("cloudtrail_trails", UNSET)
        for cloudtrail_trails_item_data in _cloudtrail_trails or []:
            cloudtrail_trails_item = ModelCloudNodeCloudtrailTrail.from_dict(cloudtrail_trails_item_data)

            cloudtrail_trails.append(cloudtrail_trails_item)

        _log_action = d.pop("log_action", UNSET)
        log_action: Union[Unset, ControlsAction]
        if isinstance(_log_action, Unset):
            log_action = UNSET
        else:
            log_action = ControlsAction.from_dict(_log_action)

        refresh = d.pop("refresh", UNSET)

        _scans = d.pop("scans", UNSET)
        scans: Union[Unset, None, ModelCloudNodeAccountRegisterRespDataScans]
        if _scans is None:
            scans = None
        elif isinstance(_scans, Unset):
            scans = UNSET
        else:
            scans = ModelCloudNodeAccountRegisterRespDataScans.from_dict(_scans)

        model_cloud_node_account_register_resp_data = cls(
            cloudtrail_trails=cloudtrail_trails,
            log_action=log_action,
            refresh=refresh,
            scans=scans,
        )

        model_cloud_node_account_register_resp_data.additional_properties = d
        return model_cloud_node_account_register_resp_data

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
