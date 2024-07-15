import json
import os

class Error:
    def __init__(self, noerror: str = "", custom_msg:str = ""):
        self.error = {}
        self.noerror = noerror
        self.custom_msg = custom_msg
        
        path_errors = os.path.join(os.getcwd(), 'ana', 'libs','Errors.json')
        
        with open(path_errors) as f:
            self.errors = json.load(f)
        
        id = "".join(i for i in self.noerror if not i.isdigit())
        range = "".join(i for i in self.noerror if i.isdigit())

        group_name =self.errors["info"].get(id,"Grupo desconocido")
        group_errors = self.errors.get(group_name, {}).get("errors", {})
        group_range = self.errors.get(group_name, {}).get("range", {})

        # start, end = map(int, group_range.split('-'))
        # range_list = list(range(start, end + 1))
        

        self.error = group_errors.get(self.noerror, {"msg": "Error no encontrado", "help": ""})
        # print(id, range, group_name, group_range)

    def help(self):
        print(self.error["msg"])
        if self.custom_msg != "":
            print(self.custom_msg)
        print(self.error["help"])

Error("G101")