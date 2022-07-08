from typing import Any


class Stack:
    """Stack class"""
    
    def __init__(self) -> None:
        
        self.item_list = []
        
    def delete_stack(self) -> None:
        """Deletes the stack."""
        
        self.item_list = []
        
    def is_stack_empty(self) -> bool:
        """Verifies if the stack is empty.

        Returns:
            bool: True, if the stack is empty. Otherwise, False.
        """
        
        return len(self.item_list) == 0    
        
    def pop_item(self) -> None:
        """Removes the element on the top of the stack."""
        if self.is_stack_empty():
            
            print("Empty stack!")
        else:
            
            self.item_list.pop()
    
    def push_item(self, item: Any) -> None:
        """Adds a new element to the top of the stack.

        Args:
            item (Any): The element that we want to add.
        """
        
        self.item_list.append(item)
    