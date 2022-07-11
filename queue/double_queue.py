from typing import Any


class DoubleQueue:
    """Double Queue class"""
    
    def __init__(self) -> None:
        
        self.item_list = []
        
    def add_item_at_the_end(self, item: Any) -> None:
        """Adds an item at the end of the double queue.

        Args:
            item (Any): An item that we want to add in the double queue.
        """
        
        self.item_list.append(item)
    
    def add_item_at_the_start(self, item: Any) -> None:
        """Adds an item at the start of the double queue.

        Args:
            item (Any): An item that we want to add in the double queue.
        """
        
        if self.is_double_queue_empty():
            
            self.item_list.append(item)
        else:
            
            self.item_list.insert(0, item)
    
    def delete_double_queue(self) -> None:
        """Deletes the double queue."""
        
        self.item_list = []
        
    def is_double_queue_empty(self) -> bool:
        """Verifies if the double queue is empty.

        Returns:
            bool: True, if the double queue is empty. Otherwise, False.
        """
        
        return len(self.item_list) == 0
    
    def remove_item_at_the_end(self) -> None:
        """Removes an item at the end of the double queue."""
        
        if self.is_double_queue_empty():
            
            print("Empty queue!")
        else:
            
            self.item_list.pop()
        
    def remove_item_at_the_start(self) -> None:
        """Removes an item at the start of the double queue."""
        
        if self.is_double_queue_empty():
            
            print("Empty queue!")
        else:
            
            del self.item_list[0]