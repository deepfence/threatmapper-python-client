from enum import Enum


class UtilsReportFiltersSeverityOrCheckType(str, Enum):
    AWS_FOUNDATIONAL_SECURITY = "aws_foundational_security"
    CIS = "cis"
    CRITICAL = "critical"
    GDPR = "gdpr"
    HIGH = "high"
    HIPAA = "hipaa"
    LOW = "low"
    MEDIUM = "medium"
    NIST = "nist"
    PCI = "pci"
    SOC_2 = "soc_2"

    def __str__(self) -> str:
        return str(self.value)
