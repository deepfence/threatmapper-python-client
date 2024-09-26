from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_cloud_node_account_register_req_cloud_provider import ModelCloudNodeAccountRegisterReqCloudProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cloud_node_monitored_account import ModelCloudNodeMonitoredAccount


T = TypeVar("T", bound="ModelCloudNodeAccountRegisterReq")


@_attrs_define
class ModelCloudNodeAccountRegisterReq:
    """
    Attributes:
        account_id (str):
        cloud_provider (ModelCloudNodeAccountRegisterReqCloudProvider):
        host_node_id (str):
        node_id (str):
        version (str):
        account_name (Union[Unset, str]):
        is_organization_deployment (Union[Unset, bool]):
        monitored_accounts (Union[List['ModelCloudNodeMonitoredAccount'], None, Unset]):
        organization_account_id (Union[Unset, str]):
    """

    account_id: str
    cloud_provider: ModelCloudNodeAccountRegisterReqCloudProvider
    host_node_id: str
    node_id: str
    version: str
    account_name: Union[Unset, str] = UNSET
    is_organization_deployment: Union[Unset, bool] = UNSET
    monitored_accounts: Union[List["ModelCloudNodeMonitoredAccount"], None, Unset] = UNSET
    organization_account_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id

        cloud_provider = self.cloud_provider.value

        host_node_id = self.host_node_id

        node_id = self.node_id

        version = self.version

        account_name = self.account_name

        is_organization_deployment = self.is_organization_deployment

        monitored_accounts: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.monitored_accounts, Unset):
            monitored_accounts = UNSET
        elif isinstance(self.monitored_accounts, list):
            monitored_accounts = []
            for monitored_accounts_type_0_item_data in self.monitored_accounts:
                monitored_accounts_type_0_item = monitored_accounts_type_0_item_data.to_dict()
                monitored_accounts.append(monitored_accounts_type_0_item)

        else:
            monitored_accounts = self.monitored_accounts

        organization_account_id = self.organization_account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "cloud_provider": cloud_provider,
                "host_node_id": host_node_id,
                "node_id": node_id,
                "version": version,
            }
        )
        if account_name is not UNSET:
            field_dict["account_name"] = account_name
        if is_organization_deployment is not UNSET:
            field_dict["is_organization_deployment"] = is_organization_deployment
        if monitored_accounts is not UNSET:
            field_dict["monitored_accounts"] = monitored_accounts
        if organization_account_id is not UNSET:
            field_dict["organization_account_id"] = organization_account_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_cloud_node_monitored_account import ModelCloudNodeMonitoredAccount

        d = src_dict.copy()
        account_id = d.pop("account_id")

        cloud_provider = ModelCloudNodeAccountRegisterReqCloudProvider(d.pop("cloud_provider"))

        host_node_id = d.pop("host_node_id")

        node_id = d.pop("node_id")

        version = d.pop("version")

        account_name = d.pop("account_name", UNSET)

        is_organization_deployment = d.pop("is_organization_deployment", UNSET)

        def _parse_monitored_accounts(data: object) -> Union[List["ModelCloudNodeMonitoredAccount"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                monitored_accounts_type_0 = []
                _monitored_accounts_type_0 = data
                for monitored_accounts_type_0_item_data in _monitored_accounts_type_0:
                    monitored_accounts_type_0_item = ModelCloudNodeMonitoredAccount.from_dict(
                        monitored_accounts_type_0_item_data
                    )

                    monitored_accounts_type_0.append(monitored_accounts_type_0_item)

                return monitored_accounts_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelCloudNodeMonitoredAccount"], None, Unset], data)

        monitored_accounts = _parse_monitored_accounts(d.pop("monitored_accounts", UNSET))

        organization_account_id = d.pop("organization_account_id", UNSET)

        model_cloud_node_account_register_req = cls(
            account_id=account_id,
            cloud_provider=cloud_provider,
            host_node_id=host_node_id,
            node_id=node_id,
            version=version,
            account_name=account_name,
            is_organization_deployment=is_organization_deployment,
            monitored_accounts=monitored_accounts,
            organization_account_id=organization_account_id,
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
