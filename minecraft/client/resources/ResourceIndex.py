import Logger
import os
import json

class ResourceIndex: 
    def __init__(self, assetsDir, assetsIndex):
        self.resourceMap = {}

        if assetsIndex:
            file1 = os.path.join(assetsDir, 'objects')
            file2 = os.path.join(assetsDir, 'indexes/' + assetsIndex + '.json')

            try:
                with open(file2, encoding='utf-8') as f:
                    jsonobject = json.loads(f.read()).get('objects')

                if jsonobject: # mojang did this shit, fucking s2 jsonobject12
                    for s, jsonelement in jsonobject.items():
                        jsonobject2 = jsonelement  
                        s2 = jsonobject2["hash"]
                        
                        astring = s.split("/", 1)
                        if len(astring) == 1:
                            s1 = astring[0]
                        else:
                            s1 = astring[0] + ":" + astring[1]

                        file3 = os.path.join(file1, s2[:2], s2)

                        self.resourceMap[s1] = file3

            except json.JSONDecodeError:
                Logger.output(f'Unable to parse resource index file: {file2}', type=Logger.Type.ERROR)

            except FileNotFoundError:
                Logger.output(f'Can\'t find the resource index file: {file2}', type=Logger.Type.ERROR)

    def getResourceMap(self) -> dict:
        return self.resourceMap