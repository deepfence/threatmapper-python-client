from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_basic_node import ModelBasicNode


T = TypeVar("T", bound="ModelScanResultBasicNode")


@_attrs_define
class ModelScanResultBasicNode:
    """
    Attributes:
        basic_nodes (Union[List['ModelBasicNode'], None]):
        result_id (str):
    """

    basic_nodes: Union[List["ModelBasicNode"], None]
    result_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        basic_nodes: Union[List[Dict[str, Any]], None]
        if isinstance(self.basic_nodes, list):
            basic_nodes = []
            for basic_nodes_type_0_item_data in self.basic_nodes:
                basic_nodes_type_0_item = basic_nodes_type_0_item_data.to_dict()
                basic_nodes.append(basic_nodes_type_0_item)

        else:
            basic_nodes = self.basic_nodes

        result_id = self.result_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "basic_nodes": basic_nodes,
                "result_id": result_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_basic_node import ModelBasicNode

        d = src_dict.copy()

        def _parse_basic_nodes(data: object) -> Union[List["ModelBasicNode"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                basic_nodes_type_0 = []
                _basic_nodes_type_0 = data
                for basic_nodes_type_0_item_data in _basic_nodes_type_0:
                    basic_nodes_type_0_item = ModelBasicNode.from_dict(basic_nodes_type_0_item_data)

                    basic_nodes_type_0.append(basic_nodes_type_0_item)

                return basic_nodes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelBasicNode"], None], data)

        basic_nodes = _parse_basic_nodes(d.pop("basic_nodes"))

        result_id = d.pop("result_id")

        model_scan_result_basic_node = cls(
            basic_nodes=basic_nodes,
            result_id=result_id,
        )

        model_scan_result_basic_node.additional_properties = d
        return model_scan_result_basic_node

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
