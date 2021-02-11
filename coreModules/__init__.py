import json
__all__ = []
with open('modules.json') as modules_file:
    data = json.load(modules_file)
    print(data)
    for atr in data["coreModules"]:
        print(atr["name"])
        __all__.append(atr["name"])
print(__all__)

