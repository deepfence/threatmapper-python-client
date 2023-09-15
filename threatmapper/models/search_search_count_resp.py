from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.search_search_count_resp_categories import SearchSearchCountRespCategories


T = TypeVar("T", bound="SearchSearchCountResp")


@_attrs_define
class SearchSearchCountResp:
    """
    Example:
        {'count': 6, 'categories': {'key': 0}}

    Attributes:
        count (int):
        categories (Optional[SearchSearchCountRespCategories]):
    """

    count: int
    categories: Optional["SearchSearchCountRespCategories"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        categories = self.categories.to_dict() if self.categories else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "categories": categories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.search_search_count_resp_categories import SearchSearchCountRespCategories

        d = src_dict.copy()
        count = d.pop("count")

        _categories = d.pop("categories")
        categories: Optional[SearchSearchCountRespCategories]
        if _categories is None:
            categories = None
        else:
            categories = SearchSearchCountRespCategories.from_dict(_categories)

        search_search_count_resp = cls(
            count=count,
            categories=categories,
        )

        search_search_count_resp.additional_properties = d
        return search_search_count_resp

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
