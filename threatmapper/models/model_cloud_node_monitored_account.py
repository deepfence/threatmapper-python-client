from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelCloudNodeMonitoredAccount")


@_attrs_define
class ModelCloudNodeMonitoredAccount:
    """
    Example:
        {'account_id': 'account_id', 'account_name': 'account_name', 'node_id': 'node_id'}

    Attributes:
        account_id (str):
        node_id (str):
        account_name (Union[Unset, str]):
    """

    account_id: str
    node_id: str
    account_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id

        node_id = self.node_id

        account_name = self.account_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "node_id": node_id,
            }
        )
        if account_name is not UNSET:
            field_dict["account_name"] = account_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("account_id")

        node_id = d.pop("node_id")

        account_name = d.pop("account_name", UNSET)

        model_cloud_node_monitored_account = cls(
            account_id=account_id,
            node_id=node_id,
            account_name=account_name,
        )

        model_cloud_node_monitored_account.additional_properties = d
        return model_cloud_node_monitored_account

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
