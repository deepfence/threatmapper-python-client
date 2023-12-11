""" Contains all the data models used in inputs/outputs """

from .api_docs_bad_request_response import ApiDocsBadRequestResponse
from .api_docs_bad_request_response_error_fields import ApiDocsBadRequestResponseErrorFields
from .api_docs_bad_request_response_error_index import ApiDocsBadRequestResponseErrorIndex
from .api_docs_failure_response import ApiDocsFailureResponse
from .completion_completion_node_field_req import CompletionCompletionNodeFieldReq
from .completion_completion_node_field_res import CompletionCompletionNodeFieldRes
from .controls_action import ControlsAction
from .controls_agent_beat import ControlsAgentBeat
from .controls_agent_controls import ControlsAgentControls
from .delete_scan_results_for_scan_id_scan_type import DeleteScanResultsForScanIDScanType
from .detailed_connection_summary import DetailedConnectionSummary
from .detailed_node_summaries import DetailedNodeSummaries
from .detailed_node_summary import DetailedNodeSummary
from .detailed_topology_connection_summaries import DetailedTopologyConnectionSummaries
from .diagnosis_diagnostic_logs_link import DiagnosisDiagnosticLogsLink
from .diagnosis_diagnostic_logs_status import DiagnosisDiagnosticLogsStatus
from .diagnosis_diagnostic_notification import DiagnosisDiagnosticNotification
from .diagnosis_generate_agent_diagnostic_logs_request import DiagnosisGenerateAgentDiagnosticLogsRequest
from .diagnosis_generate_cloud_scanner_diagnostic_logs_request import DiagnosisGenerateCloudScannerDiagnosticLogsRequest
from .diagnosis_generate_console_diagnostic_logs_request import DiagnosisGenerateConsoleDiagnosticLogsRequest
from .diagnosis_get_diagnostic_logs_response import DiagnosisGetDiagnosticLogsResponse
from .diagnosis_node_identifier import DiagnosisNodeIdentifier
from .diagnosis_node_identifier_node_type import DiagnosisNodeIdentifierNodeType
from .download_scan_results_scan_type import DownloadScanResultsScanType
from .form_data_model_registry_gcr_add_req import FormDataModelRegistryGCRAddReq
from .form_data_vulnerability_db_db_upload_request import FormDataVulnerabilityDbDBUploadRequest
from .graph_cloud_provider_filter import GraphCloudProviderFilter
from .graph_individual_threat_graph import GraphIndividualThreatGraph
from .graph_individual_threat_graph_request import GraphIndividualThreatGraphRequest
from .graph_individual_threat_graph_request_graph_type import GraphIndividualThreatGraphRequestGraphType
from .graph_individual_threat_graph_request_issue_type import GraphIndividualThreatGraphRequestIssueType
from .graph_node_info import GraphNodeInfo
from .graph_provider_threat_graph import GraphProviderThreatGraph
from .graph_threat_filters import GraphThreatFilters
from .graph_threat_filters_type import GraphThreatFiltersType
from .graph_threat_graph import GraphThreatGraph
from .graph_threat_node_info import GraphThreatNodeInfo
from .graph_threat_node_info_nodes import GraphThreatNodeInfoNodes
from .graph_topology_filters import GraphTopologyFilters
from .ingesters_cloud_compliance import IngestersCloudCompliance
from .ingesters_cloud_compliance_scan_status import IngestersCloudComplianceScanStatus
from .ingesters_cloud_resource import IngestersCloudResource
from .ingesters_compliance import IngestersCompliance
from .ingesters_compliance_scan_status import IngestersComplianceScanStatus
from .ingesters_compliance_stats import IngestersComplianceStats
from .ingesters_malware import IngestersMalware
from .ingesters_malware_scan_status import IngestersMalwareScanStatus
from .ingesters_meta_rules import IngestersMetaRules
from .ingesters_report_ingestion_data import IngestersReportIngestionData
from .ingesters_report_ingestion_data_container_batch_item import IngestersReportIngestionDataContainerBatchItem
from .ingesters_report_ingestion_data_container_edges_batch_item import (
    IngestersReportIngestionDataContainerEdgesBatchItem,
)
from .ingesters_report_ingestion_data_container_image_batch_item import (
    IngestersReportIngestionDataContainerImageBatchItem,
)
from .ingesters_report_ingestion_data_container_image_edge_batch_item import (
    IngestersReportIngestionDataContainerImageEdgeBatchItem,
)
from .ingesters_report_ingestion_data_container_process_edge_batch_item import (
    IngestersReportIngestionDataContainerProcessEdgeBatchItem,
)
from .ingesters_report_ingestion_data_endpoint_edges_batch_item import (
    IngestersReportIngestionDataEndpointEdgesBatchItem,
)
from .ingesters_report_ingestion_data_host_batch_item import IngestersReportIngestionDataHostBatchItem
from .ingesters_report_ingestion_data_hosts_item import IngestersReportIngestionDataHostsItem
from .ingesters_report_ingestion_data_kubernetes_cluster_batch_item import (
    IngestersReportIngestionDataKubernetesClusterBatchItem,
)
from .ingesters_report_ingestion_data_kubernetes_cluster_edge_batch_item import (
    IngestersReportIngestionDataKubernetesClusterEdgeBatchItem,
)
from .ingesters_report_ingestion_data_pod_batch_item import IngestersReportIngestionDataPodBatchItem
from .ingesters_report_ingestion_data_pod_edges_batch_item import IngestersReportIngestionDataPodEdgesBatchItem
from .ingesters_report_ingestion_data_pod_host_edges_batch_item import IngestersReportIngestionDataPodHostEdgesBatchItem
from .ingesters_report_ingestion_data_process_batch_item import IngestersReportIngestionDataProcessBatchItem
from .ingesters_report_ingestion_data_process_edges_batch_item import IngestersReportIngestionDataProcessEdgesBatchItem
from .ingesters_secret import IngestersSecret
from .ingesters_secret_match import IngestersSecretMatch
from .ingesters_secret_rule import IngestersSecretRule
from .ingesters_secret_scan_status import IngestersSecretScanStatus
from .ingesters_secret_severity import IngestersSecretSeverity
from .ingesters_vulnerability import IngestersVulnerability
from .ingesters_vulnerability_scan_status import IngestersVulnerabilityScanStatus
from .lookup_lookup_filter import LookupLookupFilter
from .model_add_scheduled_task_request import ModelAddScheduledTaskRequest
from .model_agent_id import ModelAgentId
from .model_agent_plugin_disable import ModelAgentPluginDisable
from .model_agent_plugin_enable import ModelAgentPluginEnable
from .model_agent_upgrade import ModelAgentUpgrade
from .model_api_auth_request import ModelApiAuthRequest
from .model_api_token_response import ModelApiTokenResponse
from .model_basic_node import ModelBasicNode
from .model_bulk_delete_scans_request import ModelBulkDeleteScansRequest
from .model_bulk_delete_scans_request_scan_type import ModelBulkDeleteScansRequestScanType
from .model_cloud_compliance import ModelCloudCompliance
from .model_cloud_compliance_benchmark import ModelCloudComplianceBenchmark
from .model_cloud_compliance_scan_details import ModelCloudComplianceScanDetails
from .model_cloud_compliance_scan_result import ModelCloudComplianceScanResult
from .model_cloud_compliance_scan_result_status_counts import ModelCloudComplianceScanResultStatusCounts
from .model_cloud_node_account_info import ModelCloudNodeAccountInfo
from .model_cloud_node_account_info_scan_status_map import ModelCloudNodeAccountInfoScanStatusMap
from .model_cloud_node_account_register_req import ModelCloudNodeAccountRegisterReq
from .model_cloud_node_account_register_req_cloud_provider import ModelCloudNodeAccountRegisterReqCloudProvider
from .model_cloud_node_account_register_req_monitored_account_ids import (
    ModelCloudNodeAccountRegisterReqMonitoredAccountIds,
)
from .model_cloud_node_account_register_resp import ModelCloudNodeAccountRegisterResp
from .model_cloud_node_account_register_resp_data import ModelCloudNodeAccountRegisterRespData
from .model_cloud_node_account_register_resp_data_scans import ModelCloudNodeAccountRegisterRespDataScans
from .model_cloud_node_accounts_list_req import ModelCloudNodeAccountsListReq
from .model_cloud_node_accounts_list_resp import ModelCloudNodeAccountsListResp
from .model_cloud_node_cloudtrail_trail import ModelCloudNodeCloudtrailTrail
from .model_cloud_node_compliance_control import ModelCloudNodeComplianceControl
from .model_cloud_node_control_req import ModelCloudNodeControlReq
from .model_cloud_node_control_req_cloud_provider import ModelCloudNodeControlReqCloudProvider
from .model_cloud_node_control_resp import ModelCloudNodeControlResp
from .model_cloud_node_enable_disable_req import ModelCloudNodeEnableDisableReq
from .model_cloud_node_providers_list_resp import ModelCloudNodeProvidersListResp
from .model_cloud_resource import ModelCloudResource
from .model_compliance import ModelCompliance
from .model_compliance_rule import ModelComplianceRule
from .model_compliance_scan_info import ModelComplianceScanInfo
from .model_compliance_scan_info_severity_counts import ModelComplianceScanInfoSeverityCounts
from .model_compliance_scan_result import ModelComplianceScanResult
from .model_compliance_scan_result_status_counts import ModelComplianceScanResultStatusCounts
from .model_compliance_scan_status_resp import ModelComplianceScanStatusResp
from .model_compliance_scan_trigger_req import ModelComplianceScanTriggerReq
from .model_connection import ModelConnection
from .model_container import ModelContainer
from .model_container_docker_labels import ModelContainerDockerLabels
from .model_container_image import ModelContainerImage
from .model_container_image_metadata import ModelContainerImageMetadata
from .model_download_report_response import ModelDownloadReportResponse
from .model_download_scan_results_response import ModelDownloadScanResultsResponse
from .model_email_configuration_add import ModelEmailConfigurationAdd
from .model_email_configuration_resp import ModelEmailConfigurationResp
from .model_export_report import ModelExportReport
from .model_fetch_window import ModelFetchWindow
from .model_filters_req import ModelFiltersReq
from .model_filters_req_having import ModelFiltersReqHaving
from .model_filters_result import ModelFiltersResult
from .model_filters_result_filters import ModelFiltersResultFilters
from .model_generate_report_req import ModelGenerateReportReq
from .model_generate_report_req_duration import ModelGenerateReportReqDuration
from .model_generate_report_req_report_type import ModelGenerateReportReqReportType
from .model_generate_report_resp import ModelGenerateReportResp
from .model_get_audit_logs_request import ModelGetAuditLogsRequest
from .model_graph_result import ModelGraphResult
from .model_graph_result_edges import ModelGraphResultEdges
from .model_graph_result_nodes import ModelGraphResultNodes
from .model_host import ModelHost
from .model_image_stub import ModelImageStub
from .model_init_agent_req import ModelInitAgentReq
from .model_integration_add_req import ModelIntegrationAddReq
from .model_integration_add_req_config import ModelIntegrationAddReqConfig
from .model_integration_filters import ModelIntegrationFilters
from .model_integration_list_resp import ModelIntegrationListResp
from .model_integration_list_resp_config import ModelIntegrationListRespConfig
from .model_invite_user_request import ModelInviteUserRequest
from .model_invite_user_request_action import ModelInviteUserRequestAction
from .model_invite_user_request_role import ModelInviteUserRequestRole
from .model_invite_user_response import ModelInviteUserResponse
from .model_kubernetes_cluster import ModelKubernetesCluster
from .model_login_request import ModelLoginRequest
from .model_login_response import ModelLoginResponse
from .model_malware import ModelMalware
from .model_malware_rule import ModelMalwareRule
from .model_malware_scan_result import ModelMalwareScanResult
from .model_malware_scan_result_class import ModelMalwareScanResultClass
from .model_malware_scan_result_rules import ModelMalwareScanResultRules
from .model_malware_scan_result_severity_counts import ModelMalwareScanResultSeverityCounts
from .model_malware_scan_trigger_req import ModelMalwareScanTriggerReq
from .model_message_response import ModelMessageResponse
from .model_metadata import ModelMetadata
from .model_node_identifier import ModelNodeIdentifier
from .model_node_identifier_node_type import ModelNodeIdentifierNodeType
from .model_nodes_in_scan_result_request import ModelNodesInScanResultRequest
from .model_nodes_in_scan_result_request_scan_type import ModelNodesInScanResultRequestScanType
from .model_password_reset_request import ModelPasswordResetRequest
from .model_password_reset_verify_request import ModelPasswordResetVerifyRequest
from .model_pod import ModelPod
from .model_pod_kubernetes_labels import ModelPodKubernetesLabels
from .model_posture_provider import ModelPostureProvider
from .model_process import ModelProcess
from .model_register_invited_user_request import ModelRegisterInvitedUserRequest
from .model_registry_account import ModelRegistryAccount
from .model_registry_add_req import ModelRegistryAddReq
from .model_registry_add_req_extras import ModelRegistryAddReqExtras
from .model_registry_add_req_non_secret import ModelRegistryAddReqNonSecret
from .model_registry_add_req_secret import ModelRegistryAddReqSecret
from .model_registry_count_resp import ModelRegistryCountResp
from .model_registry_image_stubs_req import ModelRegistryImageStubsReq
from .model_registry_images_req import ModelRegistryImagesReq
from .model_registry_list_resp import ModelRegistryListResp
from .model_registry_summary_all_resp import ModelRegistrySummaryAllResp
from .model_registry_update_req import ModelRegistryUpdateReq
from .model_registry_update_req_extras import ModelRegistryUpdateReqExtras
from .model_registry_update_req_non_secret import ModelRegistryUpdateReqNonSecret
from .model_registry_update_req_secret import ModelRegistryUpdateReqSecret
from .model_response_access_token import ModelResponseAccessToken
from .model_sbom_request import ModelSbomRequest
from .model_sbom_response import ModelSbomResponse
from .model_scan_compare_req import ModelScanCompareReq
from .model_scan_compare_res_github_com_deepfence_threat_mapper_deepfence_server_model_cloud_compliance import (
    ModelScanCompareResGithubComDeepfenceThreatMapperDeepfenceServerModelCloudCompliance,
)
from .model_scan_compare_res_github_com_deepfence_threat_mapper_deepfence_server_model_compliance import (
    ModelScanCompareResGithubComDeepfenceThreatMapperDeepfenceServerModelCompliance,
)
from .model_scan_compare_res_github_com_deepfence_threat_mapper_deepfence_server_model_malware import (
    ModelScanCompareResGithubComDeepfenceThreatMapperDeepfenceServerModelMalware,
)
from .model_scan_compare_res_github_com_deepfence_threat_mapper_deepfence_server_model_secret import (
    ModelScanCompareResGithubComDeepfenceThreatMapperDeepfenceServerModelSecret,
)
from .model_scan_compare_res_github_com_deepfence_threat_mapper_deepfence_server_model_vulnerability import (
    ModelScanCompareResGithubComDeepfenceThreatMapperDeepfenceServerModelVulnerability,
)
from .model_scan_filter import ModelScanFilter
from .model_scan_info import ModelScanInfo
from .model_scan_info_severity_counts import ModelScanInfoSeverityCounts
from .model_scan_list_req import ModelScanListReq
from .model_scan_list_resp import ModelScanListResp
from .model_scan_report_fields_response import ModelScanReportFieldsResponse
from .model_scan_result_basic_node import ModelScanResultBasicNode
from .model_scan_results_action_request import ModelScanResultsActionRequest
from .model_scan_results_action_request_scan_type import ModelScanResultsActionRequestScanType
from .model_scan_results_common import ModelScanResultsCommon
from .model_scan_results_mask_request import ModelScanResultsMaskRequest
from .model_scan_results_mask_request_mask_action import ModelScanResultsMaskRequestMaskAction
from .model_scan_results_mask_request_scan_type import ModelScanResultsMaskRequestScanType
from .model_scan_results_req import ModelScanResultsReq
from .model_scan_status_req import ModelScanStatusReq
from .model_scan_status_resp import ModelScanStatusResp
from .model_scan_status_resp_statuses import ModelScanStatusRespStatuses
from .model_scan_trigger_resp import ModelScanTriggerResp
from .model_secret import ModelSecret
from .model_secret_rule import ModelSecretRule
from .model_secret_scan_result import ModelSecretScanResult
from .model_secret_scan_result_rules import ModelSecretScanResultRules
from .model_secret_scan_result_severity_counts import ModelSecretScanResultSeverityCounts
from .model_secret_scan_trigger_req import ModelSecretScanTriggerReq
from .model_setting_update_request import ModelSettingUpdateRequest
from .model_setting_update_request_key import ModelSettingUpdateRequestKey
from .model_settings_response import ModelSettingsResponse
from .model_stop_scan_request import ModelStopScanRequest
from .model_stop_scan_request_scan_type import ModelStopScanRequestScanType
from .model_summary import ModelSummary
from .model_topology_delta_req import ModelTopologyDeltaReq
from .model_topology_delta_response import ModelTopologyDeltaResponse
from .model_update_scheduled_task_request import ModelUpdateScheduledTaskRequest
from .model_update_user_id_request import ModelUpdateUserIdRequest
from .model_update_user_id_request_role import ModelUpdateUserIdRequestRole
from .model_update_user_password_request import ModelUpdateUserPasswordRequest
from .model_update_user_request import ModelUpdateUserRequest
from .model_update_user_request_role import ModelUpdateUserRequestRole
from .model_user import ModelUser
from .model_user_groups import ModelUserGroups
from .model_user_register_request import ModelUserRegisterRequest
from .model_user_role import ModelUserRole
from .model_vulnerability import ModelVulnerability
from .model_vulnerability_rule import ModelVulnerabilityRule
from .model_vulnerability_scan_config_language import ModelVulnerabilityScanConfigLanguage
from .model_vulnerability_scan_config_language_language import ModelVulnerabilityScanConfigLanguageLanguage
from .model_vulnerability_scan_result import ModelVulnerabilityScanResult
from .model_vulnerability_scan_result_severity_counts import ModelVulnerabilityScanResultSeverityCounts
from .model_vulnerability_scan_trigger_req import ModelVulnerabilityScanTriggerReq
from .postgresql_db_get_audit_logs_row import PostgresqlDbGetAuditLogsRow
from .postgresql_db_scheduler import PostgresqlDbScheduler
from .postgresql_db_scheduler_last_ran_at import PostgresqlDbSchedulerLastRanAt
from .report_metadata import ReportMetadata
from .report_raw_report import ReportRawReport
from .reporters_compare_filter import ReportersCompareFilter
from .reporters_contains_filter import ReportersContainsFilter
from .reporters_contains_filter_filter_in import ReportersContainsFilterFilterIn
from .reporters_fields_filters import ReportersFieldsFilters
from .reporters_match_filter import ReportersMatchFilter
from .reporters_match_filter_filter_in import ReportersMatchFilterFilterIn
from .reporters_order_filter import ReportersOrderFilter
from .reporters_order_spec import ReportersOrderSpec
from .search_chained_search_filter import SearchChainedSearchFilter
from .search_node_count_resp import SearchNodeCountResp
from .search_result_group import SearchResultGroup
from .search_result_group_resp import SearchResultGroupResp
from .search_search_count_resp import SearchSearchCountResp
from .search_search_count_resp_categories import SearchSearchCountRespCategories
from .search_search_filter import SearchSearchFilter
from .search_search_node_req import SearchSearchNodeReq
from .search_search_scan_req import SearchSearchScanReq
from .sql_null_time import SqlNullTime
from .utils_advanced_report_filters import UtilsAdvancedReportFilters
from .utils_report_filters import UtilsReportFilters
from .utils_report_filters_node_type import UtilsReportFiltersNodeType
from .utils_report_filters_scan_type import UtilsReportFiltersScanType
from .utils_report_filters_severity_or_check_type import UtilsReportFiltersSeverityOrCheckType
from .utils_scan_sbom_request import UtilsScanSbomRequest

__all__ = (
    "ApiDocsBadRequestResponse",
    "ApiDocsBadRequestResponseErrorFields",
    "ApiDocsBadRequestResponseErrorIndex",
    "ApiDocsFailureResponse",
    "CompletionCompletionNodeFieldReq",
    "CompletionCompletionNodeFieldRes",
    "ControlsAction",
    "ControlsAgentBeat",
    "ControlsAgentControls",
    "DeleteScanResultsForScanIDScanType",
    "DetailedConnectionSummary",
    "DetailedNodeSummaries",
    "DetailedNodeSummary",
    "DetailedTopologyConnectionSummaries",
    "DiagnosisDiagnosticLogsLink",
    "DiagnosisDiagnosticLogsStatus",
    "DiagnosisDiagnosticNotification",
    "DiagnosisGenerateAgentDiagnosticLogsRequest",
    "DiagnosisGenerateCloudScannerDiagnosticLogsRequest",
    "DiagnosisGenerateConsoleDiagnosticLogsRequest",
    "DiagnosisGetDiagnosticLogsResponse",
    "DiagnosisNodeIdentifier",
    "DiagnosisNodeIdentifierNodeType",
    "DownloadScanResultsScanType",
    "FormDataModelRegistryGCRAddReq",
    "FormDataVulnerabilityDbDBUploadRequest",
    "GraphCloudProviderFilter",
    "GraphIndividualThreatGraph",
    "GraphIndividualThreatGraphRequest",
    "GraphIndividualThreatGraphRequestGraphType",
    "GraphIndividualThreatGraphRequestIssueType",
    "GraphNodeInfo",
    "GraphProviderThreatGraph",
    "GraphThreatFilters",
    "GraphThreatFiltersType",
    "GraphThreatGraph",
    "GraphThreatNodeInfo",
    "GraphThreatNodeInfoNodes",
    "GraphTopologyFilters",
    "IngestersCloudCompliance",
    "IngestersCloudComplianceScanStatus",
    "IngestersCloudResource",
    "IngestersCompliance",
    "IngestersComplianceScanStatus",
    "IngestersComplianceStats",
    "IngestersMalware",
    "IngestersMalwareScanStatus",
    "IngestersMetaRules",
    "IngestersReportIngestionData",
    "IngestersReportIngestionDataContainerBatchItem",
    "IngestersReportIngestionDataContainerEdgesBatchItem",
    "IngestersReportIngestionDataContainerImageBatchItem",
    "IngestersReportIngestionDataContainerImageEdgeBatchItem",
    "IngestersReportIngestionDataContainerProcessEdgeBatchItem",
    "IngestersReportIngestionDataEndpointEdgesBatchItem",
    "IngestersReportIngestionDataHostBatchItem",
    "IngestersReportIngestionDataHostsItem",
    "IngestersReportIngestionDataKubernetesClusterBatchItem",
    "IngestersReportIngestionDataKubernetesClusterEdgeBatchItem",
    "IngestersReportIngestionDataPodBatchItem",
    "IngestersReportIngestionDataPodEdgesBatchItem",
    "IngestersReportIngestionDataPodHostEdgesBatchItem",
    "IngestersReportIngestionDataProcessBatchItem",
    "IngestersReportIngestionDataProcessEdgesBatchItem",
    "IngestersSecret",
    "IngestersSecretMatch",
    "IngestersSecretRule",
    "IngestersSecretScanStatus",
    "IngestersSecretSeverity",
    "IngestersVulnerability",
    "IngestersVulnerabilityScanStatus",
    "LookupLookupFilter",
    "ModelAddScheduledTaskRequest",
    "ModelAgentId",
    "ModelAgentPluginDisable",
    "ModelAgentPluginEnable",
    "ModelAgentUpgrade",
    "ModelApiAuthRequest",
    "ModelApiTokenResponse",
    "ModelBasicNode",
    "ModelBulkDeleteScansRequest",
    "ModelBulkDeleteScansRequestScanType",
    "ModelCloudCompliance",
    "ModelCloudComplianceBenchmark",
    "ModelCloudComplianceScanDetails",
    "ModelCloudComplianceScanResult",
    "ModelCloudComplianceScanResultStatusCounts",
    "ModelCloudNodeAccountInfo",
    "ModelCloudNodeAccountInfoScanStatusMap",
    "ModelCloudNodeAccountRegisterReq",
    "ModelCloudNodeAccountRegisterReqCloudProvider",
    "ModelCloudNodeAccountRegisterReqMonitoredAccountIds",
    "ModelCloudNodeAccountRegisterResp",
    "ModelCloudNodeAccountRegisterRespData",
    "ModelCloudNodeAccountRegisterRespDataScans",
    "ModelCloudNodeAccountsListReq",
    "ModelCloudNodeAccountsListResp",
    "ModelCloudNodeCloudtrailTrail",
    "ModelCloudNodeComplianceControl",
    "ModelCloudNodeControlReq",
    "ModelCloudNodeControlReqCloudProvider",
    "ModelCloudNodeControlResp",
    "ModelCloudNodeEnableDisableReq",
    "ModelCloudNodeProvidersListResp",
    "ModelCloudResource",
    "ModelCompliance",
    "ModelComplianceRule",
    "ModelComplianceScanInfo",
    "ModelComplianceScanInfoSeverityCounts",
    "ModelComplianceScanResult",
    "ModelComplianceScanResultStatusCounts",
    "ModelComplianceScanStatusResp",
    "ModelComplianceScanTriggerReq",
    "ModelConnection",
    "ModelContainer",
    "ModelContainerDockerLabels",
    "ModelContainerImage",
    "ModelContainerImageMetadata",
    "ModelDownloadReportResponse",
    "ModelDownloadScanResultsResponse",
    "ModelEmailConfigurationAdd",
    "ModelEmailConfigurationResp",
    "ModelExportReport",
    "ModelFetchWindow",
    "ModelFiltersReq",
    "ModelFiltersReqHaving",
    "ModelFiltersResult",
    "ModelFiltersResultFilters",
    "ModelGenerateReportReq",
    "ModelGenerateReportReqDuration",
    "ModelGenerateReportReqReportType",
    "ModelGenerateReportResp",
    "ModelGetAuditLogsRequest",
    "ModelGraphResult",
    "ModelGraphResultEdges",
    "ModelGraphResultNodes",
    "ModelHost",
    "ModelImageStub",
    "ModelInitAgentReq",
    "ModelIntegrationAddReq",
    "ModelIntegrationAddReqConfig",
    "ModelIntegrationFilters",
    "ModelIntegrationListResp",
    "ModelIntegrationListRespConfig",
    "ModelInviteUserRequest",
    "ModelInviteUserRequestAction",
    "ModelInviteUserRequestRole",
    "ModelInviteUserResponse",
    "ModelKubernetesCluster",
    "ModelLoginRequest",
    "ModelLoginResponse",
    "ModelMalware",
    "ModelMalwareRule",
    "ModelMalwareScanResult",
    "ModelMalwareScanResultClass",
    "ModelMalwareScanResultRules",
    "ModelMalwareScanResultSeverityCounts",
    "ModelMalwareScanTriggerReq",
    "ModelMessageResponse",
    "ModelMetadata",
    "ModelNodeIdentifier",
    "ModelNodeIdentifierNodeType",
    "ModelNodesInScanResultRequest",
    "ModelNodesInScanResultRequestScanType",
    "ModelPasswordResetRequest",
    "ModelPasswordResetVerifyRequest",
    "ModelPod",
    "ModelPodKubernetesLabels",
    "ModelPostureProvider",
    "ModelProcess",
    "ModelRegisterInvitedUserRequest",
    "ModelRegistryAccount",
    "ModelRegistryAddReq",
    "ModelRegistryAddReqExtras",
    "ModelRegistryAddReqNonSecret",
    "ModelRegistryAddReqSecret",
    "ModelRegistryCountResp",
    "ModelRegistryImagesReq",
    "ModelRegistryImageStubsReq",
    "ModelRegistryListResp",
    "ModelRegistrySummaryAllResp",
    "ModelRegistryUpdateReq",
    "ModelRegistryUpdateReqExtras",
    "ModelRegistryUpdateReqNonSecret",
    "ModelRegistryUpdateReqSecret",
    "ModelResponseAccessToken",
    "ModelSbomRequest",
    "ModelSbomResponse",
    "ModelScanCompareReq",
    "ModelScanCompareResGithubComDeepfenceThreatMapperDeepfenceServerModelCloudCompliance",
    "ModelScanCompareResGithubComDeepfenceThreatMapperDeepfenceServerModelCompliance",
    "ModelScanCompareResGithubComDeepfenceThreatMapperDeepfenceServerModelMalware",
    "ModelScanCompareResGithubComDeepfenceThreatMapperDeepfenceServerModelSecret",
    "ModelScanCompareResGithubComDeepfenceThreatMapperDeepfenceServerModelVulnerability",
    "ModelScanFilter",
    "ModelScanInfo",
    "ModelScanInfoSeverityCounts",
    "ModelScanListReq",
    "ModelScanListResp",
    "ModelScanReportFieldsResponse",
    "ModelScanResultBasicNode",
    "ModelScanResultsActionRequest",
    "ModelScanResultsActionRequestScanType",
    "ModelScanResultsCommon",
    "ModelScanResultsMaskRequest",
    "ModelScanResultsMaskRequestMaskAction",
    "ModelScanResultsMaskRequestScanType",
    "ModelScanResultsReq",
    "ModelScanStatusReq",
    "ModelScanStatusResp",
    "ModelScanStatusRespStatuses",
    "ModelScanTriggerResp",
    "ModelSecret",
    "ModelSecretRule",
    "ModelSecretScanResult",
    "ModelSecretScanResultRules",
    "ModelSecretScanResultSeverityCounts",
    "ModelSecretScanTriggerReq",
    "ModelSettingsResponse",
    "ModelSettingUpdateRequest",
    "ModelSettingUpdateRequestKey",
    "ModelStopScanRequest",
    "ModelStopScanRequestScanType",
    "ModelSummary",
    "ModelTopologyDeltaReq",
    "ModelTopologyDeltaResponse",
    "ModelUpdateScheduledTaskRequest",
    "ModelUpdateUserIdRequest",
    "ModelUpdateUserIdRequestRole",
    "ModelUpdateUserPasswordRequest",
    "ModelUpdateUserRequest",
    "ModelUpdateUserRequestRole",
    "ModelUser",
    "ModelUserGroups",
    "ModelUserRegisterRequest",
    "ModelUserRole",
    "ModelVulnerability",
    "ModelVulnerabilityRule",
    "ModelVulnerabilityScanConfigLanguage",
    "ModelVulnerabilityScanConfigLanguageLanguage",
    "ModelVulnerabilityScanResult",
    "ModelVulnerabilityScanResultSeverityCounts",
    "ModelVulnerabilityScanTriggerReq",
    "PostgresqlDbGetAuditLogsRow",
    "PostgresqlDbScheduler",
    "PostgresqlDbSchedulerLastRanAt",
    "ReportersCompareFilter",
    "ReportersContainsFilter",
    "ReportersContainsFilterFilterIn",
    "ReportersFieldsFilters",
    "ReportersMatchFilter",
    "ReportersMatchFilterFilterIn",
    "ReportersOrderFilter",
    "ReportersOrderSpec",
    "ReportMetadata",
    "ReportRawReport",
    "SearchChainedSearchFilter",
    "SearchNodeCountResp",
    "SearchResultGroup",
    "SearchResultGroupResp",
    "SearchSearchCountResp",
    "SearchSearchCountRespCategories",
    "SearchSearchFilter",
    "SearchSearchNodeReq",
    "SearchSearchScanReq",
    "SqlNullTime",
    "UtilsAdvancedReportFilters",
    "UtilsReportFilters",
    "UtilsReportFiltersNodeType",
    "UtilsReportFiltersScanType",
    "UtilsReportFiltersSeverityOrCheckType",
    "UtilsScanSbomRequest",
)
