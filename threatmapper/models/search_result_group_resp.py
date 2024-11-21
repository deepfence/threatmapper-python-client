from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
        groups (Union[List['SearchResultGroup'], None, Unset]):
    """

    groups: Union[List["SearchResultGroup"], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        groups: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = []
            for groups_type_0_item_data in self.groups:
                groups_type_0_item = groups_type_0_item_data.to_dict()
                groups.append(groups_type_0_item)

        else:
            groups = self.groups

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

        def _parse_groups(data: object) -> Union[List["SearchResultGroup"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = []
                _groups_type_0 = data
                for groups_type_0_item_data in _groups_type_0:
                    groups_type_0_item = SearchResultGroup.from_dict(groups_type_0_item_data)

                    groups_type_0.append(groups_type_0_item)

                return groups_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["SearchResultGroup"], None, Unset], data)

        groups = _parse_groups(d.pop("groups", UNSET))

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
