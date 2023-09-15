from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_basic_node import ModelBasicNode


T = TypeVar("T", bound="ModelScanResultBasicNode")


@_attrs_define
class ModelScanResultBasicNode:
    """
    Example:
        {'basic_nodes': [{'node_type': 'node_type', 'name': 'name', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'node_type': 'node_type', 'name': 'name', 'host_name': 'host_name', 'node_id': 'node_id'}], 'result_id':
            'result_id'}

    Attributes:
        result_id (str):
        basic_nodes (Optional[List['ModelBasicNode']]):
    """

    result_id: str
    basic_nodes: Optional[List["ModelBasicNode"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result_id = self.result_id
        if self.basic_nodes is None:
            basic_nodes = None
        else:
            basic_nodes = []
            for basic_nodes_item_data in self.basic_nodes:
                basic_nodes_item = basic_nodes_item_data.to_dict()

                basic_nodes.append(basic_nodes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "result_id": result_id,
                "basic_nodes": basic_nodes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_basic_node import ModelBasicNode

        d = src_dict.copy()
        result_id = d.pop("result_id")

        basic_nodes = []
        _basic_nodes = d.pop("basic_nodes")
        for basic_nodes_item_data in _basic_nodes or []:
            basic_nodes_item = ModelBasicNode.from_dict(basic_nodes_item_data)

            basic_nodes.append(basic_nodes_item)

        model_scan_result_basic_node = cls(
            result_id=result_id,
            basic_nodes=basic_nodes,
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
