import typing_extensions

from threatmapper.paths import PathValues
from threatmapper.apis.paths.deepfence_api_token import DeepfenceApiToken
from threatmapper.apis.paths.deepfence_api_token_reset import DeepfenceApiTokenReset
from threatmapper.apis.paths.deepfence_auth_token import DeepfenceAuthToken
from threatmapper.apis.paths.deepfence_auth_token_refresh import DeepfenceAuthTokenRefresh
from threatmapper.apis.paths.deepfence_cloud_node_account import DeepfenceCloudNodeAccount
from threatmapper.apis.paths.deepfence_cloud_node_list_accounts import DeepfenceCloudNodeListAccounts
from threatmapper.apis.paths.deepfence_cloud_node_list_providers import DeepfenceCloudNodeListProviders
from threatmapper.apis.paths.deepfence_controls_agent import DeepfenceControlsAgent
from threatmapper.apis.paths.deepfence_controls_agent_init import DeepfenceControlsAgentInit
from threatmapper.apis.paths.deepfence_controls_agent_upgrade import DeepfenceControlsAgentUpgrade
from threatmapper.apis.paths.deepfence_controls_cloud_node import DeepfenceControlsCloudNode
from threatmapper.apis.paths.deepfence_controls_cloud_node_disable import DeepfenceControlsCloudNodeDisable
from threatmapper.apis.paths.deepfence_controls_cloud_node_enable import DeepfenceControlsCloudNodeEnable
from threatmapper.apis.paths.deepfence_controls_kubernetes_cluster import DeepfenceControlsKubernetesCluster
from threatmapper.apis.paths.deepfence_database_vulnerability import DeepfenceDatabaseVulnerability
from threatmapper.apis.paths.deepfence_diagnosis_agent_logs import DeepfenceDiagnosisAgentLogs
from threatmapper.apis.paths.deepfence_diagnosis_agent_logs_status_node_id import DeepfenceDiagnosisAgentLogsStatusNodeId
from threatmapper.apis.paths.deepfence_diagnosis_console_logs import DeepfenceDiagnosisConsoleLogs
from threatmapper.apis.paths.deepfence_diagnosis_diagnostic_logs import DeepfenceDiagnosisDiagnosticLogs
from threatmapper.apis.paths.deepfence_diagnosis_notification import DeepfenceDiagnosisNotification
from threatmapper.apis.paths.deepfence_end_user_license_agreement import DeepfenceEndUserLicenseAgreement
from threatmapper.apis.paths.deepfence_filters_cloud_compliance import DeepfenceFiltersCloudCompliance
from threatmapper.apis.paths.deepfence_filters_compliance import DeepfenceFiltersCompliance
from threatmapper.apis.paths.deepfence_graph_threat import DeepfenceGraphThreat
from threatmapper.apis.paths.deepfence_graph_threat_vulnerability import DeepfenceGraphThreatVulnerability
from threatmapper.apis.paths.deepfence_graph_topology_ import DeepfenceGraphTopology
from threatmapper.apis.paths.deepfence_graph_topology_containers import DeepfenceGraphTopologyContainers
from threatmapper.apis.paths.deepfence_graph_topology_hosts import DeepfenceGraphTopologyHosts
from threatmapper.apis.paths.deepfence_graph_topology_kubernetes import DeepfenceGraphTopologyKubernetes
from threatmapper.apis.paths.deepfence_graph_topology_pods import DeepfenceGraphTopologyPods
from threatmapper.apis.paths.deepfence_ingest_cloud_compliance import DeepfenceIngestCloudCompliance
from threatmapper.apis.paths.deepfence_ingest_cloud_compliance_scan_status import DeepfenceIngestCloudComplianceScanStatus
from threatmapper.apis.paths.deepfence_ingest_cloud_resources import DeepfenceIngestCloudResources
from threatmapper.apis.paths.deepfence_ingest_compliance import DeepfenceIngestCompliance
from threatmapper.apis.paths.deepfence_ingest_malware import DeepfenceIngestMalware
from threatmapper.apis.paths.deepfence_ingest_malware_scan_logs import DeepfenceIngestMalwareScanLogs
from threatmapper.apis.paths.deepfence_ingest_report import DeepfenceIngestReport
from threatmapper.apis.paths.deepfence_ingest_sbom import DeepfenceIngestSbom
from threatmapper.apis.paths.deepfence_ingest_secret_scan_logs import DeepfenceIngestSecretScanLogs
from threatmapper.apis.paths.deepfence_ingest_secrets import DeepfenceIngestSecrets
from threatmapper.apis.paths.deepfence_ingest_sync_report import DeepfenceIngestSyncReport
from threatmapper.apis.paths.deepfence_ingest_vulnerabilities import DeepfenceIngestVulnerabilities
from threatmapper.apis.paths.deepfence_ingest_vulnerabilities_scan_logs import DeepfenceIngestVulnerabilitiesScanLogs
from threatmapper.apis.paths.deepfence_integration import DeepfenceIntegration
from threatmapper.apis.paths.deepfence_integration_integration_id import DeepfenceIntegrationIntegrationId
from threatmapper.apis.paths.deepfence_internal_console_api_token import DeepfenceInternalConsoleApiToken
from threatmapper.apis.paths.deepfence_lookup_cloud_resources import DeepfenceLookupCloudResources
from threatmapper.apis.paths.deepfence_lookup_containerimages import DeepfenceLookupContainerimages
from threatmapper.apis.paths.deepfence_lookup_containers import DeepfenceLookupContainers
from threatmapper.apis.paths.deepfence_lookup_hosts import DeepfenceLookupHosts
from threatmapper.apis.paths.deepfence_lookup_kubernetesclusters import DeepfenceLookupKubernetesclusters
from threatmapper.apis.paths.deepfence_lookup_pods import DeepfenceLookupPods
from threatmapper.apis.paths.deepfence_lookup_processes import DeepfenceLookupProcesses
from threatmapper.apis.paths.deepfence_lookup_registryaccount import DeepfenceLookupRegistryaccount
from threatmapper.apis.paths.deepfence_registryaccount import DeepfenceRegistryaccount
from threatmapper.apis.paths.deepfence_registryaccount_count_images import DeepfenceRegistryaccountCountImages
from threatmapper.apis.paths.deepfence_registryaccount_count_stubs import DeepfenceRegistryaccountCountStubs
from threatmapper.apis.paths.deepfence_registryaccount_gcr import DeepfenceRegistryaccountGcr
from threatmapper.apis.paths.deepfence_registryaccount_images import DeepfenceRegistryaccountImages
from threatmapper.apis.paths.deepfence_registryaccount_stubs import DeepfenceRegistryaccountStubs
from threatmapper.apis.paths.deepfence_registryaccount_summary import DeepfenceRegistryaccountSummary
from threatmapper.apis.paths.deepfence_registryaccount_registry_id import DeepfenceRegistryaccountRegistryId
from threatmapper.apis.paths.deepfence_registryaccount_registry_id_summary import DeepfenceRegistryaccountRegistryIdSummary
from threatmapper.apis.paths.deepfence_registryaccount_registry_type_summary_by_type import DeepfenceRegistryaccountRegistryTypeSummaryByType
from threatmapper.apis.paths.deepfence_reports import DeepfenceReports
from threatmapper.apis.paths.deepfence_reports_report_id import DeepfenceReportsReportId
from threatmapper.apis.paths.deepfence_scan_list_cloud_compliance import DeepfenceScanListCloudCompliance
from threatmapper.apis.paths.deepfence_scan_list_compliance import DeepfenceScanListCompliance
from threatmapper.apis.paths.deepfence_scan_list_malware import DeepfenceScanListMalware
from threatmapper.apis.paths.deepfence_scan_list_secret import DeepfenceScanListSecret
from threatmapper.apis.paths.deepfence_scan_list_vulnerability import DeepfenceScanListVulnerability
from threatmapper.apis.paths.deepfence_scan_nodes_in_result import DeepfenceScanNodesInResult
from threatmapper.apis.paths.deepfence_scan_results_action_delete import DeepfenceScanResultsActionDelete
from threatmapper.apis.paths.deepfence_scan_results_action_mask import DeepfenceScanResultsActionMask
from threatmapper.apis.paths.deepfence_scan_results_action_notify import DeepfenceScanResultsActionNotify
from threatmapper.apis.paths.deepfence_scan_results_action_unmask import DeepfenceScanResultsActionUnmask
from threatmapper.apis.paths.deepfence_scan_results_cloud_compliance import DeepfenceScanResultsCloudCompliance
from threatmapper.apis.paths.deepfence_scan_results_compliance import DeepfenceScanResultsCompliance
from threatmapper.apis.paths.deepfence_scan_results_count_cloud_compliance import DeepfenceScanResultsCountCloudCompliance
from threatmapper.apis.paths.deepfence_scan_results_count_compliance import DeepfenceScanResultsCountCompliance
from threatmapper.apis.paths.deepfence_scan_results_count_group_malware import DeepfenceScanResultsCountGroupMalware
from threatmapper.apis.paths.deepfence_scan_results_count_group_malware_class import DeepfenceScanResultsCountGroupMalwareClass
from threatmapper.apis.paths.deepfence_scan_results_count_group_secret import DeepfenceScanResultsCountGroupSecret
from threatmapper.apis.paths.deepfence_scan_results_count_malware import DeepfenceScanResultsCountMalware
from threatmapper.apis.paths.deepfence_scan_results_count_secret import DeepfenceScanResultsCountSecret
from threatmapper.apis.paths.deepfence_scan_results_count_vulnerability import DeepfenceScanResultsCountVulnerability
from threatmapper.apis.paths.deepfence_scan_results_malware import DeepfenceScanResultsMalware
from threatmapper.apis.paths.deepfence_scan_results_malware_class import DeepfenceScanResultsMalwareClass
from threatmapper.apis.paths.deepfence_scan_results_malware_rules import DeepfenceScanResultsMalwareRules
from threatmapper.apis.paths.deepfence_scan_results_secret import DeepfenceScanResultsSecret
from threatmapper.apis.paths.deepfence_scan_results_secret_rules import DeepfenceScanResultsSecretRules
from threatmapper.apis.paths.deepfence_scan_results_vulnerability import DeepfenceScanResultsVulnerability
from threatmapper.apis.paths.deepfence_scan_sbom import DeepfenceScanSbom
from threatmapper.apis.paths.deepfence_scan_sbom_download import DeepfenceScanSbomDownload
from threatmapper.apis.paths.deepfence_scan_start_compliance import DeepfenceScanStartCompliance
from threatmapper.apis.paths.deepfence_scan_start_malware import DeepfenceScanStartMalware
from threatmapper.apis.paths.deepfence_scan_start_secret import DeepfenceScanStartSecret
from threatmapper.apis.paths.deepfence_scan_start_vulnerability import DeepfenceScanStartVulnerability
from threatmapper.apis.paths.deepfence_scan_status_cloud_compliance import DeepfenceScanStatusCloudCompliance
from threatmapper.apis.paths.deepfence_scan_status_compliance import DeepfenceScanStatusCompliance
from threatmapper.apis.paths.deepfence_scan_status_malware import DeepfenceScanStatusMalware
from threatmapper.apis.paths.deepfence_scan_status_secret import DeepfenceScanStatusSecret
from threatmapper.apis.paths.deepfence_scan_status_vulnerability import DeepfenceScanStatusVulnerability
from threatmapper.apis.paths.deepfence_scan_stop_compliance import DeepfenceScanStopCompliance
from threatmapper.apis.paths.deepfence_scan_stop_malware import DeepfenceScanStopMalware
from threatmapper.apis.paths.deepfence_scan_stop_secret import DeepfenceScanStopSecret
from threatmapper.apis.paths.deepfence_scan_stop_vulnerability import DeepfenceScanStopVulnerability
from threatmapper.apis.paths.deepfence_scan_scan_type_scan_id import DeepfenceScanScanTypeScanId
from threatmapper.apis.paths.deepfence_scan_scan_type_scan_id_download import DeepfenceScanScanTypeScanIdDownload
from threatmapper.apis.paths.deepfence_scans_bulk_delete import DeepfenceScansBulkDelete
from threatmapper.apis.paths.deepfence_scheduled_task import DeepfenceScheduledTask
from threatmapper.apis.paths.deepfence_scheduled_task_id import DeepfenceScheduledTaskId
from threatmapper.apis.paths.deepfence_search_cloud_accounts import DeepfenceSearchCloudAccounts
from threatmapper.apis.paths.deepfence_search_cloud_compliance_scans import DeepfenceSearchCloudComplianceScans
from threatmapper.apis.paths.deepfence_search_cloud_compliances import DeepfenceSearchCloudCompliances
from threatmapper.apis.paths.deepfence_search_cloud_resources import DeepfenceSearchCloudResources
from threatmapper.apis.paths.deepfence_search_compliance_scans import DeepfenceSearchComplianceScans
from threatmapper.apis.paths.deepfence_search_compliances import DeepfenceSearchCompliances
from threatmapper.apis.paths.deepfence_search_containers import DeepfenceSearchContainers
from threatmapper.apis.paths.deepfence_search_count_cloud_accounts import DeepfenceSearchCountCloudAccounts
from threatmapper.apis.paths.deepfence_search_count_cloud_compliance_scans import DeepfenceSearchCountCloudComplianceScans
from threatmapper.apis.paths.deepfence_search_count_cloud_compliances import DeepfenceSearchCountCloudCompliances
from threatmapper.apis.paths.deepfence_search_count_cloud_resources import DeepfenceSearchCountCloudResources
from threatmapper.apis.paths.deepfence_search_count_compliance_scans import DeepfenceSearchCountComplianceScans
from threatmapper.apis.paths.deepfence_search_count_compliances import DeepfenceSearchCountCompliances
from threatmapper.apis.paths.deepfence_search_count_containers import DeepfenceSearchCountContainers
from threatmapper.apis.paths.deepfence_search_count_hosts import DeepfenceSearchCountHosts
from threatmapper.apis.paths.deepfence_search_count_images import DeepfenceSearchCountImages
from threatmapper.apis.paths.deepfence_search_count_kubernetes_clusters import DeepfenceSearchCountKubernetesClusters
from threatmapper.apis.paths.deepfence_search_count_malware_scans import DeepfenceSearchCountMalwareScans
from threatmapper.apis.paths.deepfence_search_count_malwares import DeepfenceSearchCountMalwares
from threatmapper.apis.paths.deepfence_search_count_nodes import DeepfenceSearchCountNodes
from threatmapper.apis.paths.deepfence_search_count_pods import DeepfenceSearchCountPods
from threatmapper.apis.paths.deepfence_search_count_secret_scans import DeepfenceSearchCountSecretScans
from threatmapper.apis.paths.deepfence_search_count_secrets import DeepfenceSearchCountSecrets
from threatmapper.apis.paths.deepfence_search_count_vulnerabilities import DeepfenceSearchCountVulnerabilities
from threatmapper.apis.paths.deepfence_search_count_vulnerability_scans import DeepfenceSearchCountVulnerabilityScans
from threatmapper.apis.paths.deepfence_search_hosts import DeepfenceSearchHosts
from threatmapper.apis.paths.deepfence_search_images import DeepfenceSearchImages
from threatmapper.apis.paths.deepfence_search_kubernetes_clusters import DeepfenceSearchKubernetesClusters
from threatmapper.apis.paths.deepfence_search_malware_scans import DeepfenceSearchMalwareScans
from threatmapper.apis.paths.deepfence_search_malwares import DeepfenceSearchMalwares
from threatmapper.apis.paths.deepfence_search_pods import DeepfenceSearchPods
from threatmapper.apis.paths.deepfence_search_secret_scans import DeepfenceSearchSecretScans
from threatmapper.apis.paths.deepfence_search_secrets import DeepfenceSearchSecrets
from threatmapper.apis.paths.deepfence_search_vulnerabilities import DeepfenceSearchVulnerabilities
from threatmapper.apis.paths.deepfence_search_vulnerability_scans import DeepfenceSearchVulnerabilityScans
from threatmapper.apis.paths.deepfence_settings_email import DeepfenceSettingsEmail
from threatmapper.apis.paths.deepfence_settings_email_config_id import DeepfenceSettingsEmailConfigId
from threatmapper.apis.paths.deepfence_settings_global_settings import DeepfenceSettingsGlobalSettings
from threatmapper.apis.paths.deepfence_settings_global_settings_id import DeepfenceSettingsGlobalSettingsId
from threatmapper.apis.paths.deepfence_settings_user_activity_log import DeepfenceSettingsUserActivityLog
from threatmapper.apis.paths.deepfence_user import DeepfenceUser
from threatmapper.apis.paths.deepfence_user_invite import DeepfenceUserInvite
from threatmapper.apis.paths.deepfence_user_invite_register import DeepfenceUserInviteRegister
from threatmapper.apis.paths.deepfence_user_login import DeepfenceUserLogin
from threatmapper.apis.paths.deepfence_user_logout import DeepfenceUserLogout
from threatmapper.apis.paths.deepfence_user_password import DeepfenceUserPassword
from threatmapper.apis.paths.deepfence_user_register import DeepfenceUserRegister
from threatmapper.apis.paths.deepfence_user_reset_password_request import DeepfenceUserResetPasswordRequest
from threatmapper.apis.paths.deepfence_user_reset_password_verify import DeepfenceUserResetPasswordVerify
from threatmapper.apis.paths.deepfence_users import DeepfenceUsers
from threatmapper.apis.paths.deepfence_users_id import DeepfenceUsersId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.DEEPFENCE_APITOKEN: DeepfenceApiToken,
        PathValues.DEEPFENCE_APITOKEN_RESET: DeepfenceApiTokenReset,
        PathValues.DEEPFENCE_AUTH_TOKEN: DeepfenceAuthToken,
        PathValues.DEEPFENCE_AUTH_TOKEN_REFRESH: DeepfenceAuthTokenRefresh,
        PathValues.DEEPFENCE_CLOUDNODE_ACCOUNT: DeepfenceCloudNodeAccount,
        PathValues.DEEPFENCE_CLOUDNODE_LIST_ACCOUNTS: DeepfenceCloudNodeListAccounts,
        PathValues.DEEPFENCE_CLOUDNODE_LIST_PROVIDERS: DeepfenceCloudNodeListProviders,
        PathValues.DEEPFENCE_CONTROLS_AGENT: DeepfenceControlsAgent,
        PathValues.DEEPFENCE_CONTROLS_AGENTINIT: DeepfenceControlsAgentInit,
        PathValues.DEEPFENCE_CONTROLS_AGENTUPGRADE: DeepfenceControlsAgentUpgrade,
        PathValues.DEEPFENCE_CONTROLS_CLOUDNODE: DeepfenceControlsCloudNode,
        PathValues.DEEPFENCE_CONTROLS_CLOUDNODE_DISABLE: DeepfenceControlsCloudNodeDisable,
        PathValues.DEEPFENCE_CONTROLS_CLOUDNODE_ENABLE: DeepfenceControlsCloudNodeEnable,
        PathValues.DEEPFENCE_CONTROLS_KUBERNETESCLUSTER: DeepfenceControlsKubernetesCluster,
        PathValues.DEEPFENCE_DATABASE_VULNERABILITY: DeepfenceDatabaseVulnerability,
        PathValues.DEEPFENCE_DIAGNOSIS_AGENTLOGS: DeepfenceDiagnosisAgentLogs,
        PathValues.DEEPFENCE_DIAGNOSIS_AGENTLOGS_STATUS_NODE_ID: DeepfenceDiagnosisAgentLogsStatusNodeId,
        PathValues.DEEPFENCE_DIAGNOSIS_CONSOLELOGS: DeepfenceDiagnosisConsoleLogs,
        PathValues.DEEPFENCE_DIAGNOSIS_DIAGNOSTICLOGS: DeepfenceDiagnosisDiagnosticLogs,
        PathValues.DEEPFENCE_DIAGNOSIS_NOTIFICATION: DeepfenceDiagnosisNotification,
        PathValues.DEEPFENCE_ENDUSERLICENSEAGREEMENT: DeepfenceEndUserLicenseAgreement,
        PathValues.DEEPFENCE_FILTERS_CLOUDCOMPLIANCE: DeepfenceFiltersCloudCompliance,
        PathValues.DEEPFENCE_FILTERS_COMPLIANCE: DeepfenceFiltersCompliance,
        PathValues.DEEPFENCE_GRAPH_THREAT: DeepfenceGraphThreat,
        PathValues.DEEPFENCE_GRAPH_THREAT_VULNERABILITY: DeepfenceGraphThreatVulnerability,
        PathValues.DEEPFENCE_GRAPH_TOPOLOGY_: DeepfenceGraphTopology,
        PathValues.DEEPFENCE_GRAPH_TOPOLOGY_CONTAINERS: DeepfenceGraphTopologyContainers,
        PathValues.DEEPFENCE_GRAPH_TOPOLOGY_HOSTS: DeepfenceGraphTopologyHosts,
        PathValues.DEEPFENCE_GRAPH_TOPOLOGY_KUBERNETES: DeepfenceGraphTopologyKubernetes,
        PathValues.DEEPFENCE_GRAPH_TOPOLOGY_PODS: DeepfenceGraphTopologyPods,
        PathValues.DEEPFENCE_INGEST_CLOUDCOMPLIANCE: DeepfenceIngestCloudCompliance,
        PathValues.DEEPFENCE_INGEST_CLOUDCOMPLIANCESCANSTATUS: DeepfenceIngestCloudComplianceScanStatus,
        PathValues.DEEPFENCE_INGEST_CLOUDRESOURCES: DeepfenceIngestCloudResources,
        PathValues.DEEPFENCE_INGEST_COMPLIANCE: DeepfenceIngestCompliance,
        PathValues.DEEPFENCE_INGEST_MALWARE: DeepfenceIngestMalware,
        PathValues.DEEPFENCE_INGEST_MALWARESCANLOGS: DeepfenceIngestMalwareScanLogs,
        PathValues.DEEPFENCE_INGEST_REPORT: DeepfenceIngestReport,
        PathValues.DEEPFENCE_INGEST_SBOM: DeepfenceIngestSbom,
        PathValues.DEEPFENCE_INGEST_SECRETSCANLOGS: DeepfenceIngestSecretScanLogs,
        PathValues.DEEPFENCE_INGEST_SECRETS: DeepfenceIngestSecrets,
        PathValues.DEEPFENCE_INGEST_SYNCREPORT: DeepfenceIngestSyncReport,
        PathValues.DEEPFENCE_INGEST_VULNERABILITIES: DeepfenceIngestVulnerabilities,
        PathValues.DEEPFENCE_INGEST_VULNERABILITIESSCANLOGS: DeepfenceIngestVulnerabilitiesScanLogs,
        PathValues.DEEPFENCE_INTEGRATION: DeepfenceIntegration,
        PathValues.DEEPFENCE_INTEGRATION_INTEGRATION_ID: DeepfenceIntegrationIntegrationId,
        PathValues.DEEPFENCE_INTERNAL_CONSOLEAPITOKEN: DeepfenceInternalConsoleApiToken,
        PathValues.DEEPFENCE_LOOKUP_CLOUDRESOURCES: DeepfenceLookupCloudResources,
        PathValues.DEEPFENCE_LOOKUP_CONTAINERIMAGES: DeepfenceLookupContainerimages,
        PathValues.DEEPFENCE_LOOKUP_CONTAINERS: DeepfenceLookupContainers,
        PathValues.DEEPFENCE_LOOKUP_HOSTS: DeepfenceLookupHosts,
        PathValues.DEEPFENCE_LOOKUP_KUBERNETESCLUSTERS: DeepfenceLookupKubernetesclusters,
        PathValues.DEEPFENCE_LOOKUP_PODS: DeepfenceLookupPods,
        PathValues.DEEPFENCE_LOOKUP_PROCESSES: DeepfenceLookupProcesses,
        PathValues.DEEPFENCE_LOOKUP_REGISTRYACCOUNT: DeepfenceLookupRegistryaccount,
        PathValues.DEEPFENCE_REGISTRYACCOUNT: DeepfenceRegistryaccount,
        PathValues.DEEPFENCE_REGISTRYACCOUNT_COUNT_IMAGES: DeepfenceRegistryaccountCountImages,
        PathValues.DEEPFENCE_REGISTRYACCOUNT_COUNT_STUBS: DeepfenceRegistryaccountCountStubs,
        PathValues.DEEPFENCE_REGISTRYACCOUNT_GCR: DeepfenceRegistryaccountGcr,
        PathValues.DEEPFENCE_REGISTRYACCOUNT_IMAGES: DeepfenceRegistryaccountImages,
        PathValues.DEEPFENCE_REGISTRYACCOUNT_STUBS: DeepfenceRegistryaccountStubs,
        PathValues.DEEPFENCE_REGISTRYACCOUNT_SUMMARY: DeepfenceRegistryaccountSummary,
        PathValues.DEEPFENCE_REGISTRYACCOUNT_REGISTRY_ID: DeepfenceRegistryaccountRegistryId,
        PathValues.DEEPFENCE_REGISTRYACCOUNT_REGISTRY_ID_SUMMARY: DeepfenceRegistryaccountRegistryIdSummary,
        PathValues.DEEPFENCE_REGISTRYACCOUNT_REGISTRY_TYPE_SUMMARYBYTYPE: DeepfenceRegistryaccountRegistryTypeSummaryByType,
        PathValues.DEEPFENCE_REPORTS: DeepfenceReports,
        PathValues.DEEPFENCE_REPORTS_REPORT_ID: DeepfenceReportsReportId,
        PathValues.DEEPFENCE_SCAN_LIST_CLOUDCOMPLIANCE: DeepfenceScanListCloudCompliance,
        PathValues.DEEPFENCE_SCAN_LIST_COMPLIANCE: DeepfenceScanListCompliance,
        PathValues.DEEPFENCE_SCAN_LIST_MALWARE: DeepfenceScanListMalware,
        PathValues.DEEPFENCE_SCAN_LIST_SECRET: DeepfenceScanListSecret,
        PathValues.DEEPFENCE_SCAN_LIST_VULNERABILITY: DeepfenceScanListVulnerability,
        PathValues.DEEPFENCE_SCAN_NODESINRESULT: DeepfenceScanNodesInResult,
        PathValues.DEEPFENCE_SCAN_RESULTS_ACTION_DELETE: DeepfenceScanResultsActionDelete,
        PathValues.DEEPFENCE_SCAN_RESULTS_ACTION_MASK: DeepfenceScanResultsActionMask,
        PathValues.DEEPFENCE_SCAN_RESULTS_ACTION_NOTIFY: DeepfenceScanResultsActionNotify,
        PathValues.DEEPFENCE_SCAN_RESULTS_ACTION_UNMASK: DeepfenceScanResultsActionUnmask,
        PathValues.DEEPFENCE_SCAN_RESULTS_CLOUDCOMPLIANCE: DeepfenceScanResultsCloudCompliance,
        PathValues.DEEPFENCE_SCAN_RESULTS_COMPLIANCE: DeepfenceScanResultsCompliance,
        PathValues.DEEPFENCE_SCAN_RESULTS_COUNT_CLOUDCOMPLIANCE: DeepfenceScanResultsCountCloudCompliance,
        PathValues.DEEPFENCE_SCAN_RESULTS_COUNT_COMPLIANCE: DeepfenceScanResultsCountCompliance,
        PathValues.DEEPFENCE_SCAN_RESULTS_COUNT_GROUP_MALWARE: DeepfenceScanResultsCountGroupMalware,
        PathValues.DEEPFENCE_SCAN_RESULTS_COUNT_GROUP_MALWARE_CLASS: DeepfenceScanResultsCountGroupMalwareClass,
        PathValues.DEEPFENCE_SCAN_RESULTS_COUNT_GROUP_SECRET: DeepfenceScanResultsCountGroupSecret,
        PathValues.DEEPFENCE_SCAN_RESULTS_COUNT_MALWARE: DeepfenceScanResultsCountMalware,
        PathValues.DEEPFENCE_SCAN_RESULTS_COUNT_SECRET: DeepfenceScanResultsCountSecret,
        PathValues.DEEPFENCE_SCAN_RESULTS_COUNT_VULNERABILITY: DeepfenceScanResultsCountVulnerability,
        PathValues.DEEPFENCE_SCAN_RESULTS_MALWARE: DeepfenceScanResultsMalware,
        PathValues.DEEPFENCE_SCAN_RESULTS_MALWARE_CLASS: DeepfenceScanResultsMalwareClass,
        PathValues.DEEPFENCE_SCAN_RESULTS_MALWARE_RULES: DeepfenceScanResultsMalwareRules,
        PathValues.DEEPFENCE_SCAN_RESULTS_SECRET: DeepfenceScanResultsSecret,
        PathValues.DEEPFENCE_SCAN_RESULTS_SECRET_RULES: DeepfenceScanResultsSecretRules,
        PathValues.DEEPFENCE_SCAN_RESULTS_VULNERABILITY: DeepfenceScanResultsVulnerability,
        PathValues.DEEPFENCE_SCAN_SBOM: DeepfenceScanSbom,
        PathValues.DEEPFENCE_SCAN_SBOM_DOWNLOAD: DeepfenceScanSbomDownload,
        PathValues.DEEPFENCE_SCAN_START_COMPLIANCE: DeepfenceScanStartCompliance,
        PathValues.DEEPFENCE_SCAN_START_MALWARE: DeepfenceScanStartMalware,
        PathValues.DEEPFENCE_SCAN_START_SECRET: DeepfenceScanStartSecret,
        PathValues.DEEPFENCE_SCAN_START_VULNERABILITY: DeepfenceScanStartVulnerability,
        PathValues.DEEPFENCE_SCAN_STATUS_CLOUDCOMPLIANCE: DeepfenceScanStatusCloudCompliance,
        PathValues.DEEPFENCE_SCAN_STATUS_COMPLIANCE: DeepfenceScanStatusCompliance,
        PathValues.DEEPFENCE_SCAN_STATUS_MALWARE: DeepfenceScanStatusMalware,
        PathValues.DEEPFENCE_SCAN_STATUS_SECRET: DeepfenceScanStatusSecret,
        PathValues.DEEPFENCE_SCAN_STATUS_VULNERABILITY: DeepfenceScanStatusVulnerability,
        PathValues.DEEPFENCE_SCAN_STOP_COMPLIANCE: DeepfenceScanStopCompliance,
        PathValues.DEEPFENCE_SCAN_STOP_MALWARE: DeepfenceScanStopMalware,
        PathValues.DEEPFENCE_SCAN_STOP_SECRET: DeepfenceScanStopSecret,
        PathValues.DEEPFENCE_SCAN_STOP_VULNERABILITY: DeepfenceScanStopVulnerability,
        PathValues.DEEPFENCE_SCAN_SCAN_TYPE_SCAN_ID: DeepfenceScanScanTypeScanId,
        PathValues.DEEPFENCE_SCAN_SCAN_TYPE_SCAN_ID_DOWNLOAD: DeepfenceScanScanTypeScanIdDownload,
        PathValues.DEEPFENCE_SCANS_BULK_DELETE: DeepfenceScansBulkDelete,
        PathValues.DEEPFENCE_SCHEDULEDTASK: DeepfenceScheduledTask,
        PathValues.DEEPFENCE_SCHEDULEDTASK_ID: DeepfenceScheduledTaskId,
        PathValues.DEEPFENCE_SEARCH_CLOUDACCOUNTS: DeepfenceSearchCloudAccounts,
        PathValues.DEEPFENCE_SEARCH_CLOUDCOMPLIANCE_SCANS: DeepfenceSearchCloudComplianceScans,
        PathValues.DEEPFENCE_SEARCH_CLOUDCOMPLIANCES: DeepfenceSearchCloudCompliances,
        PathValues.DEEPFENCE_SEARCH_CLOUDRESOURCES: DeepfenceSearchCloudResources,
        PathValues.DEEPFENCE_SEARCH_COMPLIANCE_SCANS: DeepfenceSearchComplianceScans,
        PathValues.DEEPFENCE_SEARCH_COMPLIANCES: DeepfenceSearchCompliances,
        PathValues.DEEPFENCE_SEARCH_CONTAINERS: DeepfenceSearchContainers,
        PathValues.DEEPFENCE_SEARCH_COUNT_CLOUDACCOUNTS: DeepfenceSearchCountCloudAccounts,
        PathValues.DEEPFENCE_SEARCH_COUNT_CLOUDCOMPLIANCE_SCANS: DeepfenceSearchCountCloudComplianceScans,
        PathValues.DEEPFENCE_SEARCH_COUNT_CLOUDCOMPLIANCES: DeepfenceSearchCountCloudCompliances,
        PathValues.DEEPFENCE_SEARCH_COUNT_CLOUDRESOURCES: DeepfenceSearchCountCloudResources,
        PathValues.DEEPFENCE_SEARCH_COUNT_COMPLIANCE_SCANS: DeepfenceSearchCountComplianceScans,
        PathValues.DEEPFENCE_SEARCH_COUNT_COMPLIANCES: DeepfenceSearchCountCompliances,
        PathValues.DEEPFENCE_SEARCH_COUNT_CONTAINERS: DeepfenceSearchCountContainers,
        PathValues.DEEPFENCE_SEARCH_COUNT_HOSTS: DeepfenceSearchCountHosts,
        PathValues.DEEPFENCE_SEARCH_COUNT_IMAGES: DeepfenceSearchCountImages,
        PathValues.DEEPFENCE_SEARCH_COUNT_KUBERNETESCLUSTERS: DeepfenceSearchCountKubernetesClusters,
        PathValues.DEEPFENCE_SEARCH_COUNT_MALWARE_SCANS: DeepfenceSearchCountMalwareScans,
        PathValues.DEEPFENCE_SEARCH_COUNT_MALWARES: DeepfenceSearchCountMalwares,
        PathValues.DEEPFENCE_SEARCH_COUNT_NODES: DeepfenceSearchCountNodes,
        PathValues.DEEPFENCE_SEARCH_COUNT_PODS: DeepfenceSearchCountPods,
        PathValues.DEEPFENCE_SEARCH_COUNT_SECRET_SCANS: DeepfenceSearchCountSecretScans,
        PathValues.DEEPFENCE_SEARCH_COUNT_SECRETS: DeepfenceSearchCountSecrets,
        PathValues.DEEPFENCE_SEARCH_COUNT_VULNERABILITIES: DeepfenceSearchCountVulnerabilities,
        PathValues.DEEPFENCE_SEARCH_COUNT_VULNERABILITY_SCANS: DeepfenceSearchCountVulnerabilityScans,
        PathValues.DEEPFENCE_SEARCH_HOSTS: DeepfenceSearchHosts,
        PathValues.DEEPFENCE_SEARCH_IMAGES: DeepfenceSearchImages,
        PathValues.DEEPFENCE_SEARCH_KUBERNETESCLUSTERS: DeepfenceSearchKubernetesClusters,
        PathValues.DEEPFENCE_SEARCH_MALWARE_SCANS: DeepfenceSearchMalwareScans,
        PathValues.DEEPFENCE_SEARCH_MALWARES: DeepfenceSearchMalwares,
        PathValues.DEEPFENCE_SEARCH_PODS: DeepfenceSearchPods,
        PathValues.DEEPFENCE_SEARCH_SECRET_SCANS: DeepfenceSearchSecretScans,
        PathValues.DEEPFENCE_SEARCH_SECRETS: DeepfenceSearchSecrets,
        PathValues.DEEPFENCE_SEARCH_VULNERABILITIES: DeepfenceSearchVulnerabilities,
        PathValues.DEEPFENCE_SEARCH_VULNERABILITY_SCANS: DeepfenceSearchVulnerabilityScans,
        PathValues.DEEPFENCE_SETTINGS_EMAIL: DeepfenceSettingsEmail,
        PathValues.DEEPFENCE_SETTINGS_EMAIL_CONFIG_ID: DeepfenceSettingsEmailConfigId,
        PathValues.DEEPFENCE_SETTINGS_GLOBALSETTINGS: DeepfenceSettingsGlobalSettings,
        PathValues.DEEPFENCE_SETTINGS_GLOBALSETTINGS_ID: DeepfenceSettingsGlobalSettingsId,
        PathValues.DEEPFENCE_SETTINGS_USERACTIVITYLOG: DeepfenceSettingsUserActivityLog,
        PathValues.DEEPFENCE_USER: DeepfenceUser,
        PathValues.DEEPFENCE_USER_INVITE: DeepfenceUserInvite,
        PathValues.DEEPFENCE_USER_INVITE_REGISTER: DeepfenceUserInviteRegister,
        PathValues.DEEPFENCE_USER_LOGIN: DeepfenceUserLogin,
        PathValues.DEEPFENCE_USER_LOGOUT: DeepfenceUserLogout,
        PathValues.DEEPFENCE_USER_PASSWORD: DeepfenceUserPassword,
        PathValues.DEEPFENCE_USER_REGISTER: DeepfenceUserRegister,
        PathValues.DEEPFENCE_USER_RESETPASSWORD_REQUEST: DeepfenceUserResetPasswordRequest,
        PathValues.DEEPFENCE_USER_RESETPASSWORD_VERIFY: DeepfenceUserResetPasswordVerify,
        PathValues.DEEPFENCE_USERS: DeepfenceUsers,
        PathValues.DEEPFENCE_USERS_ID: DeepfenceUsersId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.DEEPFENCE_APITOKEN: DeepfenceApiToken,
        PathValues.DEEPFENCE_APITOKEN_RESET: DeepfenceApiTokenReset,
        PathValues.DEEPFENCE_AUTH_TOKEN: DeepfenceAuthToken,
        PathValues.DEEPFENCE_AUTH_TOKEN_REFRESH: DeepfenceAuthTokenRefresh,
        PathValues.DEEPFENCE_CLOUDNODE_ACCOUNT: DeepfenceCloudNodeAccount,
        PathValues.DEEPFENCE_CLOUDNODE_LIST_ACCOUNTS: DeepfenceCloudNodeListAccounts,
        PathValues.DEEPFENCE_CLOUDNODE_LIST_PROVIDERS: DeepfenceCloudNodeListProviders,
        PathValues.DEEPFENCE_CONTROLS_AGENT: DeepfenceControlsAgent,
        PathValues.DEEPFENCE_CONTROLS_AGENTINIT: DeepfenceControlsAgentInit,
        PathValues.DEEPFENCE_CONTROLS_AGENTUPGRADE: DeepfenceControlsAgentUpgrade,
        PathValues.DEEPFENCE_CONTROLS_CLOUDNODE: DeepfenceControlsCloudNode,
        PathValues.DEEPFENCE_CONTROLS_CLOUDNODE_DISABLE: DeepfenceControlsCloudNodeDisable,
        PathValues.DEEPFENCE_CONTROLS_CLOUDNODE_ENABLE: DeepfenceControlsCloudNodeEnable,
        PathValues.DEEPFENCE_CONTROLS_KUBERNETESCLUSTER: DeepfenceControlsKubernetesCluster,
        PathValues.DEEPFENCE_DATABASE_VULNERABILITY: DeepfenceDatabaseVulnerability,
        PathValues.DEEPFENCE_DIAGNOSIS_AGENTLOGS: DeepfenceDiagnosisAgentLogs,
        PathValues.DEEPFENCE_DIAGNOSIS_AGENTLOGS_STATUS_NODE_ID: DeepfenceDiagnosisAgentLogsStatusNodeId,
        PathValues.DEEPFENCE_DIAGNOSIS_CONSOLELOGS: DeepfenceDiagnosisConsoleLogs,
        PathValues.DEEPFENCE_DIAGNOSIS_DIAGNOSTICLOGS: DeepfenceDiagnosisDiagnosticLogs,
        PathValues.DEEPFENCE_DIAGNOSIS_NOTIFICATION: DeepfenceDiagnosisNotification,
        PathValues.DEEPFENCE_ENDUSERLICENSEAGREEMENT: DeepfenceEndUserLicenseAgreement,
        PathValues.DEEPFENCE_FILTERS_CLOUDCOMPLIANCE: DeepfenceFiltersCloudCompliance,
        PathValues.DEEPFENCE_FILTERS_COMPLIANCE: DeepfenceFiltersCompliance,
        PathValues.DEEPFENCE_GRAPH_THREAT: DeepfenceGraphThreat,
        PathValues.DEEPFENCE_GRAPH_THREAT_VULNERABILITY: DeepfenceGraphThreatVulnerability,
        PathValues.DEEPFENCE_GRAPH_TOPOLOGY_: DeepfenceGraphTopology,
        PathValues.DEEPFENCE_GRAPH_TOPOLOGY_CONTAINERS: DeepfenceGraphTopologyContainers,
        PathValues.DEEPFENCE_GRAPH_TOPOLOGY_HOSTS: DeepfenceGraphTopologyHosts,
        PathValues.DEEPFENCE_GRAPH_TOPOLOGY_KUBERNETES: DeepfenceGraphTopologyKubernetes,
        PathValues.DEEPFENCE_GRAPH_TOPOLOGY_PODS: DeepfenceGraphTopologyPods,
        PathValues.DEEPFENCE_INGEST_CLOUDCOMPLIANCE: DeepfenceIngestCloudCompliance,
        PathValues.DEEPFENCE_INGEST_CLOUDCOMPLIANCESCANSTATUS: DeepfenceIngestCloudComplianceScanStatus,
        PathValues.DEEPFENCE_INGEST_CLOUDRESOURCES: DeepfenceIngestCloudResources,
        PathValues.DEEPFENCE_INGEST_COMPLIANCE: DeepfenceIngestCompliance,
        PathValues.DEEPFENCE_INGEST_MALWARE: DeepfenceIngestMalware,
        PathValues.DEEPFENCE_INGEST_MALWARESCANLOGS: DeepfenceIngestMalwareScanLogs,
        PathValues.DEEPFENCE_INGEST_REPORT: DeepfenceIngestReport,
        PathValues.DEEPFENCE_INGEST_SBOM: DeepfenceIngestSbom,
        PathValues.DEEPFENCE_INGEST_SECRETSCANLOGS: DeepfenceIngestSecretScanLogs,
        PathValues.DEEPFENCE_INGEST_SECRETS: DeepfenceIngestSecrets,
        PathValues.DEEPFENCE_INGEST_SYNCREPORT: DeepfenceIngestSyncReport,
        PathValues.DEEPFENCE_INGEST_VULNERABILITIES: DeepfenceIngestVulnerabilities,
        PathValues.DEEPFENCE_INGEST_VULNERABILITIESSCANLOGS: DeepfenceIngestVulnerabilitiesScanLogs,
        PathValues.DEEPFENCE_INTEGRATION: DeepfenceIntegration,
        PathValues.DEEPFENCE_INTEGRATION_INTEGRATION_ID: DeepfenceIntegrationIntegrationId,
        PathValues.DEEPFENCE_INTERNAL_CONSOLEAPITOKEN: DeepfenceInternalConsoleApiToken,
        PathValues.DEEPFENCE_LOOKUP_CLOUDRESOURCES: DeepfenceLookupCloudResources,
        PathValues.DEEPFENCE_LOOKUP_CONTAINERIMAGES: DeepfenceLookupContainerimages,
        PathValues.DEEPFENCE_LOOKUP_CONTAINERS: DeepfenceLookupContainers,
        PathValues.DEEPFENCE_LOOKUP_HOSTS: DeepfenceLookupHosts,
        PathValues.DEEPFENCE_LOOKUP_KUBERNETESCLUSTERS: DeepfenceLookupKubernetesclusters,
        PathValues.DEEPFENCE_LOOKUP_PODS: DeepfenceLookupPods,
        PathValues.DEEPFENCE_LOOKUP_PROCESSES: DeepfenceLookupProcesses,
        PathValues.DEEPFENCE_LOOKUP_REGISTRYACCOUNT: DeepfenceLookupRegistryaccount,
        PathValues.DEEPFENCE_REGISTRYACCOUNT: DeepfenceRegistryaccount,
        PathValues.DEEPFENCE_REGISTRYACCOUNT_COUNT_IMAGES: DeepfenceRegistryaccountCountImages,
        PathValues.DEEPFENCE_REGISTRYACCOUNT_COUNT_STUBS: DeepfenceRegistryaccountCountStubs,
        PathValues.DEEPFENCE_REGISTRYACCOUNT_GCR: DeepfenceRegistryaccountGcr,
        PathValues.DEEPFENCE_REGISTRYACCOUNT_IMAGES: DeepfenceRegistryaccountImages,
        PathValues.DEEPFENCE_REGISTRYACCOUNT_STUBS: DeepfenceRegistryaccountStubs,
        PathValues.DEEPFENCE_REGISTRYACCOUNT_SUMMARY: DeepfenceRegistryaccountSummary,
        PathValues.DEEPFENCE_REGISTRYACCOUNT_REGISTRY_ID: DeepfenceRegistryaccountRegistryId,
        PathValues.DEEPFENCE_REGISTRYACCOUNT_REGISTRY_ID_SUMMARY: DeepfenceRegistryaccountRegistryIdSummary,
        PathValues.DEEPFENCE_REGISTRYACCOUNT_REGISTRY_TYPE_SUMMARYBYTYPE: DeepfenceRegistryaccountRegistryTypeSummaryByType,
        PathValues.DEEPFENCE_REPORTS: DeepfenceReports,
        PathValues.DEEPFENCE_REPORTS_REPORT_ID: DeepfenceReportsReportId,
        PathValues.DEEPFENCE_SCAN_LIST_CLOUDCOMPLIANCE: DeepfenceScanListCloudCompliance,
        PathValues.DEEPFENCE_SCAN_LIST_COMPLIANCE: DeepfenceScanListCompliance,
        PathValues.DEEPFENCE_SCAN_LIST_MALWARE: DeepfenceScanListMalware,
        PathValues.DEEPFENCE_SCAN_LIST_SECRET: DeepfenceScanListSecret,
        PathValues.DEEPFENCE_SCAN_LIST_VULNERABILITY: DeepfenceScanListVulnerability,
        PathValues.DEEPFENCE_SCAN_NODESINRESULT: DeepfenceScanNodesInResult,
        PathValues.DEEPFENCE_SCAN_RESULTS_ACTION_DELETE: DeepfenceScanResultsActionDelete,
        PathValues.DEEPFENCE_SCAN_RESULTS_ACTION_MASK: DeepfenceScanResultsActionMask,
        PathValues.DEEPFENCE_SCAN_RESULTS_ACTION_NOTIFY: DeepfenceScanResultsActionNotify,
        PathValues.DEEPFENCE_SCAN_RESULTS_ACTION_UNMASK: DeepfenceScanResultsActionUnmask,
        PathValues.DEEPFENCE_SCAN_RESULTS_CLOUDCOMPLIANCE: DeepfenceScanResultsCloudCompliance,
        PathValues.DEEPFENCE_SCAN_RESULTS_COMPLIANCE: DeepfenceScanResultsCompliance,
        PathValues.DEEPFENCE_SCAN_RESULTS_COUNT_CLOUDCOMPLIANCE: DeepfenceScanResultsCountCloudCompliance,
        PathValues.DEEPFENCE_SCAN_RESULTS_COUNT_COMPLIANCE: DeepfenceScanResultsCountCompliance,
        PathValues.DEEPFENCE_SCAN_RESULTS_COUNT_GROUP_MALWARE: DeepfenceScanResultsCountGroupMalware,
        PathValues.DEEPFENCE_SCAN_RESULTS_COUNT_GROUP_MALWARE_CLASS: DeepfenceScanResultsCountGroupMalwareClass,
        PathValues.DEEPFENCE_SCAN_RESULTS_COUNT_GROUP_SECRET: DeepfenceScanResultsCountGroupSecret,
        PathValues.DEEPFENCE_SCAN_RESULTS_COUNT_MALWARE: DeepfenceScanResultsCountMalware,
        PathValues.DEEPFENCE_SCAN_RESULTS_COUNT_SECRET: DeepfenceScanResultsCountSecret,
        PathValues.DEEPFENCE_SCAN_RESULTS_COUNT_VULNERABILITY: DeepfenceScanResultsCountVulnerability,
        PathValues.DEEPFENCE_SCAN_RESULTS_MALWARE: DeepfenceScanResultsMalware,
        PathValues.DEEPFENCE_SCAN_RESULTS_MALWARE_CLASS: DeepfenceScanResultsMalwareClass,
        PathValues.DEEPFENCE_SCAN_RESULTS_MALWARE_RULES: DeepfenceScanResultsMalwareRules,
        PathValues.DEEPFENCE_SCAN_RESULTS_SECRET: DeepfenceScanResultsSecret,
        PathValues.DEEPFENCE_SCAN_RESULTS_SECRET_RULES: DeepfenceScanResultsSecretRules,
        PathValues.DEEPFENCE_SCAN_RESULTS_VULNERABILITY: DeepfenceScanResultsVulnerability,
        PathValues.DEEPFENCE_SCAN_SBOM: DeepfenceScanSbom,
        PathValues.DEEPFENCE_SCAN_SBOM_DOWNLOAD: DeepfenceScanSbomDownload,
        PathValues.DEEPFENCE_SCAN_START_COMPLIANCE: DeepfenceScanStartCompliance,
        PathValues.DEEPFENCE_SCAN_START_MALWARE: DeepfenceScanStartMalware,
        PathValues.DEEPFENCE_SCAN_START_SECRET: DeepfenceScanStartSecret,
        PathValues.DEEPFENCE_SCAN_START_VULNERABILITY: DeepfenceScanStartVulnerability,
        PathValues.DEEPFENCE_SCAN_STATUS_CLOUDCOMPLIANCE: DeepfenceScanStatusCloudCompliance,
        PathValues.DEEPFENCE_SCAN_STATUS_COMPLIANCE: DeepfenceScanStatusCompliance,
        PathValues.DEEPFENCE_SCAN_STATUS_MALWARE: DeepfenceScanStatusMalware,
        PathValues.DEEPFENCE_SCAN_STATUS_SECRET: DeepfenceScanStatusSecret,
        PathValues.DEEPFENCE_SCAN_STATUS_VULNERABILITY: DeepfenceScanStatusVulnerability,
        PathValues.DEEPFENCE_SCAN_STOP_COMPLIANCE: DeepfenceScanStopCompliance,
        PathValues.DEEPFENCE_SCAN_STOP_MALWARE: DeepfenceScanStopMalware,
        PathValues.DEEPFENCE_SCAN_STOP_SECRET: DeepfenceScanStopSecret,
        PathValues.DEEPFENCE_SCAN_STOP_VULNERABILITY: DeepfenceScanStopVulnerability,
        PathValues.DEEPFENCE_SCAN_SCAN_TYPE_SCAN_ID: DeepfenceScanScanTypeScanId,
        PathValues.DEEPFENCE_SCAN_SCAN_TYPE_SCAN_ID_DOWNLOAD: DeepfenceScanScanTypeScanIdDownload,
        PathValues.DEEPFENCE_SCANS_BULK_DELETE: DeepfenceScansBulkDelete,
        PathValues.DEEPFENCE_SCHEDULEDTASK: DeepfenceScheduledTask,
        PathValues.DEEPFENCE_SCHEDULEDTASK_ID: DeepfenceScheduledTaskId,
        PathValues.DEEPFENCE_SEARCH_CLOUDACCOUNTS: DeepfenceSearchCloudAccounts,
        PathValues.DEEPFENCE_SEARCH_CLOUDCOMPLIANCE_SCANS: DeepfenceSearchCloudComplianceScans,
        PathValues.DEEPFENCE_SEARCH_CLOUDCOMPLIANCES: DeepfenceSearchCloudCompliances,
        PathValues.DEEPFENCE_SEARCH_CLOUDRESOURCES: DeepfenceSearchCloudResources,
        PathValues.DEEPFENCE_SEARCH_COMPLIANCE_SCANS: DeepfenceSearchComplianceScans,
        PathValues.DEEPFENCE_SEARCH_COMPLIANCES: DeepfenceSearchCompliances,
        PathValues.DEEPFENCE_SEARCH_CONTAINERS: DeepfenceSearchContainers,
        PathValues.DEEPFENCE_SEARCH_COUNT_CLOUDACCOUNTS: DeepfenceSearchCountCloudAccounts,
        PathValues.DEEPFENCE_SEARCH_COUNT_CLOUDCOMPLIANCE_SCANS: DeepfenceSearchCountCloudComplianceScans,
        PathValues.DEEPFENCE_SEARCH_COUNT_CLOUDCOMPLIANCES: DeepfenceSearchCountCloudCompliances,
        PathValues.DEEPFENCE_SEARCH_COUNT_CLOUDRESOURCES: DeepfenceSearchCountCloudResources,
        PathValues.DEEPFENCE_SEARCH_COUNT_COMPLIANCE_SCANS: DeepfenceSearchCountComplianceScans,
        PathValues.DEEPFENCE_SEARCH_COUNT_COMPLIANCES: DeepfenceSearchCountCompliances,
        PathValues.DEEPFENCE_SEARCH_COUNT_CONTAINERS: DeepfenceSearchCountContainers,
        PathValues.DEEPFENCE_SEARCH_COUNT_HOSTS: DeepfenceSearchCountHosts,
        PathValues.DEEPFENCE_SEARCH_COUNT_IMAGES: DeepfenceSearchCountImages,
        PathValues.DEEPFENCE_SEARCH_COUNT_KUBERNETESCLUSTERS: DeepfenceSearchCountKubernetesClusters,
        PathValues.DEEPFENCE_SEARCH_COUNT_MALWARE_SCANS: DeepfenceSearchCountMalwareScans,
        PathValues.DEEPFENCE_SEARCH_COUNT_MALWARES: DeepfenceSearchCountMalwares,
        PathValues.DEEPFENCE_SEARCH_COUNT_NODES: DeepfenceSearchCountNodes,
        PathValues.DEEPFENCE_SEARCH_COUNT_PODS: DeepfenceSearchCountPods,
        PathValues.DEEPFENCE_SEARCH_COUNT_SECRET_SCANS: DeepfenceSearchCountSecretScans,
        PathValues.DEEPFENCE_SEARCH_COUNT_SECRETS: DeepfenceSearchCountSecrets,
        PathValues.DEEPFENCE_SEARCH_COUNT_VULNERABILITIES: DeepfenceSearchCountVulnerabilities,
        PathValues.DEEPFENCE_SEARCH_COUNT_VULNERABILITY_SCANS: DeepfenceSearchCountVulnerabilityScans,
        PathValues.DEEPFENCE_SEARCH_HOSTS: DeepfenceSearchHosts,
        PathValues.DEEPFENCE_SEARCH_IMAGES: DeepfenceSearchImages,
        PathValues.DEEPFENCE_SEARCH_KUBERNETESCLUSTERS: DeepfenceSearchKubernetesClusters,
        PathValues.DEEPFENCE_SEARCH_MALWARE_SCANS: DeepfenceSearchMalwareScans,
        PathValues.DEEPFENCE_SEARCH_MALWARES: DeepfenceSearchMalwares,
        PathValues.DEEPFENCE_SEARCH_PODS: DeepfenceSearchPods,
        PathValues.DEEPFENCE_SEARCH_SECRET_SCANS: DeepfenceSearchSecretScans,
        PathValues.DEEPFENCE_SEARCH_SECRETS: DeepfenceSearchSecrets,
        PathValues.DEEPFENCE_SEARCH_VULNERABILITIES: DeepfenceSearchVulnerabilities,
        PathValues.DEEPFENCE_SEARCH_VULNERABILITY_SCANS: DeepfenceSearchVulnerabilityScans,
        PathValues.DEEPFENCE_SETTINGS_EMAIL: DeepfenceSettingsEmail,
        PathValues.DEEPFENCE_SETTINGS_EMAIL_CONFIG_ID: DeepfenceSettingsEmailConfigId,
        PathValues.DEEPFENCE_SETTINGS_GLOBALSETTINGS: DeepfenceSettingsGlobalSettings,
        PathValues.DEEPFENCE_SETTINGS_GLOBALSETTINGS_ID: DeepfenceSettingsGlobalSettingsId,
        PathValues.DEEPFENCE_SETTINGS_USERACTIVITYLOG: DeepfenceSettingsUserActivityLog,
        PathValues.DEEPFENCE_USER: DeepfenceUser,
        PathValues.DEEPFENCE_USER_INVITE: DeepfenceUserInvite,
        PathValues.DEEPFENCE_USER_INVITE_REGISTER: DeepfenceUserInviteRegister,
        PathValues.DEEPFENCE_USER_LOGIN: DeepfenceUserLogin,
        PathValues.DEEPFENCE_USER_LOGOUT: DeepfenceUserLogout,
        PathValues.DEEPFENCE_USER_PASSWORD: DeepfenceUserPassword,
        PathValues.DEEPFENCE_USER_REGISTER: DeepfenceUserRegister,
        PathValues.DEEPFENCE_USER_RESETPASSWORD_REQUEST: DeepfenceUserResetPasswordRequest,
        PathValues.DEEPFENCE_USER_RESETPASSWORD_VERIFY: DeepfenceUserResetPasswordVerify,
        PathValues.DEEPFENCE_USERS: DeepfenceUsers,
        PathValues.DEEPFENCE_USERS_ID: DeepfenceUsersId,
    }
)
