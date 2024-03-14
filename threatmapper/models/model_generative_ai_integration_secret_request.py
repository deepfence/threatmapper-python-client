from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_generative_ai_integration_secret_request_query_type import (
    ModelGenerativeAiIntegrationSecretRequestQueryType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelGenerativeAiIntegrationSecretRequest")


@_attrs_define
class ModelGenerativeAiIntegrationSecretRequest:
    """
    Attributes:
        name (str):
        query_type (ModelGenerativeAiIntegrationSecretRequestQueryType):
        integration_id (Union[Unset, int]):
    """

    name: str
    query_type: ModelGenerativeAiIntegrationSecretRequestQueryType
    integration_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        query_type = self.query_type.value

        integration_id = self.integration_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "query_type": query_type,
            }
        )
        if integration_id is not UNSET:
            field_dict["integration_id"] = integration_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        query_type = ModelGenerativeAiIntegrationSecretRequestQueryType(d.pop("query_type"))

        integration_id = d.pop("integration_id", UNSET)

        model_generative_ai_integration_secret_request = cls(
            name=name,
            query_type=query_type,
            integration_id=integration_id,
        )

        model_generative_ai_integration_secret_request.additional_properties = d
        return model_generative_ai_integration_secret_request

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
