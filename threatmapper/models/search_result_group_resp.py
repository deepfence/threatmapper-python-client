from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_result_group import SearchResultGroup


T = TypeVar("T", bound="SearchResultGroupResp")


@_attrs_define
class SearchResultGroupResp:
    """
    Example:
        {'groups': [{'severity': 'severity', 'count': 0, 'name': 'name'}, {'severity': 'severity', 'count': 0, 'name':
            'name'}]}

    Attributes:
        groups (Union[Unset, None, List['SearchResultGroup']]):
    """

    groups: Union[Unset, None, List["SearchResultGroup"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        groups: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            if self.groups is None:
                groups = None
            else:
                groups = []
                for groups_item_data in self.groups:
                    groups_item = groups_item_data.to_dict()

                    groups.append(groups_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.search_result_group import SearchResultGroup

        d = src_dict.copy()
        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = SearchResultGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        search_result_group_resp = cls(
            groups=groups,
        )

        search_result_group_resp.additional_properties = d
        return search_result_group_resp

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
