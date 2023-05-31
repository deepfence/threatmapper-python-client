# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from threatmapper.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    AUTHENTICATION = "Authentication"
    COMMON = "Common"
    COMPLIANCE = "Compliance"
    TOPOLOGY = "Topology"
    SECRET_SCAN = "Secret Scan"
    MALWARE_SCAN = "Malware Scan"
    VULNERABILITY = "Vulnerability"
    CLOUD_NODES = "Cloud Nodes"
    CLOUD_RESOURCES = "Cloud Resources"
    CLOUD_SCANNER = "Cloud Scanner"
    CONTROLS = "Controls"
    DIAGNOSIS = "Diagnosis"
    INTEGRATION = "Integration"
    INTERNAL = "Internal"
    LOOKUP = "Lookup"
    REGISTRY = "Registry"
    REPORTS = "Reports"
    SCAN_RESULTS = "Scan Results"
    SEARCH = "Search"
    SETTINGS = "Settings"
    THREAT = "Threat"
    USER = "User"
