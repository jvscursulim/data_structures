

class Node:
    """Node class"""
    
    def __init__(self, info, address, next_node_address = None) -> None:
        
        self.info = info
        self.address = address
        self.next_node_address = next_node_address