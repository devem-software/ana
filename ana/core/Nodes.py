from ..utils.Finder import Find
from ..utils.Error import Error

class Nodes:
    def __init__(self, id:str ="", cx:float = 0.0, cy:float = 0.0, cz:float = 0.0, ):
        self.nodes: list = []
        self.id:str
        self.cx: float
        self.cy: float
        self.cz: float
        self.node = [self.id, self.cx, self.cy, self.cz]

    def add(self):
        exists_node = Find.node_id(self.node,  self.nodes) # type: ignore
        coords_duplicate = Find.node_coords(self.node, self.nodes) # type: ignore
        if not exists_node:
            if not coords_duplicate:
                self.nodes.append(self.node)
            else:
                Error("N101").help()
        else: