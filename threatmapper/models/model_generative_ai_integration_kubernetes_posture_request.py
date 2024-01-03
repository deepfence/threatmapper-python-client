from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_generative_ai_integration_kubernetes_posture_request_query_type import (
    ModelGenerativeAiIntegrationKubernetesPostureRequestQueryType,
)
from ..models.model_generative_ai_integration_kubernetes_posture_request_remediation_format import (
    ModelGenerativeAiIntegrationKubernetesPostureRequestRemediationFormat,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelGenerativeAiIntegrationKubernetesPostureRequest")


@_attrs_define
class ModelGenerativeAiIntegrationKubernetesPostureRequest:
    """
    Example:
        {'integration_id': 0, 'remediation_format': 'all', 'description': 'description', 'query_type': 'remediation',
            'compliance_check_type': 'compliance_check_type'}

    Attributes:
        compliance_check_type (str):
        description (str):
        query_type (ModelGenerativeAiIntegrationKubernetesPostureRequestQueryType):
        remediation_format (ModelGenerativeAiIntegrationKubernetesPostureRequestRemediationFormat):
        integration_id (Union[Unset, int]):
    """

    compliance_check_type: str
    description: str
    query_type: ModelGenerativeAiIntegrationKubernetesPostureRequestQueryType
    remediation_format: ModelGenerativeAiIntegrationKubernetesPostureRequestRemediationFormat
    integration_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compliance_check_type = self.compliance_check_type
        description = self.description
        query_type = self.query_type.value

        remediation_format = self.remediation_format.value

        integration_id = self.integration_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "compliance_check_type": compliance_check_type,
                "description": description,
                "query_type": query_type,
                "remediation_format": remediation_format,
            }
        )
        if integration_id is not UNSET:
            field_dict["integration_id"] = integration_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        compliance_check_type = d.pop("compliance_check_type")

        description = d.pop("description")

        query_type = ModelGenerativeAiIntegrationKubernetesPostureRequestQueryType(d.pop("query_type"))

        remediation_format = ModelGenerativeAiIntegrationKubernetesPostureRequestRemediationFormat(
            d.pop("remediation_format")
        )

        integration_id = d.pop("integration_id", UNSET)

        model_generative_ai_integration_kubernetes_posture_request = cls(
            compliance_check_type=compliance_check_type,
            description=description,
            query_type=query_type,
            remediation_format=remediation_format,
            integration_id=integration_id,
        )

        model_generative_ai_integration_kubernetes_posture_request.additional_properties = d
        return model_generative_ai_integration_kubernetes_posture_request

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
