from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_add_generative_ai_bedrock_integration_aws_region import (
    ModelAddGenerativeAiBedrockIntegrationAwsRegion,
)
from ..models.model_add_generative_ai_bedrock_integration_model_id import ModelAddGenerativeAiBedrockIntegrationModelId
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelAddGenerativeAiBedrockIntegration")


@_attrs_define
class ModelAddGenerativeAiBedrockIntegration:
    """
    Example:
        {'aws_region': 'us-east-1', 'aws_access_key': 'aws_access_key', 'model_id': 'anthropic.claude-v2',
            'aws_secret_key': 'aws_secret_key', 'use_iam_role': True}

    Attributes:
        aws_region (ModelAddGenerativeAiBedrockIntegrationAwsRegion):
        model_id (ModelAddGenerativeAiBedrockIntegrationModelId):
        aws_access_key (Union[Unset, str]):
        aws_secret_key (Union[Unset, str]):
        use_iam_role (Union[Unset, bool]):
    """

    aws_region: ModelAddGenerativeAiBedrockIntegrationAwsRegion
    model_id: ModelAddGenerativeAiBedrockIntegrationModelId
    aws_access_key: Union[Unset, str] = UNSET
    aws_secret_key: Union[Unset, str] = UNSET
    use_iam_role: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aws_region = self.aws_region.value

        model_id = self.model_id.value

        aws_access_key = self.aws_access_key

        aws_secret_key = self.aws_secret_key

        use_iam_role = self.use_iam_role

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aws_region": aws_region,
                "model_id": model_id,
            }
        )
        if aws_access_key is not UNSET:
            field_dict["aws_access_key"] = aws_access_key
        if aws_secret_key is not UNSET:
            field_dict["aws_secret_key"] = aws_secret_key
        if use_iam_role is not UNSET:
            field_dict["use_iam_role"] = use_iam_role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        aws_region = ModelAddGenerativeAiBedrockIntegrationAwsRegion(d.pop("aws_region"))

        model_id = ModelAddGenerativeAiBedrockIntegrationModelId(d.pop("model_id"))

        aws_access_key = d.pop("aws_access_key", UNSET)

        aws_secret_key = d.pop("aws_secret_key", UNSET)

        use_iam_role = d.pop("use_iam_role", UNSET)

        model_add_generative_ai_bedrock_integration = cls(
            aws_region=aws_region,
            model_id=model_id,
            aws_access_key=aws_access_key,
            aws_secret_key=aws_secret_key,
            use_iam_role=use_iam_role,
        )

        model_add_generative_ai_bedrock_integration.additional_properties = d
        return model_add_generative_ai_bedrock_integration

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
