from enum import Enum


class ModelGenerateReportReqDuration(str, Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "7"
    VALUE_3 = "30"
    VALUE_4 = "60"
    VALUE_5 = "90"
    VALUE_6 = "180"

    def __str__(self) -> str:
        return str(self.value)
