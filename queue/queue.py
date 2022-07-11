from typing import Any


class Queue:
    """Queue class"""
    
    def __init__(self) -> None:
        
        self.item_list = []
        
    def add_item(self, item: Any) -> None:
        """Adds a new item to the end of the queue.

        Args:
            item (Any): An item that we want to add in the queue.
        """
        
        self.item_list.append(item)
        
    def delete_queue(self) -> None:
        """Deletes the queue."""
        
        self.item_list = []
        
    def is_queue_empty(self) -> bool:
        """verifies if the queue is empty.

        Returns:
            bool: True, if the queue is empty. Otherwise, False.
        """
        
        return len(self.item_list) == 0
    
    def remove_item(self) -> None:
        """Removes the first item in the queue."""
        
        if self.is_queue_empty():
            
            print("Empty queue!")
        else:
            
            del self.item_list[0]
    