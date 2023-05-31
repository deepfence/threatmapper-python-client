import typing_extensions

from threatmapper.apis.tags import TagValues
from threatmapper.apis.tags.authentication_api import AuthenticationApi
from threatmapper.apis.tags.common_api import CommonApi
from threatmapper.apis.tags.compliance_api import ComplianceApi
from threatmapper.apis.tags.topology_api import TopologyApi
from threatmapper.apis.tags.secret_scan_api import SecretScanApi
from threatmapper.apis.tags.malware_scan_api import MalwareScanApi
from threatmapper.apis.tags.vulnerability_api import VulnerabilityApi
from threatmapper.apis.tags.cloud_nodes_api import CloudNodesApi
from threatmapper.apis.tags.cloud_resources_api import CloudResourcesApi
from threatmapper.apis.tags.cloud_scanner_api import CloudScannerApi
from threatmapper.apis.tags.controls_api import ControlsApi
from threatmapper.apis.tags.diagnosis_api import DiagnosisApi
from threatmapper.apis.tags.integration_api import IntegrationApi
from threatmapper.apis.tags.internal_api import InternalApi
from threatmapper.apis.tags.lookup_api import LookupApi
from threatmapper.apis.tags.registry_api import RegistryApi
from threatmapper.apis.tags.reports_api import ReportsApi
from threatmapper.apis.tags.scan_results_api import ScanResultsApi
from threatmapper.apis.tags.search_api import SearchApi
from threatmapper.apis.tags.settings_api import SettingsApi
from threatmapper.apis.tags.threat_api import ThreatApi
from threatmapper.apis.tags.user_api import UserApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.COMMON: CommonApi,
        TagValues.COMPLIANCE: ComplianceApi,
        TagValues.TOPOLOGY: TopologyApi,
        TagValues.SECRET_SCAN: SecretScanApi,
        TagValues.MALWARE_SCAN: MalwareScanApi,
        TagValues.VULNERABILITY: VulnerabilityApi,
        TagValues.CLOUD_NODES: CloudNodesApi,
        TagValues.CLOUD_RESOURCES: CloudResourcesApi,
        TagValues.CLOUD_SCANNER: CloudScannerApi,
        TagValues.CONTROLS: ControlsApi,
        TagValues.DIAGNOSIS: DiagnosisApi,
        TagValues.INTEGRATION: IntegrationApi,
        TagValues.INTERNAL: InternalApi,
        TagValues.LOOKUP: LookupApi,
        TagValues.REGISTRY: RegistryApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.SCAN_RESULTS: ScanResultsApi,
        TagValues.SEARCH: SearchApi,
        TagValues.SETTINGS: SettingsApi,
        TagValues.THREAT: ThreatApi,
        TagValues.USER: UserApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.COMMON: CommonApi,
        TagValues.COMPLIANCE: ComplianceApi,
        TagValues.TOPOLOGY: TopologyApi,
        TagValues.SECRET_SCAN: SecretScanApi,
        TagValues.MALWARE_SCAN: MalwareScanApi,
        TagValues.VULNERABILITY: VulnerabilityApi,
        TagValues.CLOUD_NODES: CloudNodesApi,
        TagValues.CLOUD_RESOURCES: CloudResourcesApi,
        TagValues.CLOUD_SCANNER: CloudScannerApi,
        TagValues.CONTROLS: ControlsApi,
        TagValues.DIAGNOSIS: DiagnosisApi,
        TagValues.INTEGRATION: IntegrationApi,
        TagValues.INTERNAL: InternalApi,
        TagValues.LOOKUP: LookupApi,
        TagValues.REGISTRY: RegistryApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.SCAN_RESULTS: ScanResultsApi,
        TagValues.SEARCH: SearchApi,
        TagValues.SETTINGS: SettingsApi,
        TagValues.THREAT: ThreatApi,
        TagValues.USER: UserApi,
    }
)
