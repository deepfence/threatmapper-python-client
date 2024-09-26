from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_registry_add_req_extras_type_0 import ModelRegistryAddReqExtrasType0
    from ..models.model_registry_add_req_non_secret_type_0 import ModelRegistryAddReqNonSecretType0
    from ..models.model_registry_add_req_secret_type_0 import ModelRegistryAddReqSecretType0


T = TypeVar("T", bound="ModelRegistryAddReq")


@_attrs_define
class ModelRegistryAddReq:
    """
    Attributes:
        name (str):
        registry_type (str):
        extras (Union['ModelRegistryAddReqExtrasType0', None, Unset]):
        non_secret (Union['ModelRegistryAddReqNonSecretType0', None, Unset]):
        secret (Union['ModelRegistryAddReqSecretType0', None, Unset]):
    """

    name: str
    registry_type: str
    extras: Union["ModelRegistryAddReqExtrasType0", None, Unset] = UNSET
    non_secret: Union["ModelRegistryAddReqNonSecretType0", None, Unset] = UNSET
    secret: Union["ModelRegistryAddReqSecretType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.model_registry_add_req_extras_type_0 import ModelRegistryAddReqExtrasType0
        from ..models.model_registry_add_req_non_secret_type_0 import ModelRegistryAddReqNonSecretType0
        from ..models.model_registry_add_req_secret_type_0 import ModelRegistryAddReqSecretType0

        name = self.name

        registry_type = self.registry_type

        extras: Union[Dict[str, Any], None, Unset]
        if isinstance(self.extras, Unset):
            extras = UNSET
        elif isinstance(self.extras, ModelRegistryAddReqExtrasType0):
            extras = self.extras.to_dict()
        else:
            extras = self.extras

        non_secret: Union[Dict[str, Any], None, Unset]
        if isinstance(self.non_secret, Unset):
            non_secret = UNSET
        elif isinstance(self.non_secret, ModelRegistryAddReqNonSecretType0):
            non_secret = self.non_secret.to_dict()
        else:
            non_secret = self.non_secret

        secret: Union[Dict[str, Any], None, Unset]
        if isinstance(self.secret, Unset):
            secret = UNSET
        elif isinstance(self.secret, ModelRegistryAddReqSecretType0):
            secret = self.secret.to_dict()
        else:
            secret = self.secret

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
        from ..models.model_registry_add_req_extras_type_0 import ModelRegistryAddReqExtrasType0
        from ..models.model_registry_add_req_non_secret_type_0 import ModelRegistryAddReqNonSecretType0
        from ..models.model_registry_add_req_secret_type_0 import ModelRegistryAddReqSecretType0

        d = src_dict.copy()
        name = d.pop("name")

        registry_type = d.pop("registry_type")

        def _parse_extras(data: object) -> Union["ModelRegistryAddReqExtrasType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extras_type_0 = ModelRegistryAddReqExtrasType0.from_dict(data)

                return extras_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelRegistryAddReqExtrasType0", None, Unset], data)

        extras = _parse_extras(d.pop("extras", UNSET))

        def _parse_non_secret(data: object) -> Union["ModelRegistryAddReqNonSecretType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                non_secret_type_0 = ModelRegistryAddReqNonSecretType0.from_dict(data)

                return non_secret_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelRegistryAddReqNonSecretType0", None, Unset], data)

        non_secret = _parse_non_secret(d.pop("non_secret", UNSET))

        def _parse_secret(data: object) -> Union["ModelRegistryAddReqSecretType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                secret_type_0 = ModelRegistryAddReqSecretType0.from_dict(data)

                return secret_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelRegistryAddReqSecretType0", None, Unset], data)

        secret = _parse_secret(d.pop("secret", UNSET))

        model_registry_add_req = cls(
            name=name,
            registry_type=registry_type,
            extras=extras,
            non_secret=non_secret,
            secret=secret,
        )

        model_registry_add_req.additional_properties = d
        return model_registry_add_req

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
