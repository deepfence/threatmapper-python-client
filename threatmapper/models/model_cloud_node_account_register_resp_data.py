from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.controls_action import ControlsAction
    from ..models.model_cloud_node_account_register_resp_data_scans_type_0 import (
        ModelCloudNodeAccountRegisterRespDataScansType0,
    )
    from ..models.model_cloud_node_cloudtrail_trail import ModelCloudNodeCloudtrailTrail


T = TypeVar("T", bound="ModelCloudNodeAccountRegisterRespData")


@_attrs_define
class ModelCloudNodeAccountRegisterRespData:
    """
    Attributes:
        cloudtrail_trails (Union[List['ModelCloudNodeCloudtrailTrail'], None, Unset]):
        log_action (Union[Unset, ControlsAction]):
        refresh (Union[Unset, str]):
        scans (Union['ModelCloudNodeAccountRegisterRespDataScansType0', None, Unset]):
    """

    cloudtrail_trails: Union[List["ModelCloudNodeCloudtrailTrail"], None, Unset] = UNSET
    log_action: Union[Unset, "ControlsAction"] = UNSET
    refresh: Union[Unset, str] = UNSET
    scans: Union["ModelCloudNodeAccountRegisterRespDataScansType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.model_cloud_node_account_register_resp_data_scans_type_0 import (
            ModelCloudNodeAccountRegisterRespDataScansType0,
        )

        cloudtrail_trails: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.cloudtrail_trails, Unset):
            cloudtrail_trails = UNSET
        elif isinstance(self.cloudtrail_trails, list):
            cloudtrail_trails = []
            for cloudtrail_trails_type_0_item_data in self.cloudtrail_trails:
                cloudtrail_trails_type_0_item = cloudtrail_trails_type_0_item_data.to_dict()
                cloudtrail_trails.append(cloudtrail_trails_type_0_item)

        else:
            cloudtrail_trails = self.cloudtrail_trails

        log_action: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.log_action, Unset):
            log_action = self.log_action.to_dict()

        refresh = self.refresh

        scans: Union[Dict[str, Any], None, Unset]
        if isinstance(self.scans, Unset):
            scans = UNSET
        elif isinstance(self.scans, ModelCloudNodeAccountRegisterRespDataScansType0):
            scans = self.scans.to_dict()
        else:
            scans = self.scans

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
        from ..models.model_cloud_node_account_register_resp_data_scans_type_0 import (
            ModelCloudNodeAccountRegisterRespDataScansType0,
        )
        from ..models.model_cloud_node_cloudtrail_trail import ModelCloudNodeCloudtrailTrail

        d = src_dict.copy()

        def _parse_cloudtrail_trails(data: object) -> Union[List["ModelCloudNodeCloudtrailTrail"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cloudtrail_trails_type_0 = []
                _cloudtrail_trails_type_0 = data
                for cloudtrail_trails_type_0_item_data in _cloudtrail_trails_type_0:
                    cloudtrail_trails_type_0_item = ModelCloudNodeCloudtrailTrail.from_dict(
                        cloudtrail_trails_type_0_item_data
                    )

                    cloudtrail_trails_type_0.append(cloudtrail_trails_type_0_item)

                return cloudtrail_trails_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelCloudNodeCloudtrailTrail"], None, Unset], data)

        cloudtrail_trails = _parse_cloudtrail_trails(d.pop("cloudtrail_trails", UNSET))

        _log_action = d.pop("log_action", UNSET)
        log_action: Union[Unset, ControlsAction]
        if isinstance(_log_action, Unset):
            log_action = UNSET
        else:
            log_action = ControlsAction.from_dict(_log_action)

        refresh = d.pop("refresh", UNSET)

        def _parse_scans(data: object) -> Union["ModelCloudNodeAccountRegisterRespDataScansType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                scans_type_0 = ModelCloudNodeAccountRegisterRespDataScansType0.from_dict(data)

                return scans_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelCloudNodeAccountRegisterRespDataScansType0", None, Unset], data)

        scans = _parse_scans(d.pop("scans", UNSET))

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
