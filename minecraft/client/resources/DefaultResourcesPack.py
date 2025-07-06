from typing import Set, TypeVar, Optional, Dict, IO
from io import BytesIO
from PIL import Image
import os

from minecraft.util import ResourceLocation
from minecraft.client.renderer.texture import TextureUtil

T = TypeVar('T')  

class DefaultResourcePack:
    defaultResourceDomains: Set[str] = {"minecraft", "realms"}

    def __init__(self, mapAssets: Dict[str, str]):
        self.mapAssets = mapAssets

    def getInputStream(self, location: ResourceLocation) -> IO[bytes]:
        inputstream = self.getResourceStream(location)
        if inputstream:
            return inputstream
        inputstream1 = self.getInputStreamAssets(location)
        if inputstream1:
            return inputstream1
        raise FileNotFoundError(location.getResourcePath())

    def getInputStreamAssets(self, location: ResourceLocation) -> Optional[IO[bytes]]:
        path = self.mapAssets.get(str(location))
        if path and os.path.isfile(path):
            return open(path, 'rb')
        return None

    def getResourceStream(self, location: ResourceLocation) -> Optional[IO[bytes]]:
        return None

    def resourceExists(self, location: ResourceLocation) -> bool:
        return self.getResourceStream(location) is not None or str(location) in self.mapAssets

    def getResourceDomains(self) -> Set[str]:
        return self.defaultResourceDomains

    def getPackMetadata(self, metadataSerializer, metadataSectionName: str) -> Optional[T]:
        try:
            path = self.mapAssets.get("pack.mcmeta")
            if not path:
                return None
            with open(path, 'r', encoding='utf-8') as f:
                return metadataSerializer.readMetadata(f, metadataSectionName)
        except (RuntimeError, FileNotFoundError):
            return None

    def getPackImage(self) -> Image.Image:
        stream = self.getResourceStream(ResourceLocation("pack.png"))
        if stream:
            return TextureUtil.readBufferedImage(stream)
        else:
            raise FileNotFoundError("pack.png not found")

    def getPackName(self) -> str:
        return "Default"
