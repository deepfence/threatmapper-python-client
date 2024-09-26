from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelGetAgentBinaryDownloadURLResponse")


@_attrs_define
class ModelGetAgentBinaryDownloadURLResponse:
    """
    Attributes:
        agent_binary_amd64_download_url (Union[Unset, str]):
        agent_binary_arm64_download_url (Union[Unset, str]):
        start_agent_script_download_url (Union[Unset, str]):
        uninstall_agent_script_download_url (Union[Unset, str]):
    """

    agent_binary_amd64_download_url: Union[Unset, str] = UNSET
    agent_binary_arm64_download_url: Union[Unset, str] = UNSET
    start_agent_script_download_url: Union[Unset, str] = UNSET
    uninstall_agent_script_download_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_binary_amd64_download_url = self.agent_binary_amd64_download_url

        agent_binary_arm64_download_url = self.agent_binary_arm64_download_url

        start_agent_script_download_url = self.start_agent_script_download_url

        uninstall_agent_script_download_url = self.uninstall_agent_script_download_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_binary_amd64_download_url is not UNSET:
            field_dict["agent_binary_amd64_download_url"] = agent_binary_amd64_download_url
        if agent_binary_arm64_download_url is not UNSET:
            field_dict["agent_binary_arm64_download_url"] = agent_binary_arm64_download_url
        if start_agent_script_download_url is not UNSET:
            field_dict["start_agent_script_download_url"] = start_agent_script_download_url
        if uninstall_agent_script_download_url is not UNSET:
            field_dict["uninstall_agent_script_download_url"] = uninstall_agent_script_download_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        agent_binary_amd64_download_url = d.pop("agent_binary_amd64_download_url", UNSET)

        agent_binary_arm64_download_url = d.pop("agent_binary_arm64_download_url", UNSET)

        start_agent_script_download_url = d.pop("start_agent_script_download_url", UNSET)

        uninstall_agent_script_download_url = d.pop("uninstall_agent_script_download_url", UNSET)

        model_get_agent_binary_download_url_response = cls(
            agent_binary_amd64_download_url=agent_binary_amd64_download_url,
            agent_binary_arm64_download_url=agent_binary_arm64_download_url,
            start_agent_script_download_url=start_agent_script_download_url,
            uninstall_agent_script_download_url=uninstall_agent_script_download_url,
        )

        model_get_agent_binary_download_url_response.additional_properties = d
        return model_get_agent_binary_download_url_response

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
