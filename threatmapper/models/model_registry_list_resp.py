from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelRegistryListResp")


@_attrs_define
class ModelRegistryListResp:
    """
    Attributes:
        created_at (Union[Unset, int]):
        id (Union[Unset, int]):
        is_syncing (Union[Unset, bool]):
        name (Union[Unset, str]):
        node_id (Union[Unset, str]):
        non_secret (Union[Unset, Any]):
        registry_type (Union[Unset, str]):
        updated_at (Union[Unset, int]):
    """

    created_at: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    is_syncing: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    non_secret: Union[Unset, Any] = UNSET
    registry_type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at

        id = self.id

        is_syncing = self.is_syncing

        name = self.name

        node_id = self.node_id

        non_secret = self.non_secret

        registry_type = self.registry_type

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if is_syncing is not UNSET:
            field_dict["is_syncing"] = is_syncing
        if name is not UNSET:
            field_dict["name"] = name
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if non_secret is not UNSET:
            field_dict["non_secret"] = non_secret
        if registry_type is not UNSET:
            field_dict["registry_type"] = registry_type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        is_syncing = d.pop("is_syncing", UNSET)

        name = d.pop("name", UNSET)

        node_id = d.pop("node_id", UNSET)

        non_secret = d.pop("non_secret", UNSET)

        registry_type = d.pop("registry_type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        model_registry_list_resp = cls(
            created_at=created_at,
            id=id,
            is_syncing=is_syncing,
            name=name,
            node_id=node_id,
            non_secret=non_secret,
            registry_type=registry_type,
            updated_at=updated_at,
        )

        model_registry_list_resp.additional_properties = d
        return model_registry_list_resp

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
