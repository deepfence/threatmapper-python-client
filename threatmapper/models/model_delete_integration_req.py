from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelDeleteIntegrationReq")


@_attrs_define
class ModelDeleteIntegrationReq:
    """
    Attributes:
        integration_ids (Union[List[int], None]):
    """

    integration_ids: Union[List[int], None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        integration_ids: Union[List[int], None]
        if isinstance(self.integration_ids, list):
            integration_ids = self.integration_ids

        else:
            integration_ids = self.integration_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "integration_ids": integration_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_integration_ids(data: object) -> Union[List[int], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                integration_ids_type_0 = cast(List[int], data)

                return integration_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[int], None], data)

        integration_ids = _parse_integration_ids(d.pop("integration_ids"))

        model_delete_integration_req = cls(
            integration_ids=integration_ids,
        )

        model_delete_integration_req.additional_properties = d
        return model_delete_integration_req

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
