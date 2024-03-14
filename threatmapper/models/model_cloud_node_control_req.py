from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_cloud_node_control_req_cloud_provider import ModelCloudNodeControlReqCloudProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelCloudNodeControlReq")


@_attrs_define
class ModelCloudNodeControlReq:
    """
    Attributes:
        cloud_provider (ModelCloudNodeControlReqCloudProvider):
        compliance_type (str):
        node_id (Union[Unset, str]):
    """

    cloud_provider: ModelCloudNodeControlReqCloudProvider
    compliance_type: str
    node_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloud_provider = self.cloud_provider.value

        compliance_type = self.compliance_type

        node_id = self.node_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_provider": cloud_provider,
                "compliance_type": compliance_type,
            }
        )
        if node_id is not UNSET:
            field_dict["node_id"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cloud_provider = ModelCloudNodeControlReqCloudProvider(d.pop("cloud_provider"))

        compliance_type = d.pop("compliance_type")

        node_id = d.pop("node_id", UNSET)

        model_cloud_node_control_req = cls(
            cloud_provider=cloud_provider,
            compliance_type=compliance_type,
            node_id=node_id,
        )

        model_cloud_node_control_req.additional_properties = d
        return model_cloud_node_control_req

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
