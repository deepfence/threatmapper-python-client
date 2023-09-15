from enum import Enum


class ModelStopScanRequestScanType(str, Enum):
    CLOUDCOMPLIANCESCAN = "CloudComplianceScan"
    COMPLIANCESCAN = "ComplianceScan"
    MALWARESCAN = "MalwareScan"
    SECRETSCAN = "SecretScan"
    VULNERABILITYSCAN = "VulnerabilityScan"

    def __str__(self) -> str:
        return str(self.value)
