import ruamel.yaml


class LoadFile:

    def __init__(self, path) -> None:
        self.path = path
        self.file = ""
        self.data = []
        
    def toJson(self):
        yaml = ruamel.yaml.YAML(type="safe")
        with open(self.path) as fpi:
            self.data = yaml.load(fpi)
        return self.data


print(ruamel)
