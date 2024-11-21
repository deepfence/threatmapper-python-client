from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelDeleteRegistryBulkReq")


@_attrs_define
class ModelDeleteRegistryBulkReq:
    """
    Example:
        {'registry_ids': ['registry_ids', 'registry_ids']}

    Attributes:
        registry_ids (Union[List[str], None]):
    """

    registry_ids: Union[List[str], None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        registry_ids: Union[List[str], None]
        if isinstance(self.registry_ids, list):
            registry_ids = self.registry_ids

        else:
            registry_ids = self.registry_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "registry_ids": registry_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_registry_ids(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                registry_ids_type_0 = cast(List[str], data)

                return registry_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        registry_ids = _parse_registry_ids(d.pop("registry_ids"))

        model_delete_registry_bulk_req = cls(
            registry_ids=registry_ids,
        )

        model_delete_registry_bulk_req.additional_properties = d
        return model_delete_registry_bulk_req

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
