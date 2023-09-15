from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelAddScheduledTaskRequest")


@_attrs_define
class ModelAddScheduledTaskRequest:
    """
    Example:
        {'node_type': 'node_type', 'cron_expr': 'cron_expr', 'action': 'action', 'description': 'description',
            'filters': 'filters'}

    Attributes:
        action (Union[Unset, str]):
        cron_expr (Union[Unset, str]):
        description (Union[Unset, str]):
        filters (Union[Unset, str]):
        node_type (Union[Unset, str]):
    """

    action: Union[Unset, str] = UNSET
    cron_expr: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    filters: Union[Unset, str] = UNSET
    node_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action
        cron_expr = self.cron_expr
        description = self.description
        filters = self.filters
        node_type = self.node_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if cron_expr is not UNSET:
            field_dict["cron_expr"] = cron_expr
        if description is not UNSET:
            field_dict["description"] = description
        if filters is not UNSET:
            field_dict["filters"] = filters
        if node_type is not UNSET:
            field_dict["node_type"] = node_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action = d.pop("action", UNSET)

        cron_expr = d.pop("cron_expr", UNSET)

        description = d.pop("description", UNSET)

        filters = d.pop("filters", UNSET)

        node_type = d.pop("node_type", UNSET)

        model_add_scheduled_task_request = cls(
            action=action,
            cron_expr=cron_expr,
            description=description,
            filters=filters,
            node_type=node_type,
        )

        model_add_scheduled_task_request.additional_properties = d
        return model_add_scheduled_task_request

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
