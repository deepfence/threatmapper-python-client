from enum import Enum


class UtilsReportOptionsSbomFormat(str, Enum):
    CYCLONEDX_JSON1_5 = "cyclonedx-json@1.5"
    SPDX_JSON2_2 = "spdx-json@2.2"
    SPDX_JSON2_3 = "spdx-json@2.3"
    SYFT_JSON11_0_1 = "syft-json@11.0.1"

    def __str__(self) -> str:
        return str(self.value)
