import ruamel.yaml


class Json2Py:
    def __init__(self, path: str):
        self.path = path
        self.file = ""
        self.data = {}

    def get(self):
        yaml = ruamel.yaml.YAML(typ="safe")
        with open(self.path) as fpi:
            self.data = yaml.load(fpi)
        return self.data
