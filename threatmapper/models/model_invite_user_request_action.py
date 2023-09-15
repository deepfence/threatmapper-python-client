from enum import Enum


class ModelInviteUserRequestAction(str, Enum):
    GET_INVITE_LINK = "get-invite-link"
    SEND_INVITE_EMAIL = "send-invite-email"

    def __str__(self) -> str:
        return str(self.value)
