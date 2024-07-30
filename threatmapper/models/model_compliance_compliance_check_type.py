from enum import Enum


class ModelComplianceComplianceCheckType(str, Enum):
    GDPR = "gdpr"
    HIPAA = "hipaa"
    NIST = "nist"
    PCI = "pci"

    def __str__(self) -> str:
        return str(self.value)
