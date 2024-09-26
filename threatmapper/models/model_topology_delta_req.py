from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelTopologyDeltaReq")


@_attrs_define
class ModelTopologyDeltaReq:
    """
    Attributes:
        addition (bool):
        addition_timestamp (int):
        deletion (bool):
        deletion_timestamp (int):
        entity_types (Union[List[str], None]):
    """

    addition: bool
    addition_timestamp: int
    deletion: bool
    deletion_timestamp: int
    entity_types: Union[List[str], None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        addition = self.addition

        addition_timestamp = self.addition_timestamp

        deletion = self.deletion

        deletion_timestamp = self.deletion_timestamp

        entity_types: Union[List[str], None]
        if isinstance(self.entity_types, list):
            entity_types = self.entity_types

        else:
            entity_types = self.entity_types

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "addition": addition,
                "addition_timestamp": addition_timestamp,
                "deletion": deletion,
                "deletion_timestamp": deletion_timestamp,
                "entity_types": entity_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        addition = d.pop("addition")

        addition_timestamp = d.pop("addition_timestamp")

        deletion = d.pop("deletion")

        deletion_timestamp = d.pop("deletion_timestamp")

        def _parse_entity_types(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                entity_types_type_0 = cast(List[str], data)

                return entity_types_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        entity_types = _parse_entity_types(d.pop("entity_types"))

        model_topology_delta_req = cls(
            addition=addition,
            addition_timestamp=addition_timestamp,
            deletion=deletion,
            deletion_timestamp=deletion_timestamp,
            entity_types=entity_types,
        )

        model_topology_delta_req.additional_properties = d
        return model_topology_delta_req

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
