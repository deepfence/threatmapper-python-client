from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_cloud_node_account_register_req_cloud_provider import ModelCloudNodeAccountRegisterReqCloudProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cloud_node_account_register_req_monitored_account_ids import (
        ModelCloudNodeAccountRegisterReqMonitoredAccountIds,
    )


T = TypeVar("T", bound="ModelCloudNodeAccountRegisterReq")


@_attrs_define
class ModelCloudNodeAccountRegisterReq:
    """
    Example:
        {'cloud_account': 'cloud_account', 'monitored_account_ids': {'key': 'monitored_account_ids'}, 'org_acc_id':
            'org_acc_id', 'cloud_provider': 'aws', 'version': 'version', 'node_id': 'node_id'}

    Attributes:
        cloud_account (str):
        cloud_provider (ModelCloudNodeAccountRegisterReqCloudProvider):
        node_id (str):
        monitored_account_ids (Union[Unset, None, ModelCloudNodeAccountRegisterReqMonitoredAccountIds]):
        org_acc_id (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    cloud_account: str
    cloud_provider: ModelCloudNodeAccountRegisterReqCloudProvider
    node_id: str
    monitored_account_ids: Union[Unset, None, "ModelCloudNodeAccountRegisterReqMonitoredAccountIds"] = UNSET
    org_acc_id: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloud_account = self.cloud_account
        cloud_provider = self.cloud_provider.value

        node_id = self.node_id
        monitored_account_ids: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.monitored_account_ids, Unset):
            monitored_account_ids = self.monitored_account_ids.to_dict() if self.monitored_account_ids else None

        org_acc_id = self.org_acc_id
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_account": cloud_account,
                "cloud_provider": cloud_provider,
                "node_id": node_id,
            }
        )
        if monitored_account_ids is not UNSET:
            field_dict["monitored_account_ids"] = monitored_account_ids
        if org_acc_id is not UNSET:
            field_dict["org_acc_id"] = org_acc_id
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_cloud_node_account_register_req_monitored_account_ids import (
            ModelCloudNodeAccountRegisterReqMonitoredAccountIds,
        )

        d = src_dict.copy()
        cloud_account = d.pop("cloud_account")

        cloud_provider = ModelCloudNodeAccountRegisterReqCloudProvider(d.pop("cloud_provider"))

        node_id = d.pop("node_id")

        _monitored_account_ids = d.pop("monitored_account_ids", UNSET)
        monitored_account_ids: Union[Unset, None, ModelCloudNodeAccountRegisterReqMonitoredAccountIds]
        if _monitored_account_ids is None:
            monitored_account_ids = None
        elif isinstance(_monitored_account_ids, Unset):
            monitored_account_ids = UNSET
        else:
            monitored_account_ids = ModelCloudNodeAccountRegisterReqMonitoredAccountIds.from_dict(
                _monitored_account_ids
            )

        org_acc_id = d.pop("org_acc_id", UNSET)

        version = d.pop("version", UNSET)

        model_cloud_node_account_register_req = cls(
            cloud_account=cloud_account,
            cloud_provider=cloud_provider,
            node_id=node_id,
            monitored_account_ids=monitored_account_ids,
            org_acc_id=org_acc_id,
            version=version,
        )

        model_cloud_node_account_register_req.additional_properties = d
        return model_cloud_node_account_register_req

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
