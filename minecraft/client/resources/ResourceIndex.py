import os
import json
import Logger

class ResourceIndex:
    def __init__(self, assetsDir: str, assetsIndex: str):
        self.resourceMap: dict[str, str] = {}

        if assetsIndex is not None:
            file1 = os.path.join(assetsDir, "objects")
            file2 = os.path.join(assetsDir, "indexes", f"{assetsIndex}.json")

            try:
                with open(file2, "r", encoding="utf-8") as f:
                    jsonobject = json.load(f)

                jsonobject1 = jsonobject.get("objects", None)

                if jsonobject1 is not None:
                    for s, jsonobject2 in jsonobject1.items():
                        astring = s.split("/", 1)
                        s1 = astring[0] if len(astring) == 1 else f"{astring[0]}:{astring[1]}"
                        s2 = jsonobject2.get("hash")
                        if s2 is None:
                            continue
                        file3 = os.path.join(file1, s2[:2], s2)
                        self.resourceMap[s1] = file3

            except json.JSONDecodeError:
                Logger.output(f"Unable to parse resource index file: {file2}", type=Logger.Type.ERROR)
            except FileNotFoundError:
                Logger.output(f"Can't find the resource index file: {file2}", type=Logger.Type.ERROR)

    def getResourceMap(self) -> dict:
        return self.resourceMap
