from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_generative_ai_integration_cloud_posture_request_query_type import (
    ModelGenerativeAiIntegrationCloudPostureRequestQueryType,
)
from ..models.model_generative_ai_integration_cloud_posture_request_remediation_format import (
    ModelGenerativeAiIntegrationCloudPostureRequestRemediationFormat,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelGenerativeAiIntegrationCloudPostureRequest")


@_attrs_define
class ModelGenerativeAiIntegrationCloudPostureRequest:
    """
    Attributes:
        cloud_provider (str):
        compliance_check_type (str):
        query_type (ModelGenerativeAiIntegrationCloudPostureRequestQueryType):
        remediation_format (ModelGenerativeAiIntegrationCloudPostureRequestRemediationFormat):
        title (str):
        group (Union[Unset, str]):
        integration_id (Union[Unset, int]):
        service (Union[Unset, str]):
    """

    cloud_provider: str
    compliance_check_type: str
    query_type: ModelGenerativeAiIntegrationCloudPostureRequestQueryType
    remediation_format: ModelGenerativeAiIntegrationCloudPostureRequestRemediationFormat
    title: str
    group: Union[Unset, str] = UNSET
    integration_id: Union[Unset, int] = UNSET
    service: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloud_provider = self.cloud_provider

        compliance_check_type = self.compliance_check_type

        query_type = self.query_type.value

        remediation_format = self.remediation_format.value

        title = self.title

        group = self.group

        integration_id = self.integration_id

        service = self.service

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_provider": cloud_provider,
                "compliance_check_type": compliance_check_type,
                "query_type": query_type,
                "remediation_format": remediation_format,
                "title": title,
            }
        )
        if group is not UNSET:
            field_dict["group"] = group
        if integration_id is not UNSET:
            field_dict["integration_id"] = integration_id
        if service is not UNSET:
            field_dict["service"] = service

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cloud_provider = d.pop("cloud_provider")

        compliance_check_type = d.pop("compliance_check_type")

        query_type = ModelGenerativeAiIntegrationCloudPostureRequestQueryType(d.pop("query_type"))

        remediation_format = ModelGenerativeAiIntegrationCloudPostureRequestRemediationFormat(
            d.pop("remediation_format")
        )

        title = d.pop("title")

        group = d.pop("group", UNSET)

        integration_id = d.pop("integration_id", UNSET)

        service = d.pop("service", UNSET)

        model_generative_ai_integration_cloud_posture_request = cls(
            cloud_provider=cloud_provider,
            compliance_check_type=compliance_check_type,
            query_type=query_type,
            remediation_format=remediation_format,
            title=title,
            group=group,
            integration_id=integration_id,
            service=service,
        )

        model_generative_ai_integration_cloud_posture_request.additional_properties = d
        return model_generative_ai_integration_cloud_posture_request

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
