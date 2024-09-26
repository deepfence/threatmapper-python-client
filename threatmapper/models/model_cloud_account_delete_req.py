from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelCloudAccountDeleteReq")


@_attrs_define
class ModelCloudAccountDeleteReq:
    """
    Attributes:
        node_ids (Union[List[str], None]):
    """

    node_ids: Union[List[str], None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_ids: Union[List[str], None]
        if isinstance(self.node_ids, list):
            node_ids = self.node_ids

        else:
            node_ids = self.node_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_ids": node_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_node_ids(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                node_ids_type_0 = cast(List[str], data)

                return node_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        node_ids = _parse_node_ids(d.pop("node_ids"))

        model_cloud_account_delete_req = cls(
            node_ids=node_ids,
        )

        model_cloud_account_delete_req.additional_properties = d
        return model_cloud_account_delete_req

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
