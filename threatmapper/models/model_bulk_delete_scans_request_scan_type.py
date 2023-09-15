from enum import Enum


class ModelBulkDeleteScansRequestScanType(str, Enum):
    CLOUDCOMPLIANCE = "CloudCompliance"
    COMPLIANCE = "Compliance"
    MALWARE = "Malware"
    SECRET = "Secret"
    VULNERABILITY = "Vulnerability"

    def __str__(self) -> str:
        return str(self.value)
