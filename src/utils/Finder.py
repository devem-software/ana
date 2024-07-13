from typing import Union, List


class Find:
    def __init__():
        '''The above function is a Python constructor that does nothing.
        
        '''
        pass

    def array_in_array(super_array: List, array: List, position: int):
        '''The function checks if any sub-array in a super array matches a given array at a specific position.
        
        Parameters
        ----------
        super_array : List
            A list of lists containing arrays of elements.
        array : List
            The `array` parameter in the `array_in_array` function represents a list that you want to check for
        existence within the `super_array` parameter at a specific position indicated by the `position`
        parameter.
        position : int
            The `position` parameter in the `array_in_array` function represents the index at which you want to
        compare the elements of the `array` and the elements of each sub-array in the `super_array`.
        
        Returns
        -------
            a boolean value indicating whether there is any sub-array in the `super_array` where the element at
        the specified `position` matches the element at the same `position` in the given `array`.
        
        '''
        return any(n[position] == array[position] for n in super_array)

    # Si no encuentra una coincidencia retorna el nodo, de lo contrario retorna False
    def node_id(node: List, nodes: List) -> Union[List, bool]:
        '''The function `node_id` checks if a node is already present in a list of nodes and returns False if
        it is, otherwise it returns the node itself.
        
        Parameters
        ----------
        node : List
            The `node` parameter is a single element from a list of nodes. It seems to be a list itself, as
        indicated by the type hint `List`.
        nodes : List
            A list of nodes, where each node is represented as a list. Each node list contains information
        about the node, with the first element being the node ID.
        
        Returns
        -------
            If the node ID is not found in the list of nodes, the function will return the node ID. Otherwise,
        it will return `False`.
        
        '''
        for n in nodes:
            if n[0] == node[0]:
                return False
        return node

    def node_coords(node: List, nodes: List) -> Union[List, bool]:
        '''This function checks if a given node's coordinates already exist in a list of nodes and returns
        False if they do, otherwise it returns the node itself.
        
        Parameters
        ----------
        node : List
            The `node_coords` function takes two parameters:
        nodes : List
            The `nodes` parameter seems to be a list of lists where each inner list represents a node with at
        least four elements. The elements of a node are accessed using indices 1, 2, and 3.
        
        Returns
        -------
            If the function `node_coords` finds a node in the `nodes` list that has the same values at index 1,
        2, and 3 as the `node` parameter, it will return `False`. Otherwise, it will return the `node`
        parameter itself.
        
        '''

        for n in nodes:
            if n[1] == node[1] and n[2] == node[2] and n[3] == node[3]:
                return False
        return node


nodes = [
    ["0", 0, 1, 2],
    ["1", 0, 1, 2],
    ["2", 3, 4, 5],
    ["3", 6, 7, 8],
]
node = ["1", 9, 1, 8]

print(Find.node_id(nodes, node))
print(Find.node_coords(nodes, node))
