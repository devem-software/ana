class Find:
    def __init__(): # type: ignore
        pass

    def array_in_array(super_array: list, array: list, position: int): # type: ignore
        return any(n[position] == array[position] for n in super_array)

    # Si no encuentra una coincidencia retorna el nodo, de lo contrario retorna False
    def node_id(node: list, nodes: list): # type: ignore
        for n in nodes:
            if n[0] == node[0]:
                return False
        return node

    def node_coords(node: list, nodes: list): # type: ignore
        for n in nodes:
            if n[1] == node[1] and n[2] == node[2] and n[3] == node[3]:
                return False
        return node

