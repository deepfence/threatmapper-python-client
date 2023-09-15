from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelCloudNodeEnableDisableReq")


@_attrs_define
class ModelCloudNodeEnableDisableReq:
    """
    Example:
        {'control_ids': ['control_ids', 'control_ids'], 'node_id': 'node_id'}

    Attributes:
        control_ids (Union[Unset, None, List[str]]):
        node_id (Union[Unset, str]):
    """

    control_ids: Union[Unset, None, List[str]] = UNSET
    node_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        control_ids: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.control_ids, Unset):
            if self.control_ids is None:
                control_ids = None
            else:
                control_ids = self.control_ids

        node_id = self.node_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if control_ids is not UNSET:
            field_dict["control_ids"] = control_ids
        if node_id is not UNSET:
            field_dict["node_id"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        control_ids = cast(List[str], d.pop("control_ids", UNSET))

        node_id = d.pop("node_id", UNSET)

        model_cloud_node_enable_disable_req = cls(
            control_ids=control_ids,
            node_id=node_id,
        )

        model_cloud_node_enable_disable_req.additional_properties = d
        return model_cloud_node_enable_disable_req

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
