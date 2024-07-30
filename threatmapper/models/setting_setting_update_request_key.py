from enum import Enum


class SettingSettingUpdateRequestKey(str, Enum):
    CONSOLE_URL = "console_url"
    FILE_SERVER_URL = "file_server_url"
    INACTIVE_DELETE_SCAN_RESULTS = "inactive_delete_scan_results"

    def __str__(self) -> str:
        return str(self.value)
