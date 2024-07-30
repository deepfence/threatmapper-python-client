from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelGenerativeAiIntegrationListResponse")


@_attrs_define
class ModelGenerativeAiIntegrationListResponse:
    """
    Example:
        {'default_integration': True, 'id': 0, 'label': 'label', 'integration_type': 'integration_type',
            'last_error_msg': 'last_error_msg'}

    Attributes:
        default_integration (Union[Unset, bool]):
        id (Union[Unset, int]):
        integration_type (Union[Unset, str]):
        label (Union[Unset, str]):
        last_error_msg (Union[Unset, str]):
    """

    default_integration: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    integration_type: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    last_error_msg: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default_integration = self.default_integration

        id = self.id

        integration_type = self.integration_type

        label = self.label

        last_error_msg = self.last_error_msg

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_integration is not UNSET:
            field_dict["default_integration"] = default_integration
        if id is not UNSET:
            field_dict["id"] = id
        if integration_type is not UNSET:
            field_dict["integration_type"] = integration_type
        if label is not UNSET:
            field_dict["label"] = label
        if last_error_msg is not UNSET:
            field_dict["last_error_msg"] = last_error_msg

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        default_integration = d.pop("default_integration", UNSET)

        id = d.pop("id", UNSET)

        integration_type = d.pop("integration_type", UNSET)

        label = d.pop("label", UNSET)

        last_error_msg = d.pop("last_error_msg", UNSET)

        model_generative_ai_integration_list_response = cls(
            default_integration=default_integration,
            id=id,
            integration_type=integration_type,
            label=label,
            last_error_msg=last_error_msg,
        )

        model_generative_ai_integration_list_response.additional_properties = d
        return model_generative_ai_integration_list_response

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
