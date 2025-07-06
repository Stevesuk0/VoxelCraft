import time
import json
import atexit
import threading
import Logger

from dataclasses import dataclass
from typing import Optional

import voxelcraft.util.Session as Session
import voxelcraft.client.main.GameConfiguration

@dataclass
class GameConfiguration:
    class UserInformation:
        session: Session
        user_properties: dict
        profile_properties: dict
        proxy: Optional[tuple]

    class DisplayInformation:
        width: int
        height: int
        fullscreen: bool
        check_gl_errors: bool

    class folderInfo:
        game_dir: str
        resource_pack_dir: str
        assets_dir: str
        asset_index: Optional[str]

    class GameInformation:
        demo: bool
        version: str

    class ServerInformation:
        server: Optional[str]
        port: int


def main(args: dict):
    Logger.output("Hello, World!")

    opt_demo = args.get('demo', False)
    opt_fullscreen = args.get('fullscreen', False)
    opt_checkGlErrors = args.get('checkGlErrors', False)

    opt_server = args.get('server', None)
    opt_port = int(args.get('port', 25565))

    opt_gameDir = args.get('gameDir', ".")
    opt_assetsDir = args.get('assetsDir', None)
    opt_resourcePackDir = args.get('resourcePackDir', None)

    opt_proxyHost = args.get('proxyHost', None)
    opt_proxyPort = int(args.get('proxyPort', 8080))
    opt_proxyUser = args.get('proxyUser', None)
    opt_proxyPass = args.get('proxyPass', None)

    opt_username = args.get('username', "Player" + str(int(time.time() * 1000) % 1000))
    opt_uuid = args.get('uuid', None)

    opt_accessToken = args.get('accessToken')
    if opt_accessToken is None:
        raise ValueError("accessToken is required")

    opt_version = args.get('version')
    if opt_version is None:
        raise ValueError("version is required")

    opt_width = int(args.get('width', 854))
    opt_height = int(args.get('height', 480))

    opt_userProperties = args.get('userProperties', '{}')
    opt_profileProperties = args.get('profileProperties', '{}')

    opt_assetIndex = args.get('assetIndex', None)
    opt_userType = args.get('userType', 'legacy')

    non_options = args.get('_nonOptions', [])
    if non_options:
        print("Completely ignored arguments:", non_options)

    if opt_proxyHost is None:
        proxy = False
    else:
        proxy = ('SOCKS', (opt_proxyHost, int(opt_proxyPort)))

    property_map = json.loads(opt_userProperties)
    profile_property_map = json.loads(opt_profileProperties)
    
    opt_final_uuid = opt_uuid if opt_uuid else opt_username

    session = Session.Session(
        username=opt_username,
        player_id=opt_final_uuid,
        token=opt_accessToken,
        session_type_str=opt_userType
    )

    
    # atexit.register()

    game_configuration = voxelcraft.client.main.GameConfiguration.GameConfiguration(
        userInfo = voxelcraft.client.main.GameConfiguration.UserInformation(session, property_map, profile_property_map, proxy),
        displayInfo = voxelcraft.client.main.GameConfiguration.DisplayInformation(opt_width, opt_height, opt_fullscreen, opt_checkGlErrors),
        folderInfo = voxelcraft.client.main.GameConfiguration.FolderInformation(opt_gameDir, opt_resourcePackDir, opt_assetsDir, opt_assetIndex),
        gameInfo = voxelcraft.client.main.GameConfiguration.GameInformation(opt_demo, opt_version),
        serverInfo = voxelcraft.client.main.GameConfiguration.ServerInformation(opt_server, int(opt_port))
    )
    voxelcraft.client.voxelcraft.Minecraft(game_configuration)