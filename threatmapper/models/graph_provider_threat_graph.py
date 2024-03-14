from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.graph_threat_node_info import GraphThreatNodeInfo


T = TypeVar("T", bound="GraphProviderThreatGraph")


@_attrs_define
class GraphProviderThreatGraph:
    """
    Attributes:
        cloud_compliance_count (int):
        cloud_warn_alarm_count (int):
        compliance_count (int):
        exploitable_secrets_count (int):
        exploitable_vulnerabilities_count (int):
        resources (Union[List['GraphThreatNodeInfo'], None]):
        secrets_count (int):
        vulnerability_count (int):
        warn_alarm_count (int):
    """

    cloud_compliance_count: int
    cloud_warn_alarm_count: int
    compliance_count: int
    exploitable_secrets_count: int
    exploitable_vulnerabilities_count: int
    resources: Union[List["GraphThreatNodeInfo"], None]
    secrets_count: int
    vulnerability_count: int
    warn_alarm_count: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloud_compliance_count = self.cloud_compliance_count

        cloud_warn_alarm_count = self.cloud_warn_alarm_count

        compliance_count = self.compliance_count

        exploitable_secrets_count = self.exploitable_secrets_count

        exploitable_vulnerabilities_count = self.exploitable_vulnerabilities_count

        resources: Union[List[Dict[str, Any]], None]
        if isinstance(self.resources, list):
            resources = []
            for resources_type_0_item_data in self.resources:
                resources_type_0_item = resources_type_0_item_data.to_dict()
                resources.append(resources_type_0_item)

        else:
            resources = self.resources

        secrets_count = self.secrets_count

        vulnerability_count = self.vulnerability_count

        warn_alarm_count = self.warn_alarm_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_compliance_count": cloud_compliance_count,
                "cloud_warn_alarm_count": cloud_warn_alarm_count,
                "compliance_count": compliance_count,
                "exploitable_secrets_count": exploitable_secrets_count,
                "exploitable_vulnerabilities_count": exploitable_vulnerabilities_count,
                "resources": resources,
                "secrets_count": secrets_count,
                "vulnerability_count": vulnerability_count,
                "warn_alarm_count": warn_alarm_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.graph_threat_node_info import GraphThreatNodeInfo

        d = src_dict.copy()
        cloud_compliance_count = d.pop("cloud_compliance_count")

        cloud_warn_alarm_count = d.pop("cloud_warn_alarm_count")

        compliance_count = d.pop("compliance_count")

        exploitable_secrets_count = d.pop("exploitable_secrets_count")

        exploitable_vulnerabilities_count = d.pop("exploitable_vulnerabilities_count")

        def _parse_resources(data: object) -> Union[List["GraphThreatNodeInfo"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resources_type_0 = []
                _resources_type_0 = data
                for resources_type_0_item_data in _resources_type_0:
                    resources_type_0_item = GraphThreatNodeInfo.from_dict(resources_type_0_item_data)

                    resources_type_0.append(resources_type_0_item)

                return resources_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["GraphThreatNodeInfo"], None], data)

        resources = _parse_resources(d.pop("resources"))

        secrets_count = d.pop("secrets_count")

        vulnerability_count = d.pop("vulnerability_count")

        warn_alarm_count = d.pop("warn_alarm_count")

        graph_provider_threat_graph = cls(
            cloud_compliance_count=cloud_compliance_count,
            cloud_warn_alarm_count=cloud_warn_alarm_count,
            compliance_count=compliance_count,
            exploitable_secrets_count=exploitable_secrets_count,
            exploitable_vulnerabilities_count=exploitable_vulnerabilities_count,
            resources=resources,
            secrets_count=secrets_count,
            vulnerability_count=vulnerability_count,
            warn_alarm_count=warn_alarm_count,
        )

        graph_provider_threat_graph.additional_properties = d
        return graph_provider_threat_graph

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
