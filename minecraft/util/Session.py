import uuid
from typing import Optional

class GameProfile:
    def __init__(self, uuid_: Optional[uuid.UUID], name: str):
        self.uuid = uuid_
        self.name = name

    def __repr__(self):
        return f"GameProfile(uuid={self.uuid}, name={self.name})"


class SessionType:
    LEGACY = "legacy"
    MOJANG = "mojang"

    _SESSION_TYPES = {
        "legacy": LEGACY,
        "mojang": MOJANG,
    }

    @staticmethod
    def from_string(session_type_str: str):
        return SessionType._SESSION_TYPES.get(session_type_str.lower(), SessionType.LEGACY)


class Session:
    def __init__(self, username: str, player_id: str, token: str, session_type_str: str):
        self.username = username
        self.player_id = player_id
        self.token = token
        self.session_type = SessionType.from_string(session_type_str)

    def get_session_id(self) -> str:
        return f"token:{self.token}:{self.player_id}"

    def get_player_id(self) -> str:
        return self.player_id

    def get_username(self) -> str:
        return self.username

    def get_token(self) -> str:
        return self.token

    def get_profile(self) -> GameProfile:
        try:
            uuid_val = uuid.UUID(self.player_id)
        except ValueError:
            uuid_val = None
        return GameProfile(uuid_val, self.username)

    def get_session_type(self) -> str:
        return self.session_type
