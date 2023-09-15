from enum import Enum


class GraphIndividualThreatGraphRequestGraphType(str, Enum):
    DIRECT_INTERNET_EXPOSURE = "direct_internet_exposure"
    INDIRECT_INTERNET_EXPOSURE = "indirect_internet_exposure"
    MOST_VULNERABLE_ATTACK_PATHS = "most_vulnerable_attack_paths"

    def __str__(self) -> str:
        return str(self.value)
