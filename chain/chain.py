from chain import Node


class Chain:
    """Chain class"""
    
    def __init__(self) -> None:
        
        self.nodes_list = []
        
    def add_node(self, node: Node) -> None:
        """Inserts a node in the Chain.

        Args:
            node (Node): A node that we want to add to the chain.

        Raises:
            TypeError: If the input is not a node.
        """
        
        if isinstance(node, Node):
        
            if self.is_chain_empty():
                
                self.nodes_list.append(node)
            else:
                
                node.next_node_address = self.nodes_list[0].address
                self.nodes_list.insert(0, node)
        else:
            
            raise TypeError("The input is not Node type!")
        
    def delete_chain(self) -> None:
        """Deletes the chain."""
        
        self.nodes_list = []
        
    def is_chain_empty(self) -> bool:
        """Verifies if the chain is empty.

        Returns:
            bool: True, if the chain is empty. False, if the chain is not empty.
        """
        
        return len(self.nodes_list) == 0
    
    def remove_node(self, element) -> None:
        """Removes a node of the chain.

        Args:
            element (_type_): The element stored in the node that will be removed.
        """
        if self.is_chain_empty():
            
            print("Empty chain!")
        else:
            
            if self.search_element(element = element):
                
                info_list = [node.info for node in self.nodes_list]
                index = info_list.index(element)
                
                if index == 0:
                    
                    self.nodes_list[1].next_node_address = None
                elif index == len(self.nodes_list) - 1:
                    
                    self.nodes_list[index - 1].next_node_address = None
                else:
                    
                    self.nodes_list[index - 1].next_node_address = self.nodes_list[index + 1].address
                
                del self.nodes_list[index]  
            else:
                
                print("This element is not present in the chain!")
    
    def search_element(self, element) -> bool:
        """Tells us if the input element is in some node of the chain.

        Args:
            element (_type_): The element that we are searching for.

        Returns:
            bool: True, if the element is present. False, if the element is not present.
        """
        info_list = [node.info for node in self.nodes_list]
        
        return element in info_list
            
    def show_nodes_info(self) -> None:
        """Prints the information stored in the nodes of the chain."""
        
        if self.is_chain_empty():
            
            print("Empty chain!")
        else:
            
            for node in self.nodes_list:
                
                print(node.info)