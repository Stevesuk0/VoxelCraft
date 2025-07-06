import Logger
import minecraft.client.resources.ResourceIndex as ResourceIndex
import minecraft.client.resources.DefaultResourcesPack as DefaultResourcesPack

class Minecraft:
    def __init__(self, gameConfig):
        self.mcDataDir = gameConfig.folderInfo.mcDataDir
        self.fileAssets = gameConfig.folderInfo.assetsDir
        self.fileResourcepacks = gameConfig.folderInfo.resourcePacksDir
        self.launchedVersion = gameConfig.gameInfo.version
        self.twitchDetails = gameConfig.userInfo.userProperties
        self.profileProperties = gameConfig.userInfo.profileProperties
        self.session = gameConfig.userInfo.session
        Logger.output("Setting user: " + self.session.getUsername())
        Logger.output("(Session ID is " + self.session.getSessionID() + ")")
        self.isDemo = gameConfig.gameInfo.isDemo
        self.tempDisplayWidth = gameConfig.displayInfo.width
        self.tempDisplayHeight = gameConfig.displayInfo.height
        self.fullscreen = gameConfig.displayInfo.fullscreen
        self.proxy = gameConfig.userInfo.proxy if gameConfig.userInfo.proxy is not None else False
        self.displayWidth = gameConfig.displayInfo.width if gameConfig.displayInfo.width > 0 else 1
        self.displayHeight = gameConfig.displayInfo.height if gameConfig.displayInfo.height > 0 else 1
        self.mcDefaultResourcePack = DefaultResourcesPack.DefaultResourcePack(ResourceIndex.ResourceIndex(gameConfig.folderInfo.assetsDir, gameConfig.folderInfo.assetIndex).getResourceMap())
        
        # self.sessionService = (new YggdrasilAuthenticationService(gameConfig.userInfo.proxy, UUID.randomUUID().toString())).createMinecraftSessionService()
        
        if gameConfig.serverInfo.serverName:
            self.serverName = gameConfig.serverInfo.serverName
            self.serverPort = gameConfig.serverInfo.serverPort
