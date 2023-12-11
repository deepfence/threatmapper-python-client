from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diagnosis_diagnostic_logs_link import DiagnosisDiagnosticLogsLink


T = TypeVar("T", bound="DiagnosisGetDiagnosticLogsResponse")


@_attrs_define
class DiagnosisGetDiagnosticLogsResponse:
    """
    Example:
        {'console_logs': [{'url_link': 'url_link', 'created_at': 'created_at', 'label': 'label', 'message': 'message'},
            {'url_link': 'url_link', 'created_at': 'created_at', 'label': 'label', 'message': 'message'}], 'agent_logs':
            [{'url_link': 'url_link', 'created_at': 'created_at', 'label': 'label', 'message': 'message'}, {'url_link':
            'url_link', 'created_at': 'created_at', 'label': 'label', 'message': 'message'}], 'cloud_scanner_logs':
            [{'url_link': 'url_link', 'created_at': 'created_at', 'label': 'label', 'message': 'message'}, {'url_link':
            'url_link', 'created_at': 'created_at', 'label': 'label', 'message': 'message'}]}

    Attributes:
        agent_logs (Union[Unset, None, List['DiagnosisDiagnosticLogsLink']]):
        cloud_scanner_logs (Union[Unset, None, List['DiagnosisDiagnosticLogsLink']]):
        console_logs (Union[Unset, None, List['DiagnosisDiagnosticLogsLink']]):
    """

    agent_logs: Union[Unset, None, List["DiagnosisDiagnosticLogsLink"]] = UNSET
    cloud_scanner_logs: Union[Unset, None, List["DiagnosisDiagnosticLogsLink"]] = UNSET
    console_logs: Union[Unset, None, List["DiagnosisDiagnosticLogsLink"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_logs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.agent_logs, Unset):
            if self.agent_logs is None:
                agent_logs = None
            else:
                agent_logs = []
                for agent_logs_item_data in self.agent_logs:
                    agent_logs_item = agent_logs_item_data.to_dict()

                    agent_logs.append(agent_logs_item)

        cloud_scanner_logs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cloud_scanner_logs, Unset):
            if self.cloud_scanner_logs is None:
                cloud_scanner_logs = None
            else:
                cloud_scanner_logs = []
                for cloud_scanner_logs_item_data in self.cloud_scanner_logs:
                    cloud_scanner_logs_item = cloud_scanner_logs_item_data.to_dict()

                    cloud_scanner_logs.append(cloud_scanner_logs_item)

        console_logs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.console_logs, Unset):
            if self.console_logs is None:
                console_logs = None
            else:
                console_logs = []
                for console_logs_item_data in self.console_logs:
                    console_logs_item = console_logs_item_data.to_dict()

                    console_logs.append(console_logs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_logs is not UNSET:
            field_dict["agent_logs"] = agent_logs
        if cloud_scanner_logs is not UNSET:
            field_dict["cloud_scanner_logs"] = cloud_scanner_logs
        if console_logs is not UNSET:
            field_dict["console_logs"] = console_logs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.diagnosis_diagnostic_logs_link import DiagnosisDiagnosticLogsLink

        d = src_dict.copy()
        agent_logs = []
        _agent_logs = d.pop("agent_logs", UNSET)
        for agent_logs_item_data in _agent_logs or []:
            agent_logs_item = DiagnosisDiagnosticLogsLink.from_dict(agent_logs_item_data)

            agent_logs.append(agent_logs_item)

        cloud_scanner_logs = []
        _cloud_scanner_logs = d.pop("cloud_scanner_logs", UNSET)
        for cloud_scanner_logs_item_data in _cloud_scanner_logs or []:
            cloud_scanner_logs_item = DiagnosisDiagnosticLogsLink.from_dict(cloud_scanner_logs_item_data)

            cloud_scanner_logs.append(cloud_scanner_logs_item)

        console_logs = []
        _console_logs = d.pop("console_logs", UNSET)
        for console_logs_item_data in _console_logs or []:
            console_logs_item = DiagnosisDiagnosticLogsLink.from_dict(console_logs_item_data)

            console_logs.append(console_logs_item)

        diagnosis_get_diagnostic_logs_response = cls(
            agent_logs=agent_logs,
            cloud_scanner_logs=cloud_scanner_logs,
            console_logs=console_logs,
        )

        diagnosis_get_diagnostic_logs_response.additional_properties = d
        return diagnosis_get_diagnostic_logs_response

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
