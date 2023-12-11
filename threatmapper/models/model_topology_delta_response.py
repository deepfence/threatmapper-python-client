from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_node_identifier import ModelNodeIdentifier


T = TypeVar("T", bound="ModelTopologyDeltaResponse")


@_attrs_define
class ModelTopologyDeltaResponse:
    """
    Example:
        {'deletions': [{'node_type': 'image', 'node_id': 'node_id'}, {'node_type': 'image', 'node_id': 'node_id'}],
            'additons': [{'node_type': 'image', 'node_id': 'node_id'}, {'node_type': 'image', 'node_id': 'node_id'}],
            'deletion_timestamp': 6, 'addition_timestamp': 0}

    Attributes:
        addition_timestamp (Union[Unset, int]):
        additons (Union[Unset, None, List['ModelNodeIdentifier']]):
        deletion_timestamp (Union[Unset, int]):
        deletions (Union[Unset, None, List['ModelNodeIdentifier']]):
    """

    addition_timestamp: Union[Unset, int] = UNSET
    additons: Union[Unset, None, List["ModelNodeIdentifier"]] = UNSET
    deletion_timestamp: Union[Unset, int] = UNSET
    deletions: Union[Unset, None, List["ModelNodeIdentifier"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        addition_timestamp = self.addition_timestamp
        additons: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.additons, Unset):
            if self.additons is None:
                additons = None
            else:
                additons = []
                for additons_item_data in self.additons:
                    additons_item = additons_item_data.to_dict()

                    additons.append(additons_item)

        deletion_timestamp = self.deletion_timestamp
        deletions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.deletions, Unset):
            if self.deletions is None:
                deletions = None
            else:
                deletions = []
                for deletions_item_data in self.deletions:
                    deletions_item = deletions_item_data.to_dict()

                    deletions.append(deletions_item)

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

        additons = []
        _additons = d.pop("additons", UNSET)
        for additons_item_data in _additons or []:
            additons_item = ModelNodeIdentifier.from_dict(additons_item_data)

            additons.append(additons_item)

        deletion_timestamp = d.pop("deletion_timestamp", UNSET)

        deletions = []
        _deletions = d.pop("deletions", UNSET)
        for deletions_item_data in _deletions or []:
            deletions_item = ModelNodeIdentifier.from_dict(deletions_item_data)

            deletions.append(deletions_item)

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
