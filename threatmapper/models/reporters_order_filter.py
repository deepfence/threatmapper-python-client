from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reporters_order_spec import ReportersOrderSpec


T = TypeVar("T", bound="ReportersOrderFilter")


@_attrs_define
class ReportersOrderFilter:
    """
    Example:
        {'order_fields': [{'size': 0, 'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True,
            'field_name': 'field_name'}]}

    Attributes:
        order_fields (Union[List['ReportersOrderSpec'], None]):
    """

    order_fields: Union[List["ReportersOrderSpec"], None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_fields: Union[List[Dict[str, Any]], None]
        if isinstance(self.order_fields, list):
            order_fields = []
            for order_fields_type_0_item_data in self.order_fields:
                order_fields_type_0_item = order_fields_type_0_item_data.to_dict()
                order_fields.append(order_fields_type_0_item)

        else:
            order_fields = self.order_fields

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_fields": order_fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reporters_order_spec import ReportersOrderSpec

        d = src_dict.copy()

        def _parse_order_fields(data: object) -> Union[List["ReportersOrderSpec"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                order_fields_type_0 = []
                _order_fields_type_0 = data
                for order_fields_type_0_item_data in _order_fields_type_0:
                    order_fields_type_0_item = ReportersOrderSpec.from_dict(order_fields_type_0_item_data)

                    order_fields_type_0.append(order_fields_type_0_item)

                return order_fields_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ReportersOrderSpec"], None], data)

        order_fields = _parse_order_fields(d.pop("order_fields"))

        reporters_order_filter = cls(
            order_fields=order_fields,
        )

        reporters_order_filter.additional_properties = d
        return reporters_order_filter

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
