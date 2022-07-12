class Node:
    """Node class."""
    
    def __init__(self, info, address, next_node_address = None) -> None:
        
        self.info = info
        self.address = address
        self.next_node_address = next_node_address
        
        
class NodeForDoubleChain(Node):
    """A child class of the class Node that is used in Double Chain."""
    
    def __init__(self, info, address, next_node_address = None, previous_node_address = None) -> None:
        
        super().__init__(info, address, next_node_address)
        self.previous_node_address = previous_node_address