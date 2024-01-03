from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelListAgentVersionResp")


@_attrs_define
class ModelListAgentVersionResp:
    """
    Example:
        {'versions': ['versions', 'versions']}

    Attributes:
        versions (Optional[List[str]]):
    """

    versions: Optional[List[str]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if self.versions is None:
            versions = None
        else:
            versions = self.versions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "versions": versions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        versions = cast(List[str], d.pop("versions"))

        model_list_agent_version_resp = cls(
            versions=versions,
        )

        model_list_agent_version_resp.additional_properties = d
        return model_list_agent_version_resp

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
