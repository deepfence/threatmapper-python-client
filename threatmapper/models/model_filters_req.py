from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_filters_req_having import ModelFiltersReqHaving


T = TypeVar("T", bound="ModelFiltersReq")


@_attrs_define
class ModelFiltersReq:
    """
    Example:
        {'having': {'key': ''}, 'filters': ['filters', 'filters']}

    Attributes:
        filters (Optional[List[str]]):
        having (Union[Unset, None, ModelFiltersReqHaving]):
    """

    filters: Optional[List[str]]
    having: Union[Unset, None, "ModelFiltersReqHaving"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if self.filters is None:
            filters = None
        else:
            filters = self.filters

        having: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.having, Unset):
            having = self.having.to_dict() if self.having else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
            }
        )
        if having is not UNSET:
            field_dict["having"] = having

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_filters_req_having import ModelFiltersReqHaving

        d = src_dict.copy()
        filters = cast(List[str], d.pop("filters"))

        _having = d.pop("having", UNSET)
        having: Union[Unset, None, ModelFiltersReqHaving]
        if _having is None:
            having = None
        elif isinstance(_having, Unset):
            having = UNSET
        else:
            having = ModelFiltersReqHaving.from_dict(_having)

        model_filters_req = cls(
            filters=filters,
            having=having,
        )

        model_filters_req.additional_properties = d
        return model_filters_req

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
