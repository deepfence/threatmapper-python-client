from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_node_identifier import ModelNodeIdentifier


T = TypeVar("T", bound="ModelTopologyDeltaResponse")


@_attrs_define
class ModelTopologyDeltaResponse:
    """
    Attributes:
        addition_timestamp (Union[Unset, int]):
        additons (Union[List['ModelNodeIdentifier'], None, Unset]):
        deletion_timestamp (Union[Unset, int]):
        deletions (Union[List['ModelNodeIdentifier'], None, Unset]):
    """

    addition_timestamp: Union[Unset, int] = UNSET
    additons: Union[List["ModelNodeIdentifier"], None, Unset] = UNSET
    deletion_timestamp: Union[Unset, int] = UNSET
    deletions: Union[List["ModelNodeIdentifier"], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        addition_timestamp = self.addition_timestamp

        additons: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.additons, Unset):
            additons = UNSET
        elif isinstance(self.additons, list):
            additons = []
            for additons_type_0_item_data in self.additons:
                additons_type_0_item = additons_type_0_item_data.to_dict()
                additons.append(additons_type_0_item)

        else:
            additons = self.additons

        deletion_timestamp = self.deletion_timestamp

        deletions: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.deletions, Unset):
            deletions = UNSET
        elif isinstance(self.deletions, list):
            deletions = []
            for deletions_type_0_item_data in self.deletions:
                deletions_type_0_item = deletions_type_0_item_data.to_dict()
                deletions.append(deletions_type_0_item)

        else:
            deletions = self.deletions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addition_timestamp is not UNSET:
            field_dict["addition_timestamp"] = addition_timestamp
        if additons is not UNSET:
            field_dict["additons"] = additons
        if deletion_timestamp is not UNSET:
            field_dict["deletion_timestamp"] = deletion_timestamp
        if deletions is not UNSET:
            field_dict["deletions"] = deletions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_node_identifier import ModelNodeIdentifier

        d = src_dict.copy()
        addition_timestamp = d.pop("addition_timestamp", UNSET)

        def _parse_additons(data: object) -> Union[List["ModelNodeIdentifier"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                additons_type_0 = []
                _additons_type_0 = data
                for additons_type_0_item_data in _additons_type_0:
                    additons_type_0_item = ModelNodeIdentifier.from_dict(additons_type_0_item_data)

                    additons_type_0.append(additons_type_0_item)

                return additons_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelNodeIdentifier"], None, Unset], data)

        additons = _parse_additons(d.pop("additons", UNSET))

        deletion_timestamp = d.pop("deletion_timestamp", UNSET)

        def _parse_deletions(data: object) -> Union[List["ModelNodeIdentifier"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                deletions_type_0 = []
                _deletions_type_0 = data
                for deletions_type_0_item_data in _deletions_type_0:
                    deletions_type_0_item = ModelNodeIdentifier.from_dict(deletions_type_0_item_data)

                    deletions_type_0.append(deletions_type_0_item)

                return deletions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelNodeIdentifier"], None, Unset], data)

        deletions = _parse_deletions(d.pop("deletions", UNSET))

        model_topology_delta_response = cls(
            addition_timestamp=addition_timestamp,
            additons=additons,
            deletion_timestamp=deletion_timestamp,
            deletions=deletions,
        )

        model_topology_delta_response.additional_properties = d
        return model_topology_delta_response

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
