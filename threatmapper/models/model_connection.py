from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelConnection")


@_attrs_define
class ModelConnection:
    """
    Attributes:
        count (Union[Unset, int]):
        ips (Union[List[Any], None, Unset]):
        node_id (Union[Unset, str]):
        node_name (Union[Unset, str]):
    """

    count: Union[Unset, int] = UNSET
    ips: Union[List[Any], None, Unset] = UNSET
    node_id: Union[Unset, str] = UNSET
    node_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

        ips: Union[List[Any], None, Unset]
        if isinstance(self.ips, Unset):
            ips = UNSET
        elif isinstance(self.ips, list):
            ips = self.ips

        else:
            ips = self.ips

        node_id = self.node_id

        node_name = self.node_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if ips is not UNSET:
            field_dict["ips"] = ips
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if node_name is not UNSET:
            field_dict["node_name"] = node_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count", UNSET)

        def _parse_ips(data: object) -> Union[List[Any], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ips_type_0 = cast(List[Any], data)

                return ips_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[Any], None, Unset], data)

        ips = _parse_ips(d.pop("ips", UNSET))

        node_id = d.pop("node_id", UNSET)

        node_name = d.pop("node_name", UNSET)

        model_connection = cls(
            count=count,
            ips=ips,
            node_id=node_id,
            node_name=node_name,
        )

        model_connection.additional_properties = d
        return model_connection

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
