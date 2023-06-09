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


class PostgresqlDbScheduler(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            action = schemas.StrSchema
            created_at = schemas.DateTimeSchema
            cron_expr = schemas.StrSchema
            description = schemas.StrSchema
            id = schemas.IntSchema
            is_enabled = schemas.BoolSchema
            is_system = schemas.BoolSchema
            last_ran_at = schemas.DictSchema
            payload = schemas.AnyTypeSchema
            status = schemas.StrSchema
            updated_at = schemas.DateTimeSchema
            __annotations__ = {
                "action": action,
                "created_at": created_at,
                "cron_expr": cron_expr,
                "description": description,
                "id": id,
                "is_enabled": is_enabled,
                "is_system": is_system,
                "last_ran_at": last_ran_at,
                "payload": payload,
                "status": status,
                "updated_at": updated_at,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["action"]) -> MetaOapg.properties.action: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cron_expr"]) -> MetaOapg.properties.cron_expr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_enabled"]) -> MetaOapg.properties.is_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_system"]) -> MetaOapg.properties.is_system: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_ran_at"]) -> MetaOapg.properties.last_ran_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payload"]) -> MetaOapg.properties.payload: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["action", "created_at", "cron_expr", "description", "id", "is_enabled", "is_system", "last_ran_at", "payload", "status", "updated_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["action"]) -> typing.Union[MetaOapg.properties.action, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cron_expr"]) -> typing.Union[MetaOapg.properties.cron_expr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_enabled"]) -> typing.Union[MetaOapg.properties.is_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_system"]) -> typing.Union[MetaOapg.properties.is_system, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_ran_at"]) -> typing.Union[MetaOapg.properties.last_ran_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payload"]) -> typing.Union[MetaOapg.properties.payload, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["action", "created_at", "cron_expr", "description", "id", "is_enabled", "is_system", "last_ran_at", "payload", "status", "updated_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        action: typing.Union[MetaOapg.properties.action, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        cron_expr: typing.Union[MetaOapg.properties.cron_expr, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        is_enabled: typing.Union[MetaOapg.properties.is_enabled, bool, schemas.Unset] = schemas.unset,
        is_system: typing.Union[MetaOapg.properties.is_system, bool, schemas.Unset] = schemas.unset,
        last_ran_at: typing.Union[MetaOapg.properties.last_ran_at, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        payload: typing.Union[MetaOapg.properties.payload, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostgresqlDbScheduler':
        return super().__new__(
            cls,
            *_args,
            action=action,
            created_at=created_at,
            cron_expr=cron_expr,
            description=description,
            id=id,
            is_enabled=is_enabled,
            is_system=is_system,
            last_ran_at=last_ran_at,
            payload=payload,
            status=status,
            updated_at=updated_at,
            _configuration=_configuration,
            **kwargs,
        )
