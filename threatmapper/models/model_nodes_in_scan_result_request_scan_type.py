from enum import Enum


class ModelNodesInScanResultRequestScanType(str, Enum):
    CLOUDCOMPLIANCESCAN = "CloudComplianceScan"
    COMPLIANCESCAN = "ComplianceScan"
    MALWARESCAN = "MalwareScan"
    SECRETSCAN = "SecretScan"
    VULNERABILITYSCAN = "VulnerabilityScan"

    def __str__(self) -> str:
        return str(self.value)
