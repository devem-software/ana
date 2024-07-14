import ruamel.yaml


class LoadFile:

    def __init__(self, path) -> None:
        self.path = path + ".ana"
        self.file = ""
        self.data = []
        
    def toJson(self):
        yaml = ruamel.yaml.YAML(typ="safe")
        with open(self.path) as fpi:
            self.data = yaml.load(fpi)
        return self.data
