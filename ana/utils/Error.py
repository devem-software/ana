class Error:
    def __init__(self, noerror: int = ""):
        self.noerror = noerror

    def help(self):
        if self.noerror == "":
            return "Error no especificado"
