from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_registry_update_req_extras import ModelRegistryUpdateReqExtras
    from ..models.model_registry_update_req_non_secret import ModelRegistryUpdateReqNonSecret
    from ..models.model_registry_update_req_secret import ModelRegistryUpdateReqSecret


T = TypeVar("T", bound="ModelRegistryUpdateReq")


@_attrs_define
class ModelRegistryUpdateReq:
    """
    Example:
        {'non_secret': {'key': ''}, 'registry_type': 'registry_type', 'name': 'name', 'extras': {'key': ''}, 'secret':
            {'key': ''}}

    Attributes:
        name (str):
        registry_type (str):
        extras (Union[Unset, None, ModelRegistryUpdateReqExtras]):
        non_secret (Union[Unset, None, ModelRegistryUpdateReqNonSecret]):
        secret (Union[Unset, None, ModelRegistryUpdateReqSecret]):
    """

    name: str
    registry_type: str
    extras: Union[Unset, None, "ModelRegistryUpdateReqExtras"] = UNSET
    non_secret: Union[Unset, None, "ModelRegistryUpdateReqNonSecret"] = UNSET
    secret: Union[Unset, None, "ModelRegistryUpdateReqSecret"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        registry_type = self.registry_type
        extras: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict() if self.extras else None

        non_secret: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.non_secret, Unset):
            non_secret = self.non_secret.to_dict() if self.non_secret else None

        secret: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.secret, Unset):
            secret = self.secret.to_dict() if self.secret else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "registry_type": registry_type,
            }
        )
        if extras is not UNSET:
            field_dict["extras"] = extras
        if non_secret is not UNSET:
            field_dict["non_secret"] = non_secret
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_registry_update_req_extras import ModelRegistryUpdateReqExtras
        from ..models.model_registry_update_req_non_secret import ModelRegistryUpdateReqNonSecret
        from ..models.model_registry_update_req_secret import ModelRegistryUpdateReqSecret

        d = src_dict.copy()
        name = d.pop("name")

        registry_type = d.pop("registry_type")

        _extras = d.pop("extras", UNSET)
        extras: Union[Unset, None, ModelRegistryUpdateReqExtras]
        if _extras is None:
            extras = None
        elif isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = ModelRegistryUpdateReqExtras.from_dict(_extras)

        _non_secret = d.pop("non_secret", UNSET)
        non_secret: Union[Unset, None, ModelRegistryUpdateReqNonSecret]
        if _non_secret is None:
            non_secret = None
        elif isinstance(_non_secret, Unset):
            non_secret = UNSET
        else:
            non_secret = ModelRegistryUpdateReqNonSecret.from_dict(_non_secret)

        _secret = d.pop("secret", UNSET)
        secret: Union[Unset, None, ModelRegistryUpdateReqSecret]
        if _secret is None:
            secret = None
        elif isinstance(_secret, Unset):
            secret = UNSET
        else:
            secret = ModelRegistryUpdateReqSecret.from_dict(_secret)

        model_registry_update_req = cls(
            name=name,
            registry_type=registry_type,
            extras=extras,
            non_secret=non_secret,
            secret=secret,
        )

        model_registry_update_req.additional_properties = d
        return model_registry_update_req

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
