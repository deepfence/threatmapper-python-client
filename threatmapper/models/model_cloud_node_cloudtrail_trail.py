from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelCloudNodeCloudtrailTrail")


@_attrs_define
class ModelCloudNodeCloudtrailTrail:
    """
    Example:
        {'account_id': 'account_id', 'trail_name': 'trail_name'}

    Attributes:
        account_id (Union[Unset, str]):
        trail_name (Union[Unset, str]):
    """

    account_id: Union[Unset, str] = UNSET
    trail_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        trail_name = self.trail_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if trail_name is not UNSET:
            field_dict["trail_name"] = trail_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("account_id", UNSET)

        trail_name = d.pop("trail_name", UNSET)

        model_cloud_node_cloudtrail_trail = cls(
            account_id=account_id,
            trail_name=trail_name,
        )

        model_cloud_node_cloudtrail_trail.additional_properties = d
        return model_cloud_node_cloudtrail_trail

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
