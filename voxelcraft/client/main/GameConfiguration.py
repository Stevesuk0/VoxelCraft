from dataclasses import dataclass
from typing import Optional

@dataclass
class DisplayInformation:
    width: int
    height: int
    fullscreen: bool
    checkGlErrors: bool


@dataclass
class FolderInformation:
    mcDataDir: str
    resourcePacksDir: str
    assetsDir: str
    assetIndex: Optional[str]


@dataclass
class GameInformation:
    isDemo: bool
    version: str


@dataclass
class ServerInformation:
    serverName: Optional[str]
    serverPort: int


@dataclass
class UserInformation:
    session: object
    userProperties: dict
    profileProperties: dict
    proxy: Optional[tuple]


@dataclass
class GameConfiguration:
    userInfo: UserInformation
    displayInfo: DisplayInformation
    folderInfo: FolderInformation
    gameInfo: GameInformation
    serverInfo: ServerInformation
