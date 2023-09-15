from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_filters_result_filters import ModelFiltersResultFilters


T = TypeVar("T", bound="ModelFiltersResult")


@_attrs_define
class ModelFiltersResult:
    """
    Example:
        {'filters': {'key': ['filters', 'filters']}}

    Attributes:
        filters (Optional[ModelFiltersResultFilters]):
    """

    filters: Optional["ModelFiltersResultFilters"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filters = self.filters.to_dict() if self.filters else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_filters_result_filters import ModelFiltersResultFilters

        d = src_dict.copy()
        _filters = d.pop("filters")
        filters: Optional[ModelFiltersResultFilters]
        if _filters is None:
            filters = None
        else:
            filters = ModelFiltersResultFilters.from_dict(_filters)

        model_filters_result = cls(
            filters=filters,
        )

        model_filters_result.additional_properties = d
        return model_filters_result

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
