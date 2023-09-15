from enum import IntEnum


class ModelGenerateReportReqDuration(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_7 = 7
    VALUE_30 = 30
    VALUE_60 = 60
    VALUE_90 = 90
    VALUE_180 = 180

    def __str__(self) -> str:
        return str(self.value)
