class ResourceLocation:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            domain, path = self.splitObjectName(args[0])
            self.resourceDomain = domain.lower() if domain else "minecraft"
            self.resourcePath = path
            if self.resourcePath is None:
                raise ValueError("resourcePath cannot be None")

        elif len(args) == 2 and all(isinstance(a, str) for a in args):
            domain, path = args
            self.resourceDomain = domain.lower() if domain else "minecraft"
            self.resourcePath = path
            if self.resourcePath is None:
                raise ValueError("resourcePath cannot be None")

        else:
            raise TypeError("Invalid constructor arguments for ResourceLocation")

    @staticmethod
    def splitObjectName(toSplit: str):
        idx = toSplit.find(':')
        if idx >= 0:
            domain = toSplit[:idx] if idx > 0 else None
            path = toSplit[idx + 1:]
            return domain, path
        else:
            return None, toSplit

    def getResourcePath(self):
        return self.resourcePath

    def getResourceDomain(self):
        return self.resourceDomain

    def __str__(self):
        return f"{self.resourceDomain}:{self.resourcePath}"

    def __eq__(self, other):
        if not isinstance(other, ResourceLocation):
            return False
        return (self.resourceDomain == other.resourceDomain and
                self.resourcePath == other.resourcePath)

    def __hash__(self):
        return hash(self.resourceDomain) * 31 + hash(self.resourcePath)
