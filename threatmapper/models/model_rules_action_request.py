from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelRulesActionRequest")


@_attrs_define
class ModelRulesActionRequest:
    """
    Example:
        {'rule_ids': ['rule_ids', 'rule_ids']}

    Attributes:
        rule_ids (Union[List[str], None]):
    """

    rule_ids: Union[List[str], None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rule_ids: Union[List[str], None]
        if isinstance(self.rule_ids, list):
            rule_ids = self.rule_ids

        else:
            rule_ids = self.rule_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_ids": rule_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_rule_ids(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rule_ids_type_0 = cast(List[str], data)

                return rule_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        rule_ids = _parse_rule_ids(d.pop("rule_ids"))

        model_rules_action_request = cls(
            rule_ids=rule_ids,
        )

        model_rules_action_request.additional_properties = d
        return model_rules_action_request

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
