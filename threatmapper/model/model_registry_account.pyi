# coding: utf-8

"""
    Deepfence ThreatMapper

    Deepfence Runtime API provides programmatic control over Deepfence microservice securing your container, kubernetes and cloud deployments. The API abstracts away underlying infrastructure details like cloud provider,  container distros, container orchestrator and type of deployment. This is one uniform API to manage and control security alerts, policies and response to alerts for microservices running anywhere i.e. managed pure greenfield container deployments or a mix of containers, VMs and serverless paradigms like AWS Fargate.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: community@deepfence.io
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from threatmapper import schemas  # noqa: F401


class ModelRegistryAccount(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "container_images",
            "host_name",
            "node_id",
        }
        
        class properties:
            
            
            class container_images(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ModelContainerImage']:
                        return ModelContainerImage
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'container_images':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            host_name = schemas.StrSchema
            node_id = schemas.StrSchema
            __annotations__ = {
                "container_images": container_images,
                "host_name": host_name,
                "node_id": node_id,
            }
    
    container_images: MetaOapg.properties.container_images
    host_name: MetaOapg.properties.host_name
    node_id: MetaOapg.properties.node_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["container_images"]) -> MetaOapg.properties.container_images: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["host_name"]) -> MetaOapg.properties.host_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["node_id"]) -> MetaOapg.properties.node_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["container_images", "host_name", "node_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["container_images"]) -> MetaOapg.properties.container_images: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["host_name"]) -> MetaOapg.properties.host_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["node_id"]) -> MetaOapg.properties.node_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["container_images", "host_name", "node_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        container_images: typing.Union[MetaOapg.properties.container_images, list, tuple, None, ],
        host_name: typing.Union[MetaOapg.properties.host_name, str, ],
        node_id: typing.Union[MetaOapg.properties.node_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelRegistryAccount':
        return super().__new__(
            cls,
            *_args,
            container_images=container_images,
            host_name=host_name,
            node_id=node_id,
            _configuration=_configuration,
            **kwargs,
        )

from threatmapper.model.model_container_image import ModelContainerImage
