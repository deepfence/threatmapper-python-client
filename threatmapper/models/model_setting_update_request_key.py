from enum import Enum


class ModelSettingUpdateRequestKey(str, Enum):
    CONSOLE_URL = "console_url"
    INACTIVE_DELETE_SCAN_RESULTS = "inactive_delete_scan_results"

    def __str__(self) -> str:
        return str(self.value)
