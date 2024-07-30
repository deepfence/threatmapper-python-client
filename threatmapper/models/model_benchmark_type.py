from enum import Enum


class ModelBenchmarkType(str, Enum):
    AWS_FOUNDATIONAL_SECURITY = "aws_foundational_security"
    CIS = "cis"
    GDPR = "gdpr"
    HIPAA = "hipaa"
    NIST = "nist"
    NSA_CISA = "nsa-cisa"
    PCI = "pci"
    SOC_2 = "soc_2"

    def __str__(self) -> str:
        return str(self.value)
