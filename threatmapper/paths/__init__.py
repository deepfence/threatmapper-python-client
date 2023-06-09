# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from threatmapper.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    DEEPFENCE_APITOKEN = "/deepfence/api-token"
    DEEPFENCE_APITOKEN_RESET = "/deepfence/api-token/reset"
    DEEPFENCE_AUTH_TOKEN = "/deepfence/auth/token"
    DEEPFENCE_AUTH_TOKEN_REFRESH = "/deepfence/auth/token/refresh"
    DEEPFENCE_CLOUDNODE_ACCOUNT = "/deepfence/cloud-node/account"
    DEEPFENCE_CLOUDNODE_LIST_ACCOUNTS = "/deepfence/cloud-node/list/accounts"
    DEEPFENCE_CLOUDNODE_LIST_PROVIDERS = "/deepfence/cloud-node/list/providers"
    DEEPFENCE_CONTROLS_AGENT = "/deepfence/controls/agent"
    DEEPFENCE_CONTROLS_AGENTINIT = "/deepfence/controls/agent-init"
    DEEPFENCE_CONTROLS_AGENTUPGRADE = "/deepfence/controls/agent-upgrade"
    DEEPFENCE_CONTROLS_CLOUDNODE = "/deepfence/controls/cloud-node"
    DEEPFENCE_CONTROLS_CLOUDNODE_DISABLE = "/deepfence/controls/cloud-node/disable"
    DEEPFENCE_CONTROLS_CLOUDNODE_ENABLE = "/deepfence/controls/cloud-node/enable"
    DEEPFENCE_CONTROLS_KUBERNETESCLUSTER = "/deepfence/controls/kubernetes-cluster"
    DEEPFENCE_DATABASE_VULNERABILITY = "/deepfence/database/vulnerability"
    DEEPFENCE_DIAGNOSIS_AGENTLOGS = "/deepfence/diagnosis/agent-logs"
    DEEPFENCE_DIAGNOSIS_AGENTLOGS_STATUS_NODE_ID = "/deepfence/diagnosis/agent-logs/status/{node_id}"
    DEEPFENCE_DIAGNOSIS_CONSOLELOGS = "/deepfence/diagnosis/console-logs"
    DEEPFENCE_DIAGNOSIS_DIAGNOSTICLOGS = "/deepfence/diagnosis/diagnostic-logs"
    DEEPFENCE_DIAGNOSIS_NOTIFICATION = "/deepfence/diagnosis/notification"
    DEEPFENCE_ENDUSERLICENSEAGREEMENT = "/deepfence/end-user-license-agreement"
    DEEPFENCE_FILTERS_CLOUDCOMPLIANCE = "/deepfence/filters/cloud-compliance"
    DEEPFENCE_FILTERS_COMPLIANCE = "/deepfence/filters/compliance"
    DEEPFENCE_GRAPH_THREAT = "/deepfence/graph/threat"
    DEEPFENCE_GRAPH_THREAT_VULNERABILITY = "/deepfence/graph/threat/vulnerability"
    DEEPFENCE_GRAPH_TOPOLOGY_ = "/deepfence/graph/topology/"
    DEEPFENCE_GRAPH_TOPOLOGY_CONTAINERS = "/deepfence/graph/topology/containers"
    DEEPFENCE_GRAPH_TOPOLOGY_HOSTS = "/deepfence/graph/topology/hosts"
    DEEPFENCE_GRAPH_TOPOLOGY_KUBERNETES = "/deepfence/graph/topology/kubernetes"
    DEEPFENCE_GRAPH_TOPOLOGY_PODS = "/deepfence/graph/topology/pods"
    DEEPFENCE_INGEST_CLOUDCOMPLIANCE = "/deepfence/ingest/cloud-compliance"
    DEEPFENCE_INGEST_CLOUDCOMPLIANCESCANSTATUS = "/deepfence/ingest/cloud-compliance-scan-status"
    DEEPFENCE_INGEST_CLOUDRESOURCES = "/deepfence/ingest/cloud-resources"
    DEEPFENCE_INGEST_COMPLIANCE = "/deepfence/ingest/compliance"
    DEEPFENCE_INGEST_MALWARE = "/deepfence/ingest/malware"
    DEEPFENCE_INGEST_MALWARESCANLOGS = "/deepfence/ingest/malware-scan-logs"
    DEEPFENCE_INGEST_REPORT = "/deepfence/ingest/report"
    DEEPFENCE_INGEST_SBOM = "/deepfence/ingest/sbom"
    DEEPFENCE_INGEST_SECRETSCANLOGS = "/deepfence/ingest/secret-scan-logs"
    DEEPFENCE_INGEST_SECRETS = "/deepfence/ingest/secrets"
    DEEPFENCE_INGEST_SYNCREPORT = "/deepfence/ingest/sync-report"
    DEEPFENCE_INGEST_VULNERABILITIES = "/deepfence/ingest/vulnerabilities"
    DEEPFENCE_INGEST_VULNERABILITIESSCANLOGS = "/deepfence/ingest/vulnerabilities-scan-logs"
    DEEPFENCE_INTEGRATION = "/deepfence/integration"
    DEEPFENCE_INTEGRATION_INTEGRATION_ID = "/deepfence/integration/{integration_id}"
    DEEPFENCE_INTERNAL_CONSOLEAPITOKEN = "/deepfence/internal/console-api-token"
    DEEPFENCE_LOOKUP_CLOUDRESOURCES = "/deepfence/lookup/cloud-resources"
    DEEPFENCE_LOOKUP_CONTAINERIMAGES = "/deepfence/lookup/containerimages"
    DEEPFENCE_LOOKUP_CONTAINERS = "/deepfence/lookup/containers"
    DEEPFENCE_LOOKUP_HOSTS = "/deepfence/lookup/hosts"
    DEEPFENCE_LOOKUP_KUBERNETESCLUSTERS = "/deepfence/lookup/kubernetesclusters"
    DEEPFENCE_LOOKUP_PODS = "/deepfence/lookup/pods"
    DEEPFENCE_LOOKUP_PROCESSES = "/deepfence/lookup/processes"
    DEEPFENCE_LOOKUP_REGISTRYACCOUNT = "/deepfence/lookup/registryaccount"
    DEEPFENCE_REGISTRYACCOUNT = "/deepfence/registryaccount"
    DEEPFENCE_REGISTRYACCOUNT_COUNT_IMAGES = "/deepfence/registryaccount/count/images"
    DEEPFENCE_REGISTRYACCOUNT_COUNT_STUBS = "/deepfence/registryaccount/count/stubs"
    DEEPFENCE_REGISTRYACCOUNT_GCR = "/deepfence/registryaccount/gcr"
    DEEPFENCE_REGISTRYACCOUNT_IMAGES = "/deepfence/registryaccount/images"
    DEEPFENCE_REGISTRYACCOUNT_STUBS = "/deepfence/registryaccount/stubs"
    DEEPFENCE_REGISTRYACCOUNT_SUMMARY = "/deepfence/registryaccount/summary"
    DEEPFENCE_REGISTRYACCOUNT_REGISTRY_ID = "/deepfence/registryaccount/{registry_id}"
    DEEPFENCE_REGISTRYACCOUNT_REGISTRY_ID_SUMMARY = "/deepfence/registryaccount/{registry_id}/summary"
    DEEPFENCE_REGISTRYACCOUNT_REGISTRY_TYPE_SUMMARYBYTYPE = "/deepfence/registryaccount/{registry_type}/summary-by-type"
    DEEPFENCE_REPORTS = "/deepfence/reports"
    DEEPFENCE_REPORTS_REPORT_ID = "/deepfence/reports/{report_id}"
    DEEPFENCE_SCAN_LIST_CLOUDCOMPLIANCE = "/deepfence/scan/list/cloud-compliance"
    DEEPFENCE_SCAN_LIST_COMPLIANCE = "/deepfence/scan/list/compliance"
    DEEPFENCE_SCAN_LIST_MALWARE = "/deepfence/scan/list/malware"
    DEEPFENCE_SCAN_LIST_SECRET = "/deepfence/scan/list/secret"
    DEEPFENCE_SCAN_LIST_VULNERABILITY = "/deepfence/scan/list/vulnerability"
    DEEPFENCE_SCAN_NODESINRESULT = "/deepfence/scan/nodes-in-result"
    DEEPFENCE_SCAN_RESULTS_ACTION_DELETE = "/deepfence/scan/results/action/delete"
    DEEPFENCE_SCAN_RESULTS_ACTION_MASK = "/deepfence/scan/results/action/mask"
    DEEPFENCE_SCAN_RESULTS_ACTION_NOTIFY = "/deepfence/scan/results/action/notify"
    DEEPFENCE_SCAN_RESULTS_ACTION_UNMASK = "/deepfence/scan/results/action/unmask"
    DEEPFENCE_SCAN_RESULTS_CLOUDCOMPLIANCE = "/deepfence/scan/results/cloud-compliance"
    DEEPFENCE_SCAN_RESULTS_COMPLIANCE = "/deepfence/scan/results/compliance"
    DEEPFENCE_SCAN_RESULTS_COUNT_CLOUDCOMPLIANCE = "/deepfence/scan/results/count/cloud-compliance"
    DEEPFENCE_SCAN_RESULTS_COUNT_COMPLIANCE = "/deepfence/scan/results/count/compliance"
    DEEPFENCE_SCAN_RESULTS_COUNT_GROUP_MALWARE = "/deepfence/scan/results/count/group/malware"
    DEEPFENCE_SCAN_RESULTS_COUNT_GROUP_MALWARE_CLASS = "/deepfence/scan/results/count/group/malware/class"
    DEEPFENCE_SCAN_RESULTS_COUNT_GROUP_SECRET = "/deepfence/scan/results/count/group/secret"
    DEEPFENCE_SCAN_RESULTS_COUNT_MALWARE = "/deepfence/scan/results/count/malware"
    DEEPFENCE_SCAN_RESULTS_COUNT_SECRET = "/deepfence/scan/results/count/secret"
    DEEPFENCE_SCAN_RESULTS_COUNT_VULNERABILITY = "/deepfence/scan/results/count/vulnerability"
    DEEPFENCE_SCAN_RESULTS_MALWARE = "/deepfence/scan/results/malware"
    DEEPFENCE_SCAN_RESULTS_MALWARE_CLASS = "/deepfence/scan/results/malware/class"
    DEEPFENCE_SCAN_RESULTS_MALWARE_RULES = "/deepfence/scan/results/malware/rules"
    DEEPFENCE_SCAN_RESULTS_SECRET = "/deepfence/scan/results/secret"
    DEEPFENCE_SCAN_RESULTS_SECRET_RULES = "/deepfence/scan/results/secret/rules"
    DEEPFENCE_SCAN_RESULTS_VULNERABILITY = "/deepfence/scan/results/vulnerability"
    DEEPFENCE_SCAN_SBOM = "/deepfence/scan/sbom"
    DEEPFENCE_SCAN_SBOM_DOWNLOAD = "/deepfence/scan/sbom/download"
    DEEPFENCE_SCAN_START_COMPLIANCE = "/deepfence/scan/start/compliance"
    DEEPFENCE_SCAN_START_MALWARE = "/deepfence/scan/start/malware"
    DEEPFENCE_SCAN_START_SECRET = "/deepfence/scan/start/secret"
    DEEPFENCE_SCAN_START_VULNERABILITY = "/deepfence/scan/start/vulnerability"
    DEEPFENCE_SCAN_STATUS_CLOUDCOMPLIANCE = "/deepfence/scan/status/cloud-compliance"
    DEEPFENCE_SCAN_STATUS_COMPLIANCE = "/deepfence/scan/status/compliance"
    DEEPFENCE_SCAN_STATUS_MALWARE = "/deepfence/scan/status/malware"
    DEEPFENCE_SCAN_STATUS_SECRET = "/deepfence/scan/status/secret"
    DEEPFENCE_SCAN_STATUS_VULNERABILITY = "/deepfence/scan/status/vulnerability"
    DEEPFENCE_SCAN_STOP_COMPLIANCE = "/deepfence/scan/stop/compliance"
    DEEPFENCE_SCAN_STOP_MALWARE = "/deepfence/scan/stop/malware"
    DEEPFENCE_SCAN_STOP_SECRET = "/deepfence/scan/stop/secret"
    DEEPFENCE_SCAN_STOP_VULNERABILITY = "/deepfence/scan/stop/vulnerability"
    DEEPFENCE_SCAN_SCAN_TYPE_SCAN_ID = "/deepfence/scan/{scan_type}/{scan_id}"
    DEEPFENCE_SCAN_SCAN_TYPE_SCAN_ID_DOWNLOAD = "/deepfence/scan/{scan_type}/{scan_id}/download"
    DEEPFENCE_SCANS_BULK_DELETE = "/deepfence/scans/bulk/delete"
    DEEPFENCE_SCHEDULEDTASK = "/deepfence/scheduled-task"
    DEEPFENCE_SCHEDULEDTASK_ID = "/deepfence/scheduled-task/{id}"
    DEEPFENCE_SEARCH_CLOUDACCOUNTS = "/deepfence/search/cloud-accounts"
    DEEPFENCE_SEARCH_CLOUDCOMPLIANCE_SCANS = "/deepfence/search/cloud-compliance/scans"
    DEEPFENCE_SEARCH_CLOUDCOMPLIANCES = "/deepfence/search/cloud-compliances"
    DEEPFENCE_SEARCH_CLOUDRESOURCES = "/deepfence/search/cloud-resources"
    DEEPFENCE_SEARCH_COMPLIANCE_SCANS = "/deepfence/search/compliance/scans"
    DEEPFENCE_SEARCH_COMPLIANCES = "/deepfence/search/compliances"
    DEEPFENCE_SEARCH_CONTAINERS = "/deepfence/search/containers"
    DEEPFENCE_SEARCH_COUNT_CLOUDACCOUNTS = "/deepfence/search/count/cloud-accounts"
    DEEPFENCE_SEARCH_COUNT_CLOUDCOMPLIANCE_SCANS = "/deepfence/search/count/cloud-compliance/scans"
    DEEPFENCE_SEARCH_COUNT_CLOUDCOMPLIANCES = "/deepfence/search/count/cloud-compliances"
    DEEPFENCE_SEARCH_COUNT_CLOUDRESOURCES = "/deepfence/search/count/cloud-resources"
    DEEPFENCE_SEARCH_COUNT_COMPLIANCE_SCANS = "/deepfence/search/count/compliance/scans"
    DEEPFENCE_SEARCH_COUNT_COMPLIANCES = "/deepfence/search/count/compliances"
    DEEPFENCE_SEARCH_COUNT_CONTAINERS = "/deepfence/search/count/containers"
    DEEPFENCE_SEARCH_COUNT_HOSTS = "/deepfence/search/count/hosts"
    DEEPFENCE_SEARCH_COUNT_IMAGES = "/deepfence/search/count/images"
    DEEPFENCE_SEARCH_COUNT_KUBERNETESCLUSTERS = "/deepfence/search/count/kubernetes-clusters"
    DEEPFENCE_SEARCH_COUNT_MALWARE_SCANS = "/deepfence/search/count/malware/scans"
    DEEPFENCE_SEARCH_COUNT_MALWARES = "/deepfence/search/count/malwares"
    DEEPFENCE_SEARCH_COUNT_NODES = "/deepfence/search/count/nodes"
    DEEPFENCE_SEARCH_COUNT_PODS = "/deepfence/search/count/pods"
    DEEPFENCE_SEARCH_COUNT_SECRET_SCANS = "/deepfence/search/count/secret/scans"
    DEEPFENCE_SEARCH_COUNT_SECRETS = "/deepfence/search/count/secrets"
    DEEPFENCE_SEARCH_COUNT_VULNERABILITIES = "/deepfence/search/count/vulnerabilities"
    DEEPFENCE_SEARCH_COUNT_VULNERABILITY_SCANS = "/deepfence/search/count/vulnerability/scans"
    DEEPFENCE_SEARCH_HOSTS = "/deepfence/search/hosts"
    DEEPFENCE_SEARCH_IMAGES = "/deepfence/search/images"
    DEEPFENCE_SEARCH_KUBERNETESCLUSTERS = "/deepfence/search/kubernetes-clusters"
    DEEPFENCE_SEARCH_MALWARE_SCANS = "/deepfence/search/malware/scans"
    DEEPFENCE_SEARCH_MALWARES = "/deepfence/search/malwares"
    DEEPFENCE_SEARCH_PODS = "/deepfence/search/pods"
    DEEPFENCE_SEARCH_SECRET_SCANS = "/deepfence/search/secret/scans"
    DEEPFENCE_SEARCH_SECRETS = "/deepfence/search/secrets"
    DEEPFENCE_SEARCH_VULNERABILITIES = "/deepfence/search/vulnerabilities"
    DEEPFENCE_SEARCH_VULNERABILITY_SCANS = "/deepfence/search/vulnerability/scans"
    DEEPFENCE_SETTINGS_EMAIL = "/deepfence/settings/email"
    DEEPFENCE_SETTINGS_EMAIL_CONFIG_ID = "/deepfence/settings/email/{config_id}"
    DEEPFENCE_SETTINGS_GLOBALSETTINGS = "/deepfence/settings/global-settings"
    DEEPFENCE_SETTINGS_GLOBALSETTINGS_ID = "/deepfence/settings/global-settings/{id}"
    DEEPFENCE_SETTINGS_USERACTIVITYLOG = "/deepfence/settings/user-activity-log"
    DEEPFENCE_USER = "/deepfence/user"
    DEEPFENCE_USER_INVITE = "/deepfence/user/invite"
    DEEPFENCE_USER_INVITE_REGISTER = "/deepfence/user/invite/register"
    DEEPFENCE_USER_LOGIN = "/deepfence/user/login"
    DEEPFENCE_USER_LOGOUT = "/deepfence/user/logout"
    DEEPFENCE_USER_PASSWORD = "/deepfence/user/password"
    DEEPFENCE_USER_REGISTER = "/deepfence/user/register"
    DEEPFENCE_USER_RESETPASSWORD_REQUEST = "/deepfence/user/reset-password/request"
    DEEPFENCE_USER_RESETPASSWORD_VERIFY = "/deepfence/user/reset-password/verify"
    DEEPFENCE_USERS = "/deepfence/users"
    DEEPFENCE_USERS_ID = "/deepfence/users/{id}"
