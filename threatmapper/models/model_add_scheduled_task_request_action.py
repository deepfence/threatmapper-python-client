from enum import Enum


class ModelAddScheduledTaskRequestAction(str, Enum):
    CLOUDCOMPLIANCESCAN = "CloudComplianceScan"
    COMPLIANCESCAN = "ComplianceScan"
    MALWARESCAN = "MalwareScan"
    SECRETSCAN = "SecretScan"
    VULNERABILITYSCAN = "VulnerabilityScan"

    def __str__(self) -> str:
        return str(self.value)
