from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_filters_result_filters_type_0 import ModelFiltersResultFiltersType0


T = TypeVar("T", bound="ModelFiltersResult")


@_attrs_define
class ModelFiltersResult:
    """
    Example:
        {'filters': {'key': ['filters', 'filters']}}

    Attributes:
        filters (Union['ModelFiltersResultFiltersType0', None]):
    """

    filters: Union["ModelFiltersResultFiltersType0", None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.model_filters_result_filters_type_0 import ModelFiltersResultFiltersType0

        filters: Union[Dict[str, Any], None]
        if isinstance(self.filters, ModelFiltersResultFiltersType0):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

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
        from ..models.model_filters_result_filters_type_0 import ModelFiltersResultFiltersType0

        d = src_dict.copy()

        def _parse_filters(data: object) -> Union["ModelFiltersResultFiltersType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = ModelFiltersResultFiltersType0.from_dict(data)

                return filters_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelFiltersResultFiltersType0", None], data)

        filters = _parse_filters(d.pop("filters"))

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
